import os
import re

import yaml


def write_to_yaml(filename: str, data):
    with open(os.path.join(os.getcwd().replace('core.utils', ''), 'dm_configs', filename),
              "w") as yaml_file:
        print('yaml_file: {}'.format(os.path.join(os.getcwd().replace('utils', ''), 'dm_configs', filename)))
        yaml.dump(data, yaml_file)


class RecipeResponseGenerator:

    def __init__(self):
        with open(os.path.join(os.getcwd().replace('core.utils', ''), 'rasax', 'domain.yml')) as domain_file:
            _domain = yaml.safe_load(domain_file)

        self.system_response = _domain.get('responses')
        print('type : {}'.format(type(self.system_response)))

    def run(self):
        recipe_responses = {}

        for key, value in self.system_response.items():
            recipe_response = value[0]["text"]

            if key.startswith('utter_rep') or key.startswith('utter_r'):
                rID = re.findall(r'\d+', key)[0]

                alpha_step = key.split(rID)[1].replace('_', '')
                number_step = 0 if alpha_step == "xxx" else (ord(alpha_step) - 96)

                response_dict = recipe_responses.get('r{}'.format(rID), {})
                response_dict[number_step] = {"text": str(recipe_response), "isQ": str(recipe_response).endswith("?")}
                recipe_responses['r{}'.format(rID)] = response_dict

        print('length of recipe responses: {}'.format(len(recipe_responses)))
        print('recipe responses: {}'.format(recipe_responses))

        write_to_yaml('recipe_resp.yaml', recipe_responses)

    @staticmethod
    def write_to_yaml(data):
        with open(os.path.join(os.getcwd().replace('utils', ''), 'dm_configs', 'recipe_resp.yaml'),
                  "w") as recepy_resps_file:
            yaml.dump(data, recepy_resps_file)


class RecipeIntentMappingGenerator:

    def __init__(self):
        with open(os.path.join(os.getcwd().replace('utils', ''), 'rasax', 'data', 'stories.yml')) as story_file:
            self._stories = yaml.safe_load(story_file)
        self._stories = self._stories.get('stories')
        print('type : {}'.format(type(self._stories)))

    def run(self):
        recipe_intent_map = {}

        for item in self._stories:
            steps = item.get('steps')
            for i in range(0, len(steps), 2):
                print('......')
                print(steps[i])
                print(steps[i + 1])

                sys_action = steps[i + 1].get('action')

                if sys_action == 'utter_startrep1':
                    recipe_intent_map[steps[i]['intent']] = 'r1'
                elif sys_action.startswith('utter_r'):
                    rID = re.findall(r'\d+', sys_action)[0]
                    alpha_step = sys_action.split(rID)[1].replace('_', '')
                    if alpha_step == 'a':
                        recipe_intent_map[steps[i]['intent']] = 'r{}'.format(rID)

        print('length of recipe responses: {}'.format(len(recipe_intent_map)))
        print('recipe responses: {}'.format(recipe_intent_map))

        write_to_yaml('recipe_intent_map.yaml', recipe_intent_map)


if __name__ == "__main__":
    resp_gen = RecipeResponseGenerator()
    resp_gen.run()

    map_gen = RecipeIntentMappingGenerator()
    map_gen.run()
