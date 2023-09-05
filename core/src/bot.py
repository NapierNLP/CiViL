import copy
import glob
import json
import logging
import os
import random
import re
import uuid
import yaml
from flask import request

import sql.sqlac
from bert.qamodel import BertQA
from dm.Response import Response
from dm.state import State
from nlu.rasa_nlu import RasaNLU, RasaIntent
from bert.utils import Context
from observ_pattern import Observer, Subject
from utility.queue_query import QueueQuery
from speech.asr import CivilAsr
import text_to_speech

NLU_CONF_THRESHOLD = 0.6


class CheifBot(Observer):

    def __init__(self, session_id: str, logger: logging, bert_enabled: bool = True):
        self.this_session = session_id
        self._nlu = RasaNLU()
        self._logger = logger
        self._bert_enabled = bert_enabled
        self._prev_dialogue_state = None
        self._existing_chats = {}


        if bert_enabled:
            # load BERT model and context for the system
            with open(os.path.join(os.getcwd(), 'conf', 'bert_confg.yml')) as bert_config_file:
                configs = yaml.safe_load(bert_config_file)
            self._bert_model = BertQA(configs, self._logger)

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

    def get_answer(self, user_sentence: str, intent_info: str = None, this_session: str = None):

        if this_session:
            self.this_session = this_session

        self._logger.info('session_id: {}'.format(self.this_session))
        # load the existing user
        try:
            self._prev_dialogue_state = copy.deepcopy(self.dialog_slots)
            # sql.sqlac.show_dialogues()
            # existing_record = sql.sqlac.find_record_by_id(session_id)
            existing_record = self._existing_chats.get(self.this_session)
            if existing_record:
                # self._prev_dialogue_state = json.loads(existing_record.dialogue_state)
                self._prev_dialogue_state = existing_record.get('stateInfo')
                self._logger.info(
                    'previous dialogue state by {} is: {}'.format(self.this_session, self._prev_dialogue_state))
            else:
                self._logger.info(
                    'NEW dialogue state for {} is: {}'.format(self.this_session, self._prev_dialogue_state))

            self._logger.info('user_sentence: {}'.format(user_sentence))

            if intent_info:
                intent = RasaIntent()
                intent.type = intent_info
                intent.confidence = 1.0
                intent.entities = {}
            else:
                import requests
                # get NLU results
                r = requests.post(self._nlu_url, data=json.dumps({"text": user_sentence.replace('\'', '').strip()}))
                self._logger.info('nlu results: {}'.format(r.json()))
                if r.status_code == 200:
                    intent = self._nlu.process_user_sentence(r.json())

            if intent.confidence and intent.confidence <= NLU_CONF_THRESHOLD:
                if self._bert_enabled:
                    _context = list()
                    _context.append(self._bert_context.get('r'))
                    if self._prev_dialogue_state.get('recipe_ID'):
                        _context.append(self._bert_context.get(
                            self._prev_dialogue_state.get('recipe_ID')))
                    _response = self._bert_model.predict(user_sentence, _context)

                    # sql.sqlac.insert_dialogue(session_id, json.dumps(self._prev_dialogue_state), "", json.dumps(_response))
                    result = {"system_action": "",
                              "response": _response,
                              "stateInfo": self._prev_dialogue_state}
                    self._existing_chats[self.this_session] = result
                    self._prev_dialogue_state = None
                    return result
                else:
                    # sql.sqlac.insert_dialogue(session_id, json.dumps(self._prev_dialogue_state), "",
                    #                           json.dumps({'text': "sorry, i can't understand your query."}))
                    result = {"system_action": "",
                              "response": {'text': "sorry, i can't understand your query."},
                              "stateInfo": self._prev_dialogue_state}
                    self._existing_chats[self.this_session] = result
                    self._prev_dialogue_state = None
                    return result

            # append the latest user input into the dialogue history
            self.dialogue_history.add(speaker="user", turn_data={"user_text": user_sentence, "rasa": intent})
            self._fill_slots(intent.entities)

            if "(" in intent.type:
                self._prev_dialogue_state.add('requested_ingredient', self.find_between_r(intent.type, "(", ")"))

            recipe_id = self.recipe_intent_map.get(intent.type)
            self._logger.info('{intent} --> {recipe_id}'.format(intent=intent.type, recipe_id=recipe_id))

            if recipe_id:
                self._prev_dialogue_state.add('meal_type', intent.type)
                self._prev_dialogue_state.add('recipe_ID', recipe_id)
                self._prev_dialogue_state.add('recipe_step_ID',
                                              list(self.responses.get('utter_rep').get(recipe_id).keys())[0])

            # Rule-based DM
            system_action = self.search_for_response_action(intent=intent.type)
            self._prev_dialogue_state.add('last_action', system_action)

            if intent.type == 'search_utensils':
                if self._bert_enabled:
                    _context = list()
                    _context.append(self._bert_context.get('r'))
                    if self._prev_dialogue_state.get('recipe_ID'):
                        _context.append(self._bert_context.get(
                            self._prev_dialogue_state.get('recipe_ID')))
                    _response = self._bert_model.predict(user_sentence, _context)

                    # sql.sqlac.insert_dialogue(self.this_session, json.dumps(self._prev_dialogue_state), "", json.dumps(_response))
                    result = {"system_action": "",
                              "response": _response,
                              "stateInfo": self._prev_dialogue_state}
                    self._existing_chats[self.this_session] = result
                    self._prev_dialogue_state = None
                    return result
                else:

                    # sql.sqlac.insert_dialogue(self.this_session, json.dumps(self._prev_dialogue_state), "",
                    #                           json.dumps({'text': "sorry, I'm still learning about this."}))
                    result = {"system_action": "",
                              "response": {'text': "sorry, I'm still learning about this."},
                              "stateInfo": self._prev_dialogue_state}
                    self._existing_chats[self.this_session] = result
                    self._prev_dialogue_state = None
                    return result

            # NLG
            if system_action == 'utter_rep':
                recipe_id = self._prev_dialogue_state.get('recipe_ID')
                recipe_responses = self.responses.get(system_action).get(recipe_id)
                _response = recipe_responses.get(self._prev_dialogue_state.get('recipe_step_ID'))
                self._prev_dialogue_state.add('recipe_step_ID', self._prev_dialogue_state.get('recipe_step_ID') + 1)

            elif system_action == 'utter_utensils':
                utensils_entity = intent.entities.get('utensils')
                print("response: {}".format(self.responses.keys()))
                _response = self.responses.get(system_action).get(utensils_entity)
                _response = random.choice(_response)

            elif system_action == 'utter_replace':
                requested_ingredient = self._prev_dialogue_state.get('requested_ingredient')
                response_examples = self.responses.get(system_action).get(requested_ingredient)
                _response = random.choice(response_examples)
            else:
                response_examples = self.responses.get(system_action)
                self._logger.info('current response_examples for {}: {}'.format(system_action, response_examples))
                _response = random.choice(response_examples)

            self._prev_dialogue_state.add('sys_q_type', _response.get('qType'))

            self._logger.info('current dialogue state: {}'.format(self._prev_dialogue_state))
            self._logger.info('current _response for {}: {}'.format(system_action, _response))

            # sql.sqlac.insert_dialogue(self.this_session, json.dumps(self._prev_dialogue_state),
            #                           system_action, json.dumps(_response))
            result = {"system_action": system_action,
                      "response": _response,
                      "stateInfo": self._prev_dialogue_state}
            self._existing_chats[self.this_session] = result
            self._prev_dialogue_state = None
            return result

        except Exception as e:
            self._logger.error(e)
            result = {"system_action": "",
                      "response": {"text": "sorry, I don't understand what you said."},
                      "stateInfo": self._prev_dialogue_state}
            self._existing_chats[self.this_session] = result
            self._prev_dialogue_state = None
            return result

    def search_for_response_action(self, intent: str, **kwargs):
        self._logger.info('current user intent: {}'.format(intent))
        self._logger.info('current dialogue state: {}'.format(self._prev_dialogue_state))

        for pattern, action in self.rules_regex.items():
            # self._logger.info('(2) found searches: {}'.format(re.search(pattern, intent)))
            if re.search(pattern, intent):
                self._logger.info('matched intent: {}'.format(intent))
                if isinstance(action, str):
                    if "<" in action and ">" in action:
                        key = self.find_between_r(action, "<", ">")
                        action = action.replace("<{}>".format(key), self._prev_dialogue_state.get(key))

                    self._logger.info('corresponding action : {}'.format(action))
                    return action

                elif isinstance(action, list):  # judge the rules by different states
                    for option in action:
                        state = option.get('state')
                        self._logger.info('state: {}'.format(state))
                        self._logger.info(
                            'matched? : {}'.format(state.items() <= self._prev_dialogue_state.state.items()))
                        act = option.get('action')

                        if state.items() <= self._prev_dialogue_state.state.items():
                            if "<" in act and ">" in act:
                                key = self.find_between_r(act, "<", ">")
                                act = act.replace("<{}>".format(key), self._prev_dialogue_state.get(key))

                            self._logger.info('corresponding action : {}'.format(act))
                            return act

    def _fill_slots(self, entities: {}):
        if isinstance(entities, dict):
            for key, value in entities.items():
                self._prev_dialogue_state.add(key, value)

    @staticmethod
    def find_between_r(origin_text: str, first: str, last: str):
        try:
            start = origin_text.rindex(first) + len(first)
            end = origin_text.rindex(last, start)
            return origin_text[start:end]
        except ValueError:
            return ""

    def update(self, subject: Subject) -> None:
        print("subject._recognised_text: {}".format(subject.recognised_text))
        text = self.get_answer(subject.recognised_text)
        response_text = text.get("response").get('text')
        text_to_speech.synthesize_text(response_text)


def terminal_test(logger: logging):
    this_session = str(uuid.uuid1())
    prompt = "  \033[90mUSER >\033[0m "
    bot = CheifBot(this_session, logger)
    _logger = logger

    # MAIN LOOP
    while True:
        # Read user input
        user_input = input(prompt)

        # Clear screen if requested by the user
        if user_input == "clear":
            os.system('clear')
            continue


        _logger.info(bot.get_answer(this_session, user_input))


def speech_pipeline(logger):
    this_session = str(uuid.uuid1())
    bot = CheifBot(this_session, logger)
    sub = CivilAsr()
    sub.attach(bot)
    sub.set_new_model()
    sub.start()


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
    )
    logger = logging.getLogger(__name__)

    speech_pipeline(logger)
