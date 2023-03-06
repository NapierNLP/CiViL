import copy
import os
import re

import yaml


def find_between_r(origin_text: str, first: str, last: str):
    try:
        start = origin_text.rindex(first) + len(first)
        end = origin_text.rindex(last, start)
        return origin_text[start:end]
    except ValueError:
        return ""


def write_to_yaml(filename: str, data):
    with open(os.path.join(os.getcwd().replace('core/utility', ''), 'rasax', 'data', filename),
              "w") as yaml_file:
        print('yaml_file: {}'.format(os.path.join(os.getcwd().replace('utility', ''), 'rasax', 'data', filename)))
        yaml.dump(data, yaml_file)


class RecipeResponseGenerator:

    def __init__(self):
        with open(os.path.join(os.getcwd().replace('core/utility', ''), 'rasax', 'domain.yml')) as domain_file:
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
                qType = "None"
                if str(recipe_response).endswith("ingredients?"):
                    qType = "confirm_ingredients"
                elif str(recipe_response).endswith("ok?"):
                    qType = "confirm"
                elif str(recipe_response).endswith("okay?"):
                    qType = "confirm"

                response_dict[number_step] = {"text": str(recipe_response), "qType": qType}
                recipe_responses['r{}'.format(rID)] = response_dict

        print('length of recipe responses: {}'.format(len(recipe_responses)))
        print('recipe responses: {}'.format(recipe_responses))

        write_to_yaml('response/recipe_resp.yaml', recipe_responses)


class RecipeIntentMappingGenerator:

    def __init__(self):
        with open(os.path.join(os.getcwd().replace('core/utility', ''), 'rasax', 'data',
                               'data/dm/stories.yml')) as story_file:
            self._stories = yaml.safe_load(story_file)
        self._stories = self._stories.get('stories')
        print('type of _stories: {}'.format(type(self._stories)))

        with open(os.path.join(os.getcwd().replace('core/utility', ''), 'rasax', 'data',
                               'data/dm/custom_stories.yaml')) as segment_file:
            self._segments = yaml.safe_load(segment_file)
        self._segments = self._segments.get('segments')
        print('type of _segments: {}'.format(type(self._segments)))

    def run(self):
        index = 1
        recipe_intent_map = {}

        for item in self._stories:
            steps = item.get('steps')
            for i in range(0, len(steps), 2):
                sys_action = steps[i + 1].get('action')

                if sys_action == 'utter_startrep1':
                    recipe_intent_map[steps[i]['intent']] = 'r1'
                    self._segments.append({"segment": "trigger_{}".format(index),
                                           "steps": [{"intent": steps[i]['intent']},
                                                     {"action": "utter_rep"}]
                                           })
                    index += 1

                elif sys_action.startswith('utter_r'):
                    rID = re.findall(r'\d+', sys_action)[0]
                    alpha_step = sys_action.split(rID)[1].replace('_', '')
                    if alpha_step == 'a':
                        recipe_intent_map[steps[i]['intent']] = 'r{}'.format(rID)

                        self._segments.append({"segment": "trigger_{}".format(index),
                                               "steps": [{"intent": steps[i]['intent']},
                                                         {"action": "utter_rep"}]
                                               })
                        index += 1

        print('length of recipe responses: {}'.format(len(recipe_intent_map)))
        print('recipe responses: {}'.format(recipe_intent_map))

        write_to_yaml(filename='dm/recipe_intent_map.yaml', data=recipe_intent_map)
        write_to_yaml(filename='dm/segments.yaml', data={"version": "2.0", "segments": self._segments})


class IngredientDisplayGenerator:

    def __init__(self):
        with open(os.path.join(os.getcwd().replace('core/utility', ''), 'rasax', 'data', 'original_data',
                               'display_templates.yaml')) as display_file:
            _display = yaml.safe_load(display_file)

        self._action = "display_not_all_ingredients_<meal_type>"
        self.ingredient_display = _display.get(self._action)
        self.ingredient_display_template = self.ingredient_display[0].get('templates')
        print('ingredient_display : {}'.format(self.ingredient_display))
        print('ingredient_display_template : {}'.format(self.ingredient_display_template))

        with open(os.path.join(os.getcwd().replace('core/utility', ''), 'rasax', 'data', 'original_data',
                               'RecipesV6.txt')) as ingredient_file:
            data = ingredient_file.readlines()

        self.recipe_ingredients = {}
        for line in data:
            if line:

                recipe_id = line.split(":")[0].lower()
                meal_type = find_between_r(line, ":", "[").strip().replace(" ", '').lower()
                ingredients = find_between_r(line, "[", "]").replace("\'", '').replace('’', '')
                ingredients = [item.strip() for item in ingredients.split(",")]

                meal_types = []
                if '(' in meal_type:
                    meal_types.append(meal_type.split('(')[0].strip())
                    meal_types.append(find_between_r(meal_type, "(", ")").strip())
                elif '/' in meal_type:
                    meal_types.extend(meal_type.split('/'))
                elif ',' in meal_type:
                    meal_types.extend(meal_type.split(','))
                else:
                    meal_types.append(meal_type)

                for type_name in meal_types:
                    self.recipe_ingredients[type_name] = {"recipe_id": recipe_id, "ingredients": ingredients}

    def run(self):
        displays = {}

        for key, value in self.recipe_ingredients.items():

            ingredients_displays = []
            for ingredient in value.get('ingredients'):
                ingredient = re.sub(u"(\u2018|\u2019)", "", ingredient).replace('\'','')
                ingredient_form = copy.deepcopy(self.ingredient_display_template)
                ingredient_form['title'] = ingredient
                payload = ingredient_form.get('payload')
                ingredient_form['payload'] = payload.replace('<ingredient>', ingredient)

                ingredients_displays.append(ingredient_form)

            full_ingredient_form = copy.deepcopy(self.ingredient_display)
            _buttons = full_ingredient_form[0].get('buttons')
            _buttons.extend(ingredients_displays)
            full_ingredient_form[0]['buttons'] = _buttons

            del full_ingredient_form[0]['templates']

            meal_display_name = copy.copy(self._action)
            meal_display_name = meal_display_name.replace('<meal_type>', key)
            displays[meal_display_name] = full_ingredient_form
            print('full_ingredient_form[{}]: {}'.format(meal_display_name, full_ingredient_form))

        # print('length of recipe responses: {}'.format(len(displays)))
        # print('recipe responses: {}'.format(displays))

        write_to_yaml('response/display_not_all_ingredients.yaml', displays)


if __name__ == "__main__":
    # resp_gen = RecipeResponseGenerator()
    # resp_gen.run()

    # map_gen = RecipeIntentMappingGenerator()
    # map_gen.run()

    display = IngredientDisplayGenerator()
    display.run()
