import os
import re

import yaml

# recipe_context
recipe_context = {}
with open(os.path.join(os.getcwd().replace('utils', 'core'), 'src', 'data', 'response', 'CookingDomainDataset'),
                  "r") as recipe_file:

    recipe_id = ""
    text = []
    for line in recipe_file.readlines():
        if line.startswith("R") and (not line.startswith("Ro")):
            columns = line.split(' ')

            if recipe_id and columns[0].lower().strip() != recipe_id:
                print("recipe_id {}".format(recipe_id))
                print("text {}".format(len(text)))
                recipe_context[recipe_id.lower()] = " ".join(text).encode('utf8').decode('utf8')

                text.clear()
                recipe_id = columns[0].lower().strip()
            else:
                recipe_id = columns[0].lower().strip()

        elif line.startswith("r"):
            columns = line.split(':')

            if recipe_id and columns[0].lower().strip() != recipe_id:
                print("recipe_id {}".format(recipe_id))
                print("text {}".format(len(text)))
                recipe_context[recipe_id.lower()] = " ".join(text).encode('utf8').decode('utf8')

                text.clear()
                recipe_id = columns[0].lower().strip()
            else:
                recipe_id = columns[0].lower().strip()

        elif line.startswith("Rob"):
            columns = line.split(':')
            text.append(columns[1].strip())

    print("recipe_context: {}".format(len(recipe_context)))
    print("recipe_context: {}".format(recipe_context))


# utensil_explanations
with open(os.path.join(os.getcwd().replace('utils', 'core'), 'src', 'data', 'response', 'utensil_explanations.yaml'),
                  "r") as utensil_explanations_file:
    utensil_explanations = yaml.safe_load(utensil_explanations_file)

    text = []
    utensils = list(utensil_explanations.get("utter_utensils").values())
    for item in utensils:
        text.append(item[0].get('text'))

    print("text ({}): {}".format(len(text), text))
    recipe_context["r"] = " ".join(text)

with open(os.path.join(os.getcwd().replace('utils', 'core'), 'src', 'data', 'response', 'bert_context.yml'),
    'w') as outfile:
    yaml.dump(recipe_context, outfile, default_flow_style=False)


