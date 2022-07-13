import glob
import json
import logging
import os
import random
import re
import uuid
import yaml
from flask import request


from bert.bertqa import BertQA
from dm.Response import Response
from dm.state import State
from nlu.rasa_nlu import RasaNLU, RasaIntent
from bert.utils import Context
from utils.queue_query import QueueQuery

NLU_CONF_THRESHOLD = 0.6


class CheifBot:

    def __init__(self, logger: logging): 
        self._nlu = RasaNLU()
        self._logger = logger

        # load BERT model and context for the system
        with open(os.path.join(os.getcwd(), 'conf', 'bert_confg.yml')) as bert_config_file:
            configs = yaml.safe_load(bert_config_file)
        self._bert_model = BertQA(configs)

        with open(os.path.join(os.getcwd(), 'data', 'bert_context', 'bert_context.yml'),
                  "r") as bert_context_file:
            self._bert_context = yaml.safe_load(bert_context_file)

        # load BERT model and context for the system
        with open(os.path.join(os.getcwd(), 'conf', 'civil.yml')) as bert_config_file:
            configs = yaml.safe_load(bert_config_file)
        self._nlu_url = configs.get('SERVICES').get('nlu')


        # load setup for the system
        with open(os.path.join(os.getcwd(), 'data', 'domain.yml')) as domain_file:
            _domain = yaml.safe_load(domain_file)

        self.system_actions = _domain.get('actions')
        self.user_intents = _domain.get('intents')
        self.dialog_slots = State(state_config=_domain.get('slots'))
        self.dialogue_history = QueueQuery(_domain.get('pre_turn_number'))

        self._logger.debug('self.dialog_slots[{}]: {}'.format(len(self.dialog_slots), self.dialog_slots))
        self._logger.debug(
            'self.dialogue_history[{}]: {}'.format(len(self.dialogue_history.query_queue), self.dialogue_history))

        with open(os.path.join(os.getcwd(), 'data', 'dm', 'recipe_intent_map.yaml'),
                  "r") as recipe_intent_map_file:
            self.recipe_intent_map = yaml.safe_load(recipe_intent_map_file)
        self._logger.debug('self.recipe_intent_map[{}]: {}'.format(len(self.recipe_intent_map), self.recipe_intent_map))

        # loading NLG templates
        response_files = glob.glob(
            os.path.join(os.getcwd(), 'data', 'response', '*.yaml'))
        self._logger.debug('files: {}'.format(response_files))
        self.responses = {}
        for file in response_files:
            with open(file, 'r') as yaml_file:
                self.responses.update(yaml.safe_load(yaml_file))
        self._logger.debug('self.responses[{}]: {}'.format(len(self.responses), self.responses))

        # loading DM rules and segments
        with open(os.path.join(os.getcwd(), 'data', 'dm', 'segments.yaml'),
                  "r") as segments_file:
            _segments = yaml.safe_load(segments_file)
            _segments = {item.get('steps')[0].get('intent'): item.get('steps')[1].get('action') for item in
                         _segments.get('segments')}
            self.rules_regex = {re.compile(k, re.I): v for k, v in _segments.items()}

        with open(os.path.join(os.getcwd(), 'data', 'dm', 'custom_stories.yaml'),
                  "r") as custom_stories_file:
            _custom_stories = yaml.safe_load(custom_stories_file)
            _custom_stories = {item.get('steps')[0].get('intent'): item.get('steps')[1].get('action') for item in
                               _custom_stories.get('segments')}
            self.rules_regex.update({re.compile(k, re.I): v for k, v in _custom_stories.items()})

        with open(os.path.join(os.getcwd(), 'data', 'dm', 'rules.yml'),
                  "r") as rules_file:
            _rules = yaml.safe_load(rules_file)
            _rules = {item.get('intent'): item.get('conditions') for item in _rules.get('rules')}
            self.rules_regex.update({re.compile(k, re.I): v for k, v in _rules.items()})

        self._logger.debug('self.rules_regex[{}]: {}'.format(len(self.rules_regex), self.rules_regex))

    def get(self):
        """ Overwrites super GET function to ensure GET requests are ignored."""
        pass

    def post(self):
        """ Handles POST requests from corona_main.py.
        Returns:
            response [json] -- Json with response object.
        """
        request_data = request.get_json(force=True)
        user_sentence = request_data.get("raw_text")

        _response = {'result': self.get_answer(user_sentence), 'dialog_history': self.dialogue_history.query_queue}
        return _response

    def get_answer(self, session_id: str, user_sentence: str, intent_info: str = None):
        self._logger.info('session_id: {}'.format(session_id))
        self._logger.info('user_sentence: {}'.format(user_sentence))

        if intent_info:
            intent = RasaIntent()
            intent.type = intent_info
            intent.confidence = 1.0
            intent.entities = {}
        else:
            import requests
            # get NLU results
            r = requests.post(self._nlu_url, data=json.dumps({"text": user_sentence}))
            self._logger.info('nlu results: {}'.format(r.json()))
            if r.status_code == 200:
                intent = self._nlu.process_user_sentence(r.json())

        # self.response = Response()
        if intent.confidence and intent.confidence <= NLU_CONF_THRESHOLD:
            _context = list()
            _context.append(Context(idx='r', title='r', text=self._bert_context.get('r')))
            _context.append(Context(idx=self.dialog_slots.get('recipe_ID'),
                                    title=self.dialog_slots.get('recipe_ID'),
                                    text=self._bert_context.get(self.dialog_slots.get('recipe_ID'))))
            _response = self._bert_model.predict(user_sentence, _context)
            return {"system_action": "",
                    "response": _response,
                    "stateInfo": self.dialog_slots}


        # append the latest user input into the dialogue history
        self.dialogue_history.add(speaker="user", turn_data={"user_text": user_sentence, "rasa": intent})
        self._fill_slots(intent.entities)

        if "(" in intent.type:
            self.dialog_slots.add('requested_ingredient', self.find_between_r(intent.type, "(", ")"))

        recipe_id = self.recipe_intent_map.get(intent.type)
        self._logger.info('{intent} --> {recipe_id}'.format(intent=intent.type, recipe_id=recipe_id))

        if recipe_id:
            self.dialog_slots.add('meal_type', intent.type)
            self.dialog_slots.add('recipe_ID', recipe_id)
            self.dialog_slots.add('recipe_step_ID', list(self.responses.get('utter_rep').get(recipe_id).keys())[0])

        # Rule-based DM
        system_action = self.search_for_response_action(intent=intent.type)
        self.dialog_slots.add('last_action', system_action)

        if intent.type == 'search_utensils':
            _context = list()
            _context.append(Context(idx='r', title='r', text=self._bert_context.get('r')))
            _context.append(Context(idx=self.dialog_slots.get('recipe_ID'),
                                    title=self.dialog_slots.get('recipe_ID'),
                                    text=self._bert_context.get(self.dialog_slots.get('recipe_ID'))))
            _response = self._bert_model.predict(user_sentence, _context)
            return {"system_action": "",
                    "response": _response,
                    "stateInfo": self.dialog_slots}
        # NLG
        if system_action == 'utter_rep':
            recipe_id = self.dialog_slots.get('recipe_ID')
            recipe_responses = self.responses.get(system_action).get(recipe_id)
            _response = recipe_responses.get(self.dialog_slots.get('recipe_step_ID'))
            self.dialog_slots.add('recipe_step_ID', self.dialog_slots.get('recipe_step_ID') + 1)

        elif system_action == 'utter_utensils':
            utensils_entity = intent.entities.get('utensils')
            print("response: {}".format(self.responses.keys()))
            _response = self.responses.get(system_action).get(utensils_entity)
            _response = random.choice(_response)

        # elif system_action == 'action_search_rec':
        #     # TODO: Linked to the Bert QA model for question answering
        #     pass

        elif system_action == 'utter_replace':
            requested_ingredient = self.dialog_slots.get('requested_ingredient')
            response_examples = self.responses.get(system_action).get(requested_ingredient)
            _response = random.choice(response_examples)
        else:
            response_examples = self.responses.get(system_action)
            self._logger.info('current response_examples for {}: {}'.format(system_action, response_examples))
            _response = random.choice(response_examples)

        self.dialog_slots.add('sys_q_type', _response.get('qType'))

        self._logger.info('current dialogue state: {}'.format(self.dialog_slots))
        self._logger.info('current _response for {}: {}'.format(system_action, _response))

        return {"system_action": system_action,
                "response": _response,
                "stateInfo": self.dialog_slots}

    def search_for_response_action(self, intent: str, **kwargs):
        self._logger.info('current user intent: {}'.format(intent))
        self._logger.info('current dialogue state: {}'.format(self.dialog_slots))

        for pattern, action in self.rules_regex.items():
            # self._logger.info('(2) found searches: {}'.format(re.search(pattern, intent)))
            if re.search(pattern, intent):
                self._logger.info('matched intent: {}'.format(intent))
                if isinstance(action, str):
                    if "<" in action and ">" in action:
                        key = self.find_between_r(action, "<", ">")
                        action = action.replace("<{}>".format(key), self.dialog_slots.get(key))

                    self._logger.info('corresponding action : {}'.format(action))
                    return action

                elif isinstance(action, list):  # judge the rules by different states
                    for option in action:
                        state = option.get('state')
                        self._logger.info('state: {}'.format(state))
                        self._logger.info('matched? : {}'.format(state.items() <= self.dialog_slots.state.items()))
                        act = option.get('action')

                        if state.items() <= self.dialog_slots.state.items():
                            if "<" in act and ">" in act:
                                key = self.find_between_r(act, "<", ">")
                                act = act.replace("<{}>".format(key), self.dialog_slots.get(key))

                            self._logger.info('corresponding action : {}'.format(act))
                            return act

    def _fill_slots(self, entities: {}):
        if isinstance(entities, dict):
            for key, value in entities.items():
                self.dialog_slots.add(key, value)

    @staticmethod
    def find_between_r(origin_text: str, first: str, last: str):
        try:
            start = origin_text.rindex(first) + len(first)
            end = origin_text.rindex(last, start)
            return origin_text[start:end]
        except ValueError:
            return ""
