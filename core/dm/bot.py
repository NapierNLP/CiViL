import os
import random
import uuid
from argparse import ArgumentParser

import requests
import yaml
from flask import request

from core.dm.state import State
from core.nlu.rasa_nlu import RasaNLU
from core.utils.queue_query import QueueQuery


class CheifBot:

    def __init__(self):
        with open(os.path.join(os.getcwd().replace('core.dm', ''), 'rasax', 'domain.yml')) as domain_file:
            _domain = yaml.safe_load(domain_file)

            self.system_actions = _domain.get('actions')
            self.system_responses = _domain.get('responses')
            self.user_intents = _domain.get('intents')
            self.dialog_slots = State(state_config=_domain.get('slots'))
            self.dialogue_history = QueueQuery(_domain.get('pre_turn_number'))

            print('self.system_actions: {}'.format(self.system_actions))
            print('self.user_intents: {}'.format(self.user_intents))
            print('self.dialog_slots: {}'.format(self.dialog_slots))
            print('self.dialogue_history: {}'.format(self.dialogue_history))

        with open(os.path.join(os.getcwd().replace('core.dm', ''), 'dm_configs', 'recipe_resp.yaml'),
                  "r") as recipe_resp_file:
            self.recipe_resp = yaml.safe_load(recipe_resp_file)
            print('self.recipe_resp: {}'.format(self.recipe_resp))

        with open(os.path.join(os.getcwd().replace('core.dm', ''), 'dm_configs', 'recipe_intent_map.yaml'),
                  "r") as recipe_intent_map_file:
            self.recipe_intent_map = yaml.safe_load(recipe_intent_map_file)
            print('self.recipe_intent_map: {}'.format(self.recipe_intent_map))

        self._nlu = RasaNLU()

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

    def get_answer(self, session_id: str, user_sentence: str):
        print('session_id: {}'.format(session_id))
        print('user_sentence: {}'.format(user_sentence))

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
        if recipe_id:
            self.dialog_slots.add('recipe_ID', recipe_id)
            self.dialog_slots.add('recipe_step_ID', list(self.recipe_resp.keys())[0])

        system_action = self.search_for_response_action(intent=intent.type)
        if system_action.startswith('utter_rep'):
            recipe_responses = self.recipe_resp.get(self.dialog_slots.get('recipe_ID'))
            _response = recipe_responses.get(self.dialog_slots.get('recipe_step_ID'))
            self.dialog_slots.add('is_question', _response['isQ'])
        elif system_action == 'action_search_rec':
            # TODO: Linked to the Bert QA model for question answering
            pass
        else:
            _response = self.system_responses.get(system_action)
            _response["text"] = random.choice(_response)["text"]

        return {"system_action": system_action,
                "response": _response["text"],
                "stateInfo": self.dialog_slots}

    def search_for_response_action(self, intent: str, **kwargs):
        # TODO: add a simple n-gram model to search for specific dialogue pairs
        system_action = ""

        return system_action

    def _fill_slots(self, entities: {}):
        if isinstance(entities, dict):
            for key, value in entities.items():
                self.dialog_slots.add(key, value)

    @staticmethod
    def print_response(resp: dict = {}):
        result = resp.get("result")
        print("\n \033[90mALANA >\033[0m \033[96m{}\033[0m\n".format(result))


if __name__ == "__main__":
    argp = ArgumentParser()
    argp.add_argument('-p', '--port', type=int, default=7115)
    args = argp.parse_args()

    # app.run(host="0.0.0.0", port=args.port, threaded=True)
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
