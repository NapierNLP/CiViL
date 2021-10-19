import glob
import os
import random
import re
import uuid
from argparse import ArgumentParser

import requests
import yaml
from flask import request

from core.dm.state import State
from core.nlu.rasa_nlu import RasaNLU, RasaIntent
from core.utils.queue_query import QueueQuery


class CheifBot:

    def __init__(self):
        self._nlu = RasaNLU()

        # load setup for the system
        with open(os.path.join(os.getcwd().replace('core/dm', ''), 'rasax', 'domain.yml')) as domain_file:
            _domain = yaml.safe_load(domain_file)

            self.system_actions = _domain.get('actions')
            self.user_intents = _domain.get('intents')
            self.dialog_slots = State(state_config=_domain.get('slots'))
            self.dialogue_history = QueueQuery(_domain.get('pre_turn_number'))

            # print('self.system_actions[{}]: {}'.format(len(self.system_actions), self.system_actions))
            # print('self.user_intents[{}]: {}'.format(len(self.user_intents), self.user_intents))
            print('self.dialog_slots[{}]: {}'.format(len(self.dialog_slots), self.dialog_slots))
            print('self.dialogue_history[{}]: {}'.format(len(self.dialogue_history.query_queue), self.dialogue_history))

        with open(os.path.join(os.getcwd().replace('core/dm', ''), 'rasax', 'data', 'dm', 'recipe_intent_map.yaml'),
                  "r") as recipe_intent_map_file:
            self.recipe_intent_map = yaml.safe_load(recipe_intent_map_file)
            print('self.recipe_intent_map[{}]: {}'.format(len(self.recipe_intent_map), self.recipe_intent_map))

        # loading NLG templates
        response_files = glob.glob(os.path.join(os.getcwd().replace('core/dm', ''), 'rasax', 'data', 'response', '*.yaml'))
        print('files: {}'.format(response_files))
        self.responses = {}
        for file in response_files:
            with open(file, 'r') as yaml_file:
                self.responses.update(yaml.safe_load(yaml_file))
        print('self.responses[{}]: {}'.format(len(self.responses), self.responses))

        # loading DM rules and segments
        with open(os.path.join(os.getcwd().replace('core/dm', ''), 'rasax', 'data', 'dm', 'segments.yaml'),
                  "r") as segments_file:
            _segments = yaml.safe_load(segments_file)
            _segments = {item.get('steps')[0].get('intent'): item.get('steps')[1].get('action') for item in _segments.get('segments')}
            self.rules_regex = {re.compile(k, re.I): v for k, v in _segments.items()}
            # print('self.segments[{}]: {}'.format(len(self.segments), self.segments))
            print('self.rules_regex[{}]: {}'.format(len(self.rules_regex), self.rules_regex))

        with open(os.path.join(os.getcwd().replace('core/dm', ''), 'rasax', 'data', 'dm', 'custom_stories.yaml'),
                  "r") as custom_stories_file:
            _custom_stories = yaml.safe_load(custom_stories_file)
            _custom_stories = {item.get('steps')[0].get('intent'): item.get('steps')[1].get('action') for item in _custom_stories.get('segments')}
            self.rules_regex.update({re.compile(k, re.I): v for k, v in _custom_stories.items()})
            # print('self.segments[{}]: {}'.format(len(self.segments), self.segments))
            print('self.rules_regex[{}]: {}'.format(len(self.rules_regex), self.rules_regex))

        with open(os.path.join(os.getcwd().replace('core/dm', ''), 'rasax', 'data', 'dm', 'rules.yml'),
                  "r") as rules_file:
            _rules = yaml.safe_load(rules_file)
            _rules = {item.get('intent'): item.get('conditions') for item in _rules.get('rules')}
            self.rules_regex.update({re.compile(k, re.I): v for k, v in _rules.items()})
            print('self.rules_regex[{}]: {}'.format(len(self.rules_regex), self.rules_regex))

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
        print('session_id: {}'.format(session_id))
        print('user_sentence: {}'.format(user_sentence))

        if intent_info:
            intent = RasaIntent()
            intent.type = intent_info
            intent.confidence = 1.0
            intent.entities = {}
        else:
            # get NLU results
            r = requests.post('http://localhost:5005/model/parse', data={"text": user_sentence})

            print('r: {}'.format(r))
            if r.status_code == 200:
                intent = self._nlu.process_user_sentence(r.json())

        # if intent.confidence and intent.confidence >= NLU_CONF_THRESHOLD:
        #     _resp, _sys_action, _lock, _robot_command = self.get_response(intent)
        #     self.response.result = _resp
        #     self.response.bot_params['system_action'] = _sys_action
        #     self.response.lock_requested = _lock
        #     if _robot_command:
        #         self.response.bot_params['arbiter_command'] = _robot_command

        # append the latest user input into the dialogue history
        self.dialogue_history.add(speaker="user", turn_data={"user_text": user_sentence, "rasa": intent})
        self._fill_slots(intent.entities)

        recipe_id = self.recipe_intent_map.get(intent.type)
        print('{intent} --> {recipe_id}'.format(intent=intent.type, recipe_id=recipe_id))
        if recipe_id:
            self.dialog_slots.add('meal_type', intent.type)
            self.dialog_slots.add('recipe_ID', recipe_id)
            self.dialog_slots.add('recipe_step_ID', list(self.responses.get('utter_rep').get(recipe_id).keys())[0])

        # Rule-based DM
        system_action = self.search_for_response_action(intent=intent.type)
        self.dialog_slots.add('last_action', system_action)

        # NLG
        if system_action == 'utter_rep':
            recipe_id = self.dialog_slots.get('recipe_ID')
            recipe_responses = self.responses.get(system_action).get(recipe_id)
            _response = recipe_responses.get(self.dialog_slots.get('recipe_step_ID'))
            self.dialog_slots.add('sys_q_type', _response['qType'])
            self.dialog_slots.add('recipe_step_ID', self.dialog_slots.get('recipe_step_ID')+1)

            print('current dialogue state: {}'.format(self.dialog_slots))

        # elif system_action == 'action_search_rec':
        #     # TODO: Linked to the Bert QA model for question answering
        #     pass
        # else:
        #     response_examples = self.system_responses.get(system_action)
        #     _response = random.choice(response_examples)
        #
        # return {"system_action": system_action,
        #         "response": _response,
        #         "stateInfo": self.dialog_slots}

    def search_for_response_action(self, intent: str, **kwargs):
        print('current user intent: {}'.format(intent))
        print('current dialogue state: {}'.format(self.dialog_slots))

        for pattern, action in self.rules_regex.items():
            # print('(2) found searches: {}'.format(re.search(pattern, intent)))
            if re.search(pattern, intent):
                print('matched intent: {}'.format(intent))
                if isinstance(action, str):
                    if "<" in action and ">" in action:
                        key = self.find_between_r(action, "<", ">")
                        action = action.replace("<{}>".format(key), self.dialog_slots.get(key))

                    print('corresponding action : {}'.format(action))
                    return action

                elif isinstance(action, list): # judge the rules by different states
                    for option in action:
                        state = option.get('state')
                        print('state: {}'.format(state))
                        print('matched? : {}'.format(state.items() <= self.dialog_slots.state.items()))
                        act = option.get('action')

                        if state.items() <= self.dialog_slots.state.items():
                            if "<" in act and ">" in act:
                                key = self.find_between_r(act, "<", ">")
                                act = act.replace("<{}>".format(key), self.dialog_slots.get(key))

                            print('corresponding action : {}'.format(act))
                            return act

    def _fill_slots(self, entities: {}):
        if isinstance(entities, dict):
            for key, value in entities.items():
                self.dialog_slots.add(key, value)

    @staticmethod
    def print_response(resp: dict = {}):
        result = resp.get("result")
        print("\n \033[90mALANA >\033[0m \033[96m{}\033[0m\n".format(result))

    @staticmethod
    def find_between_r(origin_text:str, first: str, last: str):
        try:
            start = origin_text.rindex(first) + len(first)
            end = origin_text.rindex(last, start)
            return origin_text[start:end]
        except ValueError:
            return ""

def terminal_test():
    bot = CheifBot()

    this_session = str(uuid.uuid1())
    prompt = "  \033[90mUSER >\033[0m "

    # MAIN LOOP
    while True:
        # Read user input
        user_input = input(prompt)

        # Clear screen if requested by the user
        if user_input == "clear":
            os.system('clear')
            continue

        # Post user input to SPRING-Alana
        print(bot.get_answer(this_session, user_input))


def terminal_test_action():
    bot = CheifBot()

    this_session = str(uuid.uuid1())
    prompt = "  \033[90mUSER >\033[0m "

    # MAIN LOOP
    while True:
        # Read user input
        user_input = input(prompt)

        # Clear screen if requested by the user
        if user_input == "clear":
            os.system('clear')
            continue

        # Post user input to SPRING-Alana
        print(bot.get_answer(this_session, "", intent_info=user_input))


def main():
    pass


if __name__ == "__main__":
    argp = ArgumentParser()
    argp.add_argument('-p', '--port', type=int, default=7115)
    args = argp.parse_args()

    # app.run(host="0.0.0.0", port=args.port, threaded=True)
    # terminal_test()
    terminal_test_action()