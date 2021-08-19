# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#


class ActionSearchRecs(Action):
    def name(self) -> Text:
        return "action_search_rec"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities= tracker.latest_message['entities']
        print(entities)
        #message='test'
        name=''
        print(entities)
        for e in entities:
            if e['entity'] =='food':
                name = e['value']    
        print(name)
        if name == "plain flour":
            message ="instead you can use; oat flour, bread flour, cake flour or coconut flour, do you have any of these ingredients?"
        if name == "olive oil":
            message ="instead you can use; peanut oil, butter, coconut milk, ghee, walnut oil, sunflower oil, canola oil or vegetable oil, do you have any of these ingredients?"
        if name == "salt":
            message ="instead you can use; mint, rosemary, nutmeg, basil, cardamon, chili, cinnamon or chives, do you have any of these ingredients?"
        if name == "black pepper":
            message ="instead you can use; white pepper, cayenne pepper or papaya seeds, do you have any of these ingredients?"
        if name == "eggs":
            message ="instead you can use; commerical egg substitute or tofu, do you have any of these ingredients?"
        if name == "milk":
            message ="instead you can use; cream, powerdered milk, plain yogurt, nut milk, soy milk, oat milk or rice milk, do you have any of these ingredients?"
        if name == "sausage":
            message ="instead you can use; pork or vegetarian sausages, do you have any of these ingredients?"
        if name == "mustard":
            message ="instead you can use; turmeric, wasabi powder or horseradish powder, do you have any of these ingredients?"
        if name == "beef stock":
            message ="instead you can use; vegetable stock, chicken stock, bouillion stock or red wine, do you have any of these ingredients?"
        if name == "cabbage":
            message ="instead you can use; brussels sprouts, yu choy, kangkong or bok choy, do you have any of these ingredients?"
        if name == "garlic":
            message ="instead you can use; garlic oil, onion, chives or lemon zest, do you have any of these ingredients?"
        if name == "mixed herbs":
            message ="instead you can use; basil, marjoram, min, oregano or parsley, do you have any of these ingredients?"
        if name == "butter":
            message ="instead you can use; olive oil, ghee, greek yogurt, avocado, pumpkin puree or coconut oil, do you have any of these ingredients?"
        if name == "potato":
            message ="instead you can use; cauliflower or cabbage, do you have any of these ingredients?"
        if name == "frozen peas":
            message ="instead you can use; lima beans, green pepper, green onion or broad beans, do you have any of these ingredients?"
        if name == "mushrooms":
            message ="instead you can use; zucchini, eggplant, chickpeas, tofu, onions or cilantro, do you have any of these ingredients?"
        if name == "oat meal":
            message ="instead you can use; amaranth, teff, buckwheat, wheat berries, spelt or quinoa, do you have any of these ingredients?"
        if name == "yeast":
            message ="instead you can use; baking powder. baking soda or sourdough, do you have any of these ingredients?"
        if name == "bacon":
            message ="instead you can use; pork, chicken or turkey bacon, do you have any of these ingredients?"
        if name == "tomatoes":
            message ="instead you can use; olives, red peppers or red capsicum, do you have any of these ingredients?"
        if name == "baked beans":
            message ="instead you can use; peas, shallots, broad beans or chickpeas, do you have any of these ingredients?"
        if name == "paprika":
            message ="instead you can use; catenne pepper, chili powder or chili flakes, do you have any of these ingredients?"
        if name == "feta":
            message ="instead you can use; ricotta, halloumi, goats cheese or queso fresco, do you have any of these ingredients?"
        if name == "parsley":
            message ="instead you can use; chervil, tarragon, chives, oregano, arugula, endive, cilantro or basil, do you have any of these ingredients?"
        if name == "cheddar":
            message ="instead you can use; cantal, edam, mimolette, gouda, emmental or french gruyere, do you have any of these ingredients?"
        if name == "pork fillet":
            message ="instead you can use; pork sirloin, pork tenderloin, chicken, turkey or beef, do you have any of these ingredients?"
        if name == "red peppers":
            message ="instead you can use; poblano peppers, cubanelle, anaheim peppers, pepperoncini, jalapeno, pimiento, zucchini or broccoli, do you have any of these ingredients?"
        if name == "courgette":
            message ="instead you can use; cucumber or zucchini do you have any of these ingredients?"
        if name == "chickpeas":
            message ="instead you can use; green peas, cannellini beans, black beans, lentils, soybeans, mung beans, peanuts or hazelnuts, do you have any of these ingredients?"
        if name == "chicken stock":
            message ="instead you can use; beef stock or vegatable stock, do you have any of these ingredients?"
        if name == "muscovado sugar":
            message ="instead you can use; demerara sugar or brown sugar, do you have any of these ingredients?"
        if name == "balsamic vinegar":
            message ="instead you can use; red wine vinegar, lemon juice or lime juice, do you have any of these ingredients?"
        if name == "paraham":
            message ="instead you can use; smoked ham, pork chops, bacon, prosciutti or cooked ham, do you have any of these ingredients?"
        if name == "passata":
            message ="instead you can use; tomatoes. pasta sauce, tomato paste, ketchup or fresh tomatoes, do you have any of these ingredients?"
        if name == "goats cheese":
            message ="instead you can use; cream cheese, mascarpone cheese, feta cheese or ricotta cheese, do you have any of these ingredients?"
        if name == "basil":
            message ="instead you can use; marajoram, mint, parsley, oregano or thyme, do you have any of these ingredients?"
        if name == "golden syrup":
            message ="instead you can use; honey, cane syrup or brown rice syrup, do you have any of these ingredients?"
        if name == "breadcrumbs":
            message ="instead you can use; oats, chrshed chips, nuts, crackers, pretzels or cereal, do you have any of these ingredients?"
        if name == "lemon":
            message ="instead you can use; lime. orange, white wine, cream of tartar or citric acid, do you have any of these ingredients?"
        if name == "sunflower oil":
            message ="instead you can use; vegetable oil, peanut oil, canola oil, walnut oil, butter, safflower oil, corn oil or grapeseed oil, do you have any of these ingredients?"
        if name == "sweet potato":
            message ="instead you can use; garnet potatoes, jewel potatoes, yukon potatoes, carrots, parsnips, pumpkin or butternut, do you have any of these ingredients?"
        if name == "apple":
            message ="instead you can use; pear, do you have any of these ingredients?"
        if name == "curry powder":
            message ="instead you can use; cumin, coriander, chilli, tumeric or black pepper, do you have any of these ingredients?"
        if name == "tomato puree":
            message ="instead you can use; tomato sauce, pizza sauce, tomato, canned tomatoes or ketchup, do you have any of these ingredients?"
        if name == "mango chutney":
            message ="instead you can use; apricot, mango salsa or marmalade, do you have any of these ingredients?"
        if name == "basmati rice":
            message ="instead you can use; jasmine rice, brown rice, white rice or texmati rice, do you have any of these ingredients?"
        if name == "sour cream":
            message ="instead you can use; greek jogurt, cottage cheese, creme fraiche or buttermilk, do you have any of these ingredients?"
        if name == "coriander":
            message ="instead you can use; cumin, garam masala, curry powder or caraway, do you have any of these ingredients?"
        if name == "braising steak":
            message ="instead you can use; diced beef, sirloin steak or rump steak, do you have any of these ingredients?"
        if name == "brown ale":
            message ="instead you can use; beef stock, chicken stock or vegatable stock, do you have any of these ingredients?"
        if name == "celery":
            message ="instead you can use; fennel, onion, scallions, carrots, shallots, garlic, chives or leeks, do you have any of these ingredients?"
        if name == "bay leaf":
            message ="instead you can use; thyme, oregano or boldo leaf, do you have any of these ingredients?"
        if name == "thyme":
            message ="instead you can use; oregano, marjoram, rosemary, savoury or basil, do you have any of these ingredients?"
        if name == "carrots":
            message ="instead you can use; parsnips, daikon, turnip or celery, do you have any of these ingredients?"
        if name == "onions":
            message ="instead you can use, leeks, chives, garlic, carrors or tomatoes, do you have any of these ingredients?"
        if name == "cornstarch":
            message ="instead you can use, wheat flour, arrowroot, potao starch, rice flour, ground flaxseeds, glucomannan or psyllium husk, do you have any of these ingredients?"
        if name == "pectin":
            message ="instead you can use, citrus peels, cornstarch or geletine, do you have any of these ingredients?"
        if name == "heavy cream":
            message ="instead you can use, milk and butter combined, soy milks and olive oil, milk and cornstarch, greek yogurt, evaporated milk or cottage cheese and milk, do you have any of these ingredients?"
        if name == "vegetable shortening":
            message ="instead you can use butter or magarine, do you have any of these ingredients?"
        if name == "vanilla extract":
            message ="instead you can use, maple syrup, almond extract, bourbon, brandy, rum, do you have any of these ingredients?"            
        if name == "powdered sugar":
            message ="instead you can use, sweetner or cornstarch do you have any of these ingredients?"            
        if name == "maple syrup":
            message ="instead you can use, honey, corn syrup or agave nectar, do you have any of these ingredients?"            
        if name == "sprinkles":
            message ="instead you can use, brown sugar or honey, do you have any of these ingredients?"            
        if name == "cinnamon powder":
            message ="instead you can use, all spice or or nutmeg, do you have any of these ingredients?"            
        if name == "cooking spray":
            message ="instead you can use, butter or olive oil, do you have any of these ingredients?"
        if name == "canned pumpkin":
            message ="instead you can use, mashed sweet potato or butternut squash, do you have any of these ingredients?"            
        if name == "brown sugar":
            message ="instead you can use, white sugar, honey, maple syrup, coconut sugar or muscovado sugar, do you have any of these ingredients?"            
        if name == "pumpkin":
            message ="instead you can use, butternut, honeynut or acorn squash, do you have any of these ingredients?"            
        if name == "cinamon":
            message ="instead you can use, cassia, allspice, clives, nutmeg or cardamom, do you have any of these ingredients?"            
        if name == "nutmeg":
            message ="instead you can use, mace, garam masala, allspice, cinnamon, apple pie spice, giner or cloves, do you have any of these ingredients?"            
        if name == "allspice":
            message ="instead you can use, cinnamon, nutmeg, cloves or applie pie spice, do you have any of these ingredients?"            
        if name == "ground cloves":
            message ="instead you can use, allspice, caradamon, pumpkin pie spice or cinnamon, do you have any of these ingredients?"            
        if name == "ginger":
            message ="instead you can use, cardamom, allspice, cinnamon, nutmeg or mace, do you have any of these ingredients?"            
        if name == "berbere seasoning":
            message ="instead you can use, cayenne pepper or ras el hanout, do you have any of these ingredients?"            
        if name == "tomato paste":
            message ="instead you can use, soy sauce, olive tapenade, canned tomatoes or tomato ketchup, do you have any of these ingredients?"            
        if name == "red lentils":
            message ="instead you can use, yellow lentils or green lentils, do you have any of these ingredients?"            
        if name == "'strawberries":
            message ="instead you can use, rasberries, red grapes or blueberries, do you have any of these ingredients?"            
        if name == "pineapple":
            message ="instead you can use, apple, orange, kiwi or grape, do you have any of these ingredients?"            
        if name == "red onion":
            message ="instead you can use, yellow onions, leeks, shallots or onion juice, poweder or flakes, do you have any of these ingredients?"            
        if name == "sweet red pepper":
            message ="instead you can use, , do you have any of these ingredients?"            
        if name == "cilantro":
            message ="instead you can use parsley, mint, basil, chives, green onions, dill or carrot greens, do you have any of these ingredients?"            
        if name == "key lime juice":
            message ="instead you can use, lemon juice or lemon extract, do you have any of these ingredients?"            
        if name == "unsalted butter":
            message ="instead you can use, maragarine, vegetable shortening, coconut oil or salted butter, do you have any of these ingredients?"            
        if name == "egg yolk":
            message ="instead you can use, apple sauce, mashed banana, ground flaxseeds, chia seeds, commerial egg replacer, silken tofu or buttermilk, do you have any of these ingredients?"            
        if name == "'pear":
            message ="instead you can use, apples, asain pears, quinces, figs or pepinos, do you have any of these ingredients?"            
        if name == "lemon juice":
            message ="instead you can use, lime juice, orange juice, vinegar, citric acid, white wine, lemon extract or cream or tartar, do you have any of these ingredients?"            
        if name == "black beans":
            message ="instead you can use, chickpeas, kidney beans, lentils, cauliflower or nuts, do you have any of these ingredients?"
        if name == "pork ribs":
            message ="instead you can use, pork chops, or pork belly, do you have any of these ingredients?"            
        if name == "smokey bacon":
            message ="instead you can use, liquid smoke, smoked paprila, veggie bacon, dark beer or blackstrap moasses, do you have any of these ingredients?"            
        if name == "pork belly":
            message ="instead you can use, pork chops or pork ribs, do you have any of these ingredients?"            
        if name == "dried chili":
            message ="instead you can use, serrano pepper, cayenne pepper, pequin chili or jalapeno, do you have any of these ingredients?"            
        if name == "cumin":
            message ="instead you can use, ground coriander, caraway seeds, chili powder, taco seasoning, curry powder or garam masala, do you have any of these ingredients?"            
        if name == "oregano":
            message ="instead you can use, mint, parsley or poultry seasoning, do you have any of these ingredients?"            
        if name == "beans":
            message ="instead you can use, tofu, sourgram, cauliflowder florets, tempeh, quinoa, peas or eggplant, do you have any of these ingredients?"            
        if name == "long grain rice":
            message ="instead you can use, white rice, brown rice or egg friend rice, do you have any of these ingredients?"            
        if name == "star anise":
            message ="instead you can use, allspice, chinese five spice powder or chili powder, do you have any of these ingredients?"        
        if name == "spring onions":
            message ="instead you can use, challots, green onions, red onions or celery , do you have any of these ingredients?"            
        if name == "miso paste":
            message ="instead you can use, soy sauce, salt, tahini or vegetable stock, do you have any of these ingredients?"            
        if name == "mirin":
            message ="instead you can use, dry sherry or sweet masala wine, do you have any of these ingredients?"            
        if name == "soy sauce":
            message ="instead you can use, tamari, worcestershire sauce, coconut aminos, miso paste or maggi seasoning, do you have any of these ingredients?"            
        if name == "shiitake mushrooms":
            message ="instead you can use, portobello mushrooms, crimini mushrooms or porcini mushrooms, do you have any of these ingredients?"            
        if name == "baby spinach":
            message ="instead you can use, rocket, spinach, watercress or beet greens, do you have any of these ingredients?"            
        if name == "white pepper":
            message ="instead you can use, ground giner, ground mustard or pink peppercorns, do you have any of these ingredients?"            
        if name == "furikake":
            message ="instead you can use, crumbled nori seaweed, sesame seeds or togarashi, do you have any of these ingredients?"            
        if name == "pasta":
            message ="instead you can use, spaghetti, eggplant lasagna, cabbage noodles, sprouts or onion noodles, do you have any of these ingredients?"            
        if name == "curry leaves":
            message ="instead you can use, lime zest, bay leves, basil leaves, lemon zest or daun salam leaves, do you have any of these ingredients?"            
        if name == "asafoetida":
            message ="instead you can use, garlic powder, garlic cloves or  , do you have any of these ingredients?"            
        if name == "peanuts":
            message ="instead you can use, beans, pretzels, seeds, tahini, sunflower seeds or almonds, do you have any of these ingredients?"    
        if name == "almonds":
            message ="instead you can use, breadcrumbs, ground rice, semolina or polenta, do you have any of these ingredients?"
        if name == "sesame seeds":
            message ="instead you can use, poppy seeds or hemp seeds, do you have any of these ingredients?"            
        if name == "golden raisins":
            message ="instead you can use, pitted dates, prines or dried cranberries , do you have any of these ingredients?"            
        if name == "cashew nuts":
            message ="instead you can use, pine nuts, almonds, walknuts, hazelnuts or sunflower seeds, do you have any of these ingredients?"            
        if name == "green chili":
            message ="instead you can use, banana pepper, anaheim pepper, poblano pepper, jalapeno, serrano or chilli powder, do you have any of these ingredients?"            
        if name == "rib roast":
            message ="instead you can use, prok belly or pork chops, do you have any of these ingredients?"            
        if name == "kosher salt":
            message ="instead you can use, sea saly, brine or coarse himalayan pink salt, do you have any of these ingredients?"            
        if name == "worcestershire sauce":
            message ="instead you can use, soy sauce, miso paste, soy sauce and ketcup r soy cause and apple sauce, do you have any of these ingredients?"            
        if name == "liquid smoke":
            message ="instead you can use, smoked paprika, smoke tea or chipotle powder, do you have any of these ingredients?"            
        if name == "beef broth":
            message ="instead you can use, vegetable broth, bouillon cubes, soy sauce or mushroom broth, do you have any of these ingredients?"            
        if name == "mustard powder":
            message ="instead you can use, tumeri powder, wasabi powder or mustard seed, do you have any of these ingredients?"            
        if name == "coriander powder":
            message ="instead you can use, cumin, garam masala, curry powder or caraway, do you have any of these ingredients?"            
        if name == "onion powder":
            message ="instead you can use, onion flakes, minced onion, fresh onion or garlc powder, do you have any of these ingredients?"            
        if name == "bay leaves":
            message ="instead you can use, dried thyme or oregano, do you have any of these ingredients?"            
        if name == "dried thyme":
            message ="instead you can use, oregano, marjoram, rosemary, savoury,or basil, do you have any of these ingredients?"            
        if name == "rosemary":
            message ="instead you can use, thyme, tarragon or savory, do you have any of these ingredients?"            
        if name == "yellow pepper":
            message ="instead you can use, red pepper, green pepper, orange bell peppers, do you have any of these ingredients?"            
        if name == "chorizo":
            message ="instead you can use, smoked paprika or bacon rind, do you have any of these ingredients?"            
        if name == "cannellini beans":
            message ="instead you can use, red kideny beans, great northen beans or navy beans, do you have any of these ingredients?"
        if name == "italian seasoniong":
            message ="instead you can use, basil, marjoram, oregano, rosemary or thyme, do you have any of these ingredients?"
        if name == "garlic salt":
            message ="instead you can use, garlic powder, kosher salt, garlic cloves or garlic powder and salt, do you have any of these ingredients?"            
        if name == "pepe pasta":
            message ="instead you can use, arugula or kale, do you have any of these ingredients?"            
        if name == "parmesan cheese":
            message ="instead you can use, gran padano or american grana, dry jack or pecorino, do you have any of these ingredients?"
        if name == "spinach":
            message ="instead you can use, argula or kale, do you have any of these ingredients?"            
        if name == "ricotta":
            message ="instead you can use, goats cheese, cottage cheese, sour cream, cream cheese or queso fresco, do you have any of these ingredients?"            
        if name == "boiled ham":
            message ="instead you can use, candian bacon or gammon, do you have any of these ingredients?"            
        if name == "spice rub":
            message ="instead you can use, BBQ seasoning, italian seasoning or allspiace, do you have any of these ingredients?"            
        if name == "cayenne pepper":
            message ="instead you can use, chili powder, paprika or red chili flakes, do you have any of these ingredients?"            
        if name == "peanut sauce":
            message ="instead you can use, almond butter or cashew butter, do you have any of these ingredients?"            
        if name == "jalapeno pepper":
            message ="instead you can use, serrano pepper, fresno pepper, anaheim pepper pr pblano pepper, do you have any of these ingredients?"            
        if name == "chicken broth":
            message ="instead you can use, beef stock, vegetable stock or lamb stock, do you have any of these ingredients?"            
        if name == "peanut butter":
            message ="instead you can use, sunflower seed butter, cookie butter, or coconut butter, do you have any of these ingredients?"            
        if name == "coconut milk":
            message ="instead you can use, soy milk, almond milk, oat milk or rice milk, do you have any of these ingredients?"            
        if name == "figs":
            message ="instead you can use, raisins, prines or dried apriocots, do you have any of these ingredients?"            
        if name == "honey":
            message ="instead you can use, date paste, agave nectar, maple syrup or brown rice sugar, do you have any of these ingredients?"            
        if name == "apple vinegar":
            message ="instead you can use, rice vinegar, red wine vinegar, lemon juice or champagne vinegar, do you have any of these ingredients?"            
        if name == "deli ham":
            message ="instead you can use, roasted chicken or canned salmon, do you have any of these ingredients?"            
        if name == "swiss cheese":
            message ="instead you can use, fontina cheese, cheddar cheese or mozzerella cheese, do you have any of these ingredients?"            
        if name == "milk yoghurt":
            message ="instead you can use, buttermilk, or sour cream, do you have any of these ingredients?"            
        if name == "confectioners sugar":
            message ="instead you can use, granulated sugar or brown sugar, do you have any of these ingredients?"            
        if name == "low fat greek yogurt":
            message ="instead you can use, buttermilk, tofu, cottage cheese or sour cream, do you have any of these ingredients?"            
        if name == "butternut squash":
            message ="instead you can use, buttercup squash, pupkin, carrots or acorn squash, do you have any of these ingredients?"            
        if name == "chili flakes":
            message ="instead you can use, cayenne pepper, black cardamon or fennel seeds, do you have any of these ingredients?"            
        if name == "broccoli":
            message ="instead you can use, kale, leafy greens, asparagus, or baby spinach leaves, do you have any of these ingredients?"            
        if name == "gorgonzola":
            message ="instead you can use, roquefort, stilon, danish blue or creamy blue cheese, do you have any of these ingredients?"            
        if name == "leek":
            message ="instead you can use, green onions, red onions, challots or celery, do you have any of these ingredients?"            
        if name == "fennel":
            message ="instead you can use, anise seeds, cumin seeds, caraway seeds or dill, do you have any of these ingredients?"            
        if name == "acord squash":
            message ="instead you can use, butternut squash or pumpkin squash, do you have any of these ingredients?"            
        if name == "sea slat flakes":
            message ="instead you can use, table salt or maldon salt, do you have any of these ingredients?"            
        if name == "tarragon":
            message ="instead you can use, dill, basil or marjoram, do you have any of these ingredients?"            
        if name == "hazelnuts":
            message ="instead you can use, walnuts, macadamia nuts or almonds, do you have any of these ingredients?"            
        if name == "mature cheddar cheese":
            message ="instead you can use, gouda or parmesan cheese, do you have any of these ingredients?"            
        if name == "tilapia":
            message ="instead you can use, catfish, striped bass, red snapper or rainbow trout, do you have any of these ingredients?"            
        if name == "panko breadcrumbs":
            message ="instead you can use, regular breadcrumbs, cracker crumbs, matzo meal, crushed cornflakes or dry stuffing mix, do you have any of these ingredients?"            
        if name == "parmesan cheese":
            message ="instead you can use, grana padano, piave cheese or pecorino, do you have any of these ingredients?"            
        if name == "paprika":
            message ="instead you can use, cayenne pepper, chili powder, chili flakes or red chili, do you have any of these ingredients?"            
        if name == "cream cheese":
            message ="instead you can use, cottage cheese, mascarphone, tofu, ricotta cheese or sour cream, do you have any of these ingredients?"            
        if name == "hot sauce":
            message ="instead you can use, chili powder, chili flakes, harissa, or curry paste, do you have any of these ingredients?"            
        if name == "tortilla wraps":
            message ="instead you can use, lettice wraps or pita bread, do you have any of these ingredients?"            
        if name == "marrow":
            message ="instead you can use, courgette or squash, do you have any of these ingredients?"            
        if name == "semolina":
            message ="instead you can use, flour, bread flour or whole wheat flour, do you have any of these ingredients?"            
        if name == "northen beans":
            message ="instead you can use, navy beans, cannellini beans or lima beans, do you have any of these ingredients?"            
        if name == "dry mustard powder":
            message ="instead you can use, dijon mustard or tumeric, do you have any of these ingredients?"                        
        if name == "ansjovis":
            message ="instead you can use, shrimp, shrimp paste, capers or asian fish sauce, do you have any of these ingredients?"            
        if name == "shallots":
            message ="instead you can use, sweet onions, leeks, garlic scapes, red onions or green onions, do you have any of these ingredients?"            
        if name == "tumeric":
            message ="instead you can use, ginger powder, cumin, saffron or annatto powder, do you have any of these ingredients?"            
        if name == "galangal":
            message ="instead you can use, fresh ginger or ginger powder, do you have any of these ingredients?"            
        if name == "lemongrass":
            message ="instead you can use, lemon grass, lemon juice, lime zest or lemon balm, do you have any of these ingredients?"            
        if name == "dry yeast":
            message ="instead you can use, equal parts lemon juice and baking soda , do you have any of these ingredients?"            
        if name == "almonds":
            message ="instead you can use, breadcrumbs, ground rice and polenta, do you have any of these ingredients?"            
        if name == "aniseed":
            message ="instead you can use, star anise, fennel seed, teaspoon caraway seed or chopped tarragon, do you have any of these ingredients?"            
        if name == "asparagus":
            message ="instead you can use, broccoli, celery, green beans or lettuce, do you have any of these ingredients?"            
        if name == "jicama":
            message ="instead you can use, daikon radish or jerusalem artichokes, do you have any of these ingredients?"            
        if name == "red cabbage":
            message ="instead you can use, white cabbage or napa cabbage, do you have any of these ingredients?"            
        if name == "purple cabbage":
            message ="instead you can use, napa cabbage, breussels sprouts, bok choy and celery, do you have any of these ingredients?"            
        if name == "lettuce":
            message ="instead you can use, spinach or parsley, do you have any of these ingredients?"            
        if name == "blueberries":
            message ="instead you can use, acai berries, blackberries, huckleberries, raspberries or currents, do you have any of these ingredients?"            
        if name == "mint":
            message ="instead you can use, peppermint or parsely, do you have any of these ingredients?"            
        if name == "mine confit zest":
            message ="instead you can use, lemon zest or lime zest, do you have any of these ingredients?"            
        if name == "chinese oyster sauce":
            message ="instead you can use, soy sauce, hoisin sauce or fish sauce, do you have any of these ingredients?"            
        if name == "apple cider vinegar":
            message ="instead you can use, red wine, white wine or sherry vinegar, do you have any of these ingredients?"            
        if name == "saffron":
            message ="instead you can use, turmeric or cumin, do you have any of these ingredients?"            
        if name == "mussels":
            message ="instead you can use, shrimp, prawns or clam, do you have any of these ingredients?"            
        if name == "prawns":
            message ="instead you can use, mussels, clam or shrimp, do you have any of these ingredients?"            
        if name == "monkfish":
            message ="instead you can use, snapper, sea bass, halibut or sea scallops, do you have any of these ingredients?"            
        if name == "squid":
            message ="instead you can use, prawns oe firm white fish, do you have any of these ingredients?"            
        if name == "risotto rice":
            message ="instead you can use, brown rice, sushi rice, basmati rice or quinoa, do you have any of these ingredients?"
        if name == "dry white wine":
            message ="instead you can use, apple cider vinegar, chicken broth, white grape juice or ginger ale, do you have any of these ingredients?"            
        if name == "chicken legs":
            message ="instead you can use, chicke drumsticks or chicken thighs, do you have any of these ingredients?"            
        if name == "cherry tomatoes":
            message ="instead you can use, olives, red pepper or canned tomatoes, do you have any of these ingredients?"            
        if name == "capers":
            message ="instead you can use, green olives, anchovies or pickles, do you have any of these ingredients?"            
        if name == "djion mustard":
            message ="instead you can use, yellow mustard, honey mustard, wasabi or mayonnaise, do you have any of these ingredients?"            
        if name == "beef bouillon":
            message ="instead you can use, chicken broth or vegetable stock, do you have any of these ingredients?"            
        if name == "celery seeds":
            message ="instead you can use, flat leaf parsley or dill seed, do you have any of these ingredients?"            
        if name == "chickpeas":
            message ="instead you can use, green peas, lentils, soybeans, mung beans or peanuts, do you have any of these ingredients?"            
        if name == "lamb stock":
            message ="instead you can use, chicken stock or vegetable stock, do you have any of these ingredients?"            
        if name == "canned tomatoes":
            message ="instead you can use, fresh tomatoes, sun dried tomatoes or red peppers, do you have any of these ingredients?"
        if name == "caramilk chocolate":
            message ="instead you can use, white chocolate, milk chocolate or dark chocolate, do you have any of these ingredients?"
        if name == "coca":
            message = "instead you can use, jackfruit seeds, do you have any of these ingredients?"
        if name == "garam masala":
            message = "instead you can use, curry powder, allspice powder or chaat powder, do you have any of these ingredients?"
        if name == "arbol chili powder":
            message = "instead you can use, cayenne powder or generic chili powder, do you have any of these ingredients?"
        if name == "ghee":
            message = "instead you can use, olive oil, coconut oil, canola oil, soybean oil, sunflower oil or butter, do you have any of these ingredients?"
        if name == "turkey tenderloin":
            message = "instead you can use, turkey breast fillets or turkey bacon, do you have any of these ingredients?"
        if name == "Egg noodles":
            message = "instead you can use, fettucine, ribbon pasta, linguine or brown / white rice, do you have any of these ingredients?"
        if name == "Chicken liver":
            message = "instead you can use, duck liver, turkey liver or goose liver, do you have any of these ingredients?"
        if name == "Chicken gizzard":
            message = "instead you can use, turkey gizzard or goose gizzard, do you have any of these ingredients?"
        if name == "Bell pepper":
            message = "instead you can use, anahiem peppers, Jalapenos, pimiento or zucchini, do you have any of these ingredients?"
        if name == "Small head wombok":
            message = "instead you can use other cabbages such as red, white or napa cabbage, do you have any of these ingredients?"
        if name == "Oyster sauce":
            message = "instead you can use, soy sauce, sweet soy sauce, hoisin sauce or plumb sauce, do you have any of these ingredients?"
        if name == "Calamansi":
            message = "instead you can use lemon and lime juices, do you have any of these ingredients?"
        if name == "Dry white wine":
            message = "instead you can use white wine vinegar, do you have any of these ingredients?"
        if name == "Orange Roughy":
            message = "instead you can use perch, blackfish, flounder, sole, haddock or red snapper, do you have any of these ingredients?"
        if name == "Limes":
            message = "instead you can use orange, lemon or zest, do you have any of these ingredients?"
        if name == "Serrano peppers":
            message = "instead you can use jalapeno, habanero, cayenne, guero or poblano pepper, do you have any of these ingredients?"
        if name == "Avocado":
            message = "instead you can use chai seeds or tree nuts, do you have any of these ingredients?"
        if name == "Honey":
            message = "instead you can use rice maly syrup, brown rice syrup, molasses, coconut syrup, maple syrup or golden syrup, do you have any of these ingredients?"
        if name == "Roma tomato":
            message = "instead you can use polish paste, plum or oxheart tomatoes, do you have any of these ingredients?"
        if name == "Yellow rice":
            message = "instead you can use white rice, brown rice, long grain rice or egg fried rice, do you have any of these ingredients?"
        if name == "Bisquick":
            message = "instead you can use 1 cup of all purpose flow mixed with 1 and a half teaspoons of baking powder, half a teaspoon or salt and one tablespoon of vegetable oil, do you have any of these ingredients?"
        if name == "Smoked paprika":
            message = "instead you can use hungarian paprika, sweer paprika, chipolatle chili or liquid smoke, do you have any of these ingredients?"
        if name == "split pig's feet":
            message ="instead you can use, ham hocks or ham shanks, do you have any of these ingredients?"    
        if name == "chicken bouillon cube":
            message ="instead you can use,chicken broth, dry white wine, poultry seasoning with water, do you have any of these ingredients?"
        if name == "butternut squash and beet noodles":
            message ="instead you can use, cucumber noodles,carrot noodles, raddish noodles, summer squash noodles, spiralized kohlrabi, sweet potato noodles or zucchini noodles, do you have any of these ingredients?"
        if name == "bosc pears":
            message ="instead you can use, asian pears, apples, quinces or figs, do you have any of these ingredients?"
        if name == "pecans":
            message ="instead you can use, hazelnuts, pistachios, macadamia nuts, brazil nuts, walnuts or pecan oil, do you have any of these ingredients?"
        if name == "canola oil":
            message ="instead you can use, grapeseed oil, vegetable oil or sunflower oil , do you have any of these ingredients?"
        if name == "vodka":
            message ="instead you can use, water, apple cide vinegar or white grae juice mixed with lime juice; aquavit, tequila or white rum, do you have any of these ingredients?"
        if name == "cane sugar":
            message ="instead you can use, honey, maple syrup, applesauce, caster sugar, brown sugar, raw sugar, powdered sugar, molasses or corn syrup, do you have any of these ingredients?"
        if name == "apple cider vinegar":
            message ="instead you can use, red or white wine vinegar, rice vinegar, sherry vinegar, champagne vinegar or lemon juice, do you have any of these ingredients?"
        if name == "jasmine rice":
            message ="instead you can use, basmati rice or long-grain rice, do you have any of these ingredients?"
        if name == "ground cinnamon":
            message ="instead you can use, nutmeg, cloves, allspice or apple pie spice, do you have any of these ingredients?"
        if name == "canned plum tomatoes":
            message ="instead you can use, regular tomatoes and tomato paste, fresh tomatoes and canned whole tomatoes or sun-dried tomatoe, do you have any of these ingredients?"
        if name == "can of tomato sauce":
            message ="instead you can use, ketchup, tomato soup or tomato paste, do you have any of these ingredients?"
        if name == "can of tomato sauce":
            message ="instead you can use, asian pears, apples, quinces or figs, do you have any of these ingredients?"
        if name == "coconut cream":
            message ="instead you can use, coconut milk, whipping cream, nut butter, tahini, greek yogurt or creamy tomato sauce, do you have any of these ingredients?"
        if name == "sugar":
            message ="instead you can use, honey, maple syrup, applesauce, molasses, cane sugar or brown sugar, do you have any of these ingredients?"
        if name == "all-purpose flour":
            message ="instead you can use, chickpea flour, rice flour, almond flour, buckwheat flour or a mixture of bread flour with cake flour, do you have any of these ingredients?"
        if name == "baking powder":
            message ="instead you can use, buttermilk, plain yogurt, molasses, cream of tartar, sour milk, vinegar, lemon juice, baking soda, self-rising flour or whipped egg whites, do you have any of these ingredients?"
        if name == "baking soda":
            message ="instead you can use, baking powder, potassium bicarbonate and salt, self-rising flour or baker's ammonia, do you have any of these ingredients?"
        if name == "grated nutmeg":
            message ="instead you can use, ground nutmeg, mace, garam masala, allspice, cinamon, pumpkin pie spice, appke pie spice, ginger or cloves, do you have any of these ingredients?"
        if name == "ginger powder":
            message ="instead you can use, ground allspice, ground cinnamon, ground mace or ground nutmeg, do you have any of these ingredients?"
        if name == "granulated sugar":
            message ="instead you can use, honey, maple syrup, applesauce, caster sugar, brown sugar, powdered sugar, molasses or corn syrup, do you have any of these ingredients?"
        if name == "packed light brown sugar":
            message ="instead you can use,white sugar and molasses, honey, white sugar and maple syrup, coconut sugar, maple syryp, agave nectar or plain white sugar, do you have any of these ingredients?"
        if name == "canned unsweetened pumpkin puree":
            message ="instead you can use, frozen butternut squash, sweet potatoes, roasted acorn squash or fresh pumpkin puree do you have any of these ingredients?"
        if name == "cranberries":
            message ="instead you can use, apricots, apples, cherries, raspberries blueberries or currants, do you have any of these ingredients?"
        if name == "maple syrup":
            message ="instead you can use, honey, brown sugar, white sugar, molasses orcorn syrup, do you have any of these ingredients?"
        if name == "turkey neck":
            message ="instead you can use chicken quarters, do you have any of these ingredients?"
        if name == "celery sticks":
            message ="instead you can use; fennel, onion, scallions, carrots, shallots, garlic, chives or leeks, do you have any of these ingredients?"
        if name == "tamari":
            message ="instead you can use; soy sauce, fish sauce, salt, miso paste, teriyaki sauce or maggi seasoning, do you have any of these ingredients?"
        if name == "walnuts":
            message ="instead you can use; almonds, cashews, filberst, brazil nuts or macadamia nuts, do you have any of these ingredients?"
        if name == "whole milk":
            message ="instead you can use; semi-skimmed milk, double cream, yogurt, sour cream, soy milk or coconut milk, do you have any of these ingredients?"
        if name == "red currant":
            message ="instead you can use; raisins, dried dates, dried prunes, dried cherries, cranberries or jujube, do you have any of these ingredients?"
        if name == "raspberry jelly":
            message ="instead you can use; strawberry jelly, cranberry jelly or red currants , do you have any of these ingredients?"
        if name == "bittersweet chocolate":
            message ="instead you can use; unsweetened baking chocolate and sugar or semisweet chocolate with cocoa powder, do you have any of these ingredients?"
        if name == "unsweetened cocoa powder":
            message ="instead you can use; melted unsweetened baking chocolate, dutch-processed cocoa or carob powder, do you have any of these ingredients?"
        if name == "buttermilk":
            message ="instead you can use; milk and vinegar, milk and lemon juice, milk and cream of tartar, sour cream and water, plain yogurt and water or plain kefir, do you have any of these ingredients?"
        if name == "semisweet chocolate chips":
            message ="instead you can use; bittersweet baking chocolate, unsweetened cocoa powder, or unsweetened baking chocolate do you have any of these ingredients?"
        if name == "cream of tartar":
            message ="instead you can use; lemon juice, white vinegar, baking powder, buttermilk or yogurt, do you have any of these ingredients?"
        if name == "egg whites":
            message ="instead you can use; aquafaba, ground flax seeds and water, agar powder and water or chia seeds and water, do you have any of these ingredients?"
        if name == "dark brown sugar":
            message ="instead you can use,white sugar and molasses, honey, white sugar and maple syrup, coconut sugar, maple syryp, agave nectar or plain white sugar, do you have any of these ingredients?"
        if name == "vegetable oil":
            message ="instead you can use, canola oil, sunflower oil, peanut oil or grapeseed oil, do you have any of these ingredients?"
        if name == "ground nutmeg":
            message ="instead you can use, grated nutmeg, mace, garam masala, allspice, cinamon, pumpkin pie spice, appke pie spice, ginger or cloves, do you have any of these ingredients?"
        if name == "old-fashioned rolled-oats":
            message ="instead you can use, qionoa flakes, stell-cut oats or instant oats, do you have any of these ingredients?"
        if name == "raisins":
            message ="instead you can use, dried currants, dried cherries, dried cranberries, dried prunes, dried sates, dried apricot or dried pineapple, do you have any of these ingredients?"
        if name == "vanilla":
            message ="instead you can use, maple syrup, almond extract, bourbon, instant coffee, expresso powder or citrus zest, do you have any of these ingredients?"
        if name == "lemon zest":
            message ="instead you can use, lemon extract, lemon juice, another citrus zest or lemon peel, do you have any of these ingredients?"
        if name == "parsnips":
            message ="instead you can use, turnips, celery root, carrots, salsify, sweet potatoes or parsley root, do you have any of these ingredients?"
        if name == "thyme leaves":
            message ="instead you can use, oregano, majoram, basil, savory, poultry seasoning, italian seasoning, za'taar or herbes de provence, do you have any of these ingredients?"
        if name == "white bread":
            message ="instead you can use, oopsie bread, ezekiel bread, corn tortillas or rye bread, do you have any of these ingredients?"
        if name == "canned cannellini beans":
            message ="instead you can use, red kidney beans, great northern beans, navy beans, baby lima beans, butter beans, garbanzo beans, borlotti beans or black beans, do you have any of these ingredients?"
        if name == "baby lima beans":
            message ="instead you can use, fava beans, red kidney beans or white kidney beans, do you have any of these ingredients?"
        if name == "large egg":
            message ="instead you can use, any other size of egg, do you have any of these ingredients?"
        if name == "powdered gelatin":
            message ="instead you can use, agar agar powder, pectin powder, carrageean or guar gum, do you have any of these ingredients?"
        if name == "ground beef":
            message ="instead you can use, mushrooms, ground poultry, textured vegetable protein, lentils, tempeh, tofu, seitan or beans, do you have any of these ingredients?"
        if name == "prociutto":
            message ="instead you can use, ham, bacon, pancetta, capiola or spanish serrano ham, do you have any of these ingredients?"
        if name == "parsley leaves":
            message ="instead you can use, cilantro, celery leaves, carrot greens, chives or chervil, do you have any of these ingredients?"
        if name == "crsuhed tomatoes":
            message ="instead you can use, fresh tomatoes, diced tomatoes, tomato paste, tomato puree, whole peeled tomatoes or pasta sauce, do you have any of these ingredients?"
        if name == "cooking wine":
            message ="instead you can use, white grape juice and apple juice, apple cider, cranberry juice, ginger ale, white wine vinegar, red wine vingear, lemon juice, chicken broth or vegetable broth, do you have any of these ingredients?"
        if name == "spaghetti":
            message ="instead you can use, vermicelli, angel hair pasta or rice stick noodles, do you have any of these ingredients?"
        if name == "red potatoes":
            message ="instead you can use, yukon gold potatoes, white potatoes, yellow potatoes or russet potato, do you have any of these ingredients?"
        if name == "chicken breasts":
            message ="instead you can use, chicken cacciatora, shrimp aragonate, grilled scallops, seared duck breasts or roast trukey breasts, do you have any of these ingredients?"
        if name == "marsala red wine":
            message ="instead you can use, madeira, fortified wine, dru sherry, sherry wine and sweet vermouth, amontillado wine and pedro ximenez, port, white grape juice with brandy, non-fortified wine, pinot noir or dry white wine, do you have any of these ingredients?"
        if name == "unflavoured gelatin":
            message ="instead you can use, kudzu, pectin and sugar, arrowroot or agar agar, do you have any of these ingredients?"
        if name == "porcini mushrooms":
            message ="instead you can use, shiitake mushrooms, dried reconstituted shiitake mushrooms, mixed mushrooms or fresh button mushrooms, do you have any of these ingredients?"
        if name == "cremini mushrooms":
            message ="instead you can use, white button mushrooms, portobello mushrooms, shiitake mushrooms or aubergine, do you have any of these ingredients?"
        if name == "white mushrooms":
            message ="instead you can use, courgette, sun dried toamtoes, aubergine, garbanzo beans, russel potatoes, tofu or onions, do you have any of these ingredients?"
        if name == "pasta sauce":
            message ="instead you can use, toamato paste, ketchup or tomato soup do you have any of these ingredients?"
        if name == "lasagna noodles":
            message ="instead you can use, macaroni with tomato sauce or flat-sliced courgette, do you have any of these ingredients?"
        if name == "mozzarella cheese":
            message ="instead you can use, white cheddar cheese, provolone, gouda, parmesan, ricotta or feta cheese, do you have any of these ingredients?"
        if name == "baking spray":
            message ="instead you can use, butter or lard, do you have any of these ingredients?"
        if name == "gruyere cheese":
            message ="instead you can use, comte cheese, beaufort cheese, jalsberg cheese, emmentaler cheese, fontina and parmesan cheese, maasdam and edam cheese or raclette cheese, do you have any of these ingredients?"
        if name == "cherries":
            message ="instead you can use, canned cherries, fresh plums, fresh apricots or fresh nectarines, do you have any of these ingredients?"
        if name == "yellow onions":
            message ="instead you can use, red onion or white onion, ricotta or feta cheese, do you have any of these ingredients?"
        if name == "mixed mushrooms":
            message ="instead you can use, courgette, sun dried toamtoes, aubergine, garbanzo beans, russel potatoes, tofu or onions, do you have any of these ingredients?"
        if name == "dried white beans":
            message ="instead you can use, dried cannellini beans, dried navy beans, dried red beans or dried pinto beans, do you have any of these ingredients?"
        if name == "canned peeled tomateos":
            message ="instead you can use, crushed tomatoes, diced tomatoes or fresh tomatoes do you have any of these ingredients?"
        if name == "swiss chard":
            message ="instead you can use, mature spinach, mustard greens, kale or large bok choy, do you have any of these ingredients?"
        if name == "kale":
            message ="instead you can use, collard greens, english spinach, baby spinach, swiss chard, mustard greens, chinese broccoli, broccoli raab or turnip, do you have any of these ingredients?"
        if name == "almond flour":
            message ="instead you can use, wheat flour, all-purpose flour, cashew flour, macadamia flour, sunflower seed flour, oat flour or a combination of tapioca flour with coconut flour, do you have any of these ingredients?"
        if name == "almond extract":
            message ="instead you can use, vanilla extract or almond flavoured liquor do you have any of these ingredients?"
        if name == "rose water":
            message ="instead you can use, rose essence, jamaica flower water,orange flower water, vanilla extract, almond extract, lavender, lemon juice or cardamom, do you have any of these ingredients?"
        if name == "food colouring":
            message ="instead you can use, liquid chlorophyll, matcha powder, spirulina powder, whatgrass juice or parsley juice, do you have any of these ingredients?"
        if name == "marzipan":
            message ="instead you can use almond paste, do you have this ingredient?"
        if name == "dried black beans":
            message ="instead you can use, kidney beans, pinto beans, lentils, soyebans, chickpeas or peas, do you have any of these ingredients?"
        if name == "lime juice":
            message ="instead you can use, lemon juice, lime zest, orange juice or white wine vinegar, do you have any of these ingredients?"
        if name == "red bell pepper":
            message ="instead you can use, poblano peppers, anaheim peppers, jalapeños, sichuan peppers, cubanelle or red, yellow or orange peppers, do you have any of these ingredients?"
        if name == "cocoa powder":
            message ="instead you can use, a chocolate bar, chocolate chips, chocolate coverture, hot chocolate drink powder or carob powder, do you have any of these ingredients?"
        if name == "agave syrup":
            message ="instead you can use, honey, simple syrup, maple syrup, brown rice syrup, white sugar, corn syrup or any artificial sweeteners, do you have any of these ingredients?"
        if name == "nutella":
            message ="instead you can use, any other chocolate spread or hazelnut and chocolate spread, do you have any of these ingredients?"
        if name == "maraschino cherries":
            message ="instead you can use, fresh cherries, amarena cherries or luxardo maraschino cherries , do you have any of these ingredients?"
        if name == "maraschino cherry juice":
            message ="instead you can use cherry juice with sugar, do you have these ingredient?"
        if name == "greek yogurt":
            message ="instead you can use, plain yogurt, sour cream, buttermilk, cottage cheese or silken tofu, do you have any of these ingredients?"
        if name == "roasted chicken meat":
            message ="instead you can use rotisserie chicken meat, do you have any of these ingredients?"
        if name == "old bay seasoning":
            message ="instead you can make your own by combining 1 tablespoon celery salt, 3 whole bay leaves, 3/4 teaspoon brown mustard seeds, 1/2 teaspoon black peppercorns, 10 allspice berries, 10 whole cloves and 1/2 teaspoon paprika or use crab boil or pickling spice; do you have any of these ingredients?"
        if name == "unsalted butter":
            message ="instead you can use, shortening, vegetable oil or lard, do you have any of these ingredients?"
        if name == "butterscotch chips":
            message ="instead you can use, caramel chips, chocolate chips or carob chips, do you have any of these ingredients?"
        if name == "sirloin steak":
            message ="instead you can use, ribeye steak, new York strip steaks, round steak or flank steak, do you have any of these ingredients?"
        if name == "dry mustard":
            message ="instead you can use, dijon mustard or yellow mustard, do you have any of these ingredients?"
        if name == "white wine":
            message ="instead you can use, apple cider vinegar, chicken broth, apple juice, grape juice, white wine vinegar or ginger ale, do you have any of these ingredients?"
        if name == "cauliflower":
            message ="instead you can use, broccoli, courgette or lettuce, do you have any of these ingredients?"
        if name == "orange zest":
            message ="instead you can use, any other citrus fruit zest, fruit juice, fruit concentrate, pure extracts or vinegar, do you have any of these ingredients?"
        if name == "green bell pepper":
            message ="instead you can use, poblano peppers, anaheim peppers, jalapeños, sichuan peppers, pimientos, cubanelle, red bell peppers or yellow bell peppers, do you have any of these ingredients?"
        if name == "chipotle chillies":
            message ="instead you can use, fresh jalapeños, serrano peppers or poblano peppers, do you have any of these ingredients?"
        if name == "chilli powder":
            message ="instead you can use, paprika, cumin, garlic powder, onion powder, oregano or cayenne, do you have any of these ingredients?"
        if name == "ground coriander":
            message ="instead you can use, cumin, caraway, garam masala or curry powder, do you have any of these ingredients?"
        if name == "ground cumin":
            message ="instead you can use, ground coriander, caraway seeds, chilli powder, taco seasoning, curry powder, garam masala, paprika or fennel seeds, do you have any of these ingredients?"
        if name == "ground buffalo":
            message ="instead you can use, ground bison or ground beef, do you have any of these ingredients?"
        if name == "pinto beans":
            message ="instead you can use black beans, navy beans, borlotti beans, red beans, kidney beans, white beans or cannellini beans, do you have any of these ingredients?"
        if name == "masa harina flour":
            message ="instead you can use, corn meal, gritis, regular flour, ground corn tortillas, corn starch, fresh masa or masa preparada, do you have any of these ingredients?"
        if name == "green beans":
            message ="instead you can use, nopalitos, thin asparagus stalks or wax beans, do you have any of these ingredients?"
        if name == "white flour":
            message ="instead you can use, almond flour, coconut flour, quinoa flour, chickpea flour, brown rice flour, oat flour, spelt flour or buckwheat flour, do you have any of these ingredients?"
        if name == "cardamom":
            message ="instead you can use, cinnamon and cloves, cinnamon and nutmeg or allspice powder, do you have any of these ingredients?"
        if name == "caster sugar":
            message ="instead you can use granulated sugar, do you have this ingredient?"
        if name == "free-range eggs":
            message ="instead you can use, banana, flaxseed, chia seeds, applesauce or organic eggs, do you have any of these ingredients?"
        if name == "shortening":
            message ="instead you can use, butter, coconut oil, margarine, lard, vegetable oil or vegan butter, do you have any of these ingredients?"
        if name == "vinegar":
            message ="instead you can use, lemon or lemon juice, do you have any of these ingredients?"
        if name == "mung beans":
            message ="instead you can use, snow peas or pigeon peas, do you have any of these ingredients?"
        if name == "hash browns":
            message ="instead you can use, cauliflower hash browns, keto has browns or fries, do you have any of these ingredients?"
        if name == "cream of chicken soup":
            message ="instead you can use, sour cream, yogurt, tomato sauce or eggs and milk  do you have any of these ingredients?"
        if name == "colby cheese":
            message ="instead you can use, pata cabra cheese, fontina cheese, limburguer cheese or carciotta cheese, do you have any of these ingredients?"
        if name == "sherry":
            message ="instead you can use, white wine vinegar, apple cider vinegar, sherry vinegar or port wine, do you have any of these ingredients?"
        if name == "sesame oil":
            message ="instead you can use, perilla oil, walnut oil, oilve oil, canola oil, avocado oil, tahini or roasted sesame seed, do you have any of these ingredients?"
        if name == "garlic sauce":
            message ="instead you can use, harissa sauce, sriracha, ketchup with garlic or red pepper flakes, do you have any of these ingredients?"
        if name == "red pepper flakes":
            message ="instead you can use, dried peppers, ground cayenne pepper or chilli powder, do you have any of these ingredients?"
        if name == "dill":
            message ="instead you can use, fennel, thyme, rosemary, parsley, chevil, basil or tarragon, do you have any of these ingredients?"
        if name == "smoked salmon":
            message ="instead you can use, smked mackerel, sardines, or pink snapper, do you have any of these ingredients?"
        if name == "arborio rice":
            message ="instead you can use, pearled barley, basmati rice, brown rice, carnaroli rice, sushi rice, quinoa or bulgur wheat, do you have any of thse ingredients?"
        if name == "marinara sauce":
            message ="instead you can use tomato sauce mixed with water, do you have this ingredient?"
        if name == "baby green peas":
            message ="instead you can use, black-eyed peas, lima beans or fresh cranberry beans, do you have any of these ingredients?"
        if name == "bread crumbs":
            message ="instead you can use, almonds, walnuts, chia seeds or flax seeds, do you have any of these ingredients?"
        if name == "flour tortillas":
            message ="instead you can use, corn tortillas, grain-free tortillas, lettuce wraps or spinach wraps, , do you have any of these ingredients?"
        if name == "chillies":
            message ="instead you can use, red bell pepper flakes or smoked paprika, do you have any of these ingredients?"
        if name == "guacamole":
            message ="instead you can use, nut butter, pesto, edamame beans, hummus or mockamole, do you have any of these ingredients?"
        if name == "refried beans":
            message ="instead you can use, chilli beans, rattlesnake beans, red kidney beans or cranberry beans, do you have any of these ingredients?"
        if name == "angel food cake mix":
            message ="instead you can use sponge cake mix, do you have this ingredient?"
        if name == "milkfish":
            message ="instead you can use mullet fish, do you have this ingredient?"
        if name == "calamansi juice":
            message ="instead you can use, lime juice, orange juice, vinegar, citric acid, lemon zest, white wine, lemon extract or cream of tartar, do you have any of these ingredients?"
        if name == "pickles":
            message ="instead you can use, chopped dill pickles, freen olives, capers, green bell peppers, celery or cucumbers, do you have any of these ingredients?"
        if name == "eggplant":
            message ="instead you can use, okra, zuchinni, mushrooms, summer squash or root vegetables, do you have any of these ingredients?"
        if name == "grapes":
            message ="instead you can use, baby kiwi, mayhaw berries, white mulberries or elderberry, do you have any of these ingredients?"
        if name == "pork":
            message ="instead you can use, chicken or tempeh, do you have any of these ingredients?"
        if name == "annatto powder":
            message ="instead you can use, hibiscus powder, tumeric powder, nutmeg, beet powder and paprika, do you have any of these ingredients?"
        if name == "kinchay":
            message ="instead you can use, parsley, basil or herb mixtures, do you have any of these ingredients?"

        dispatcher.utter_message(text=message)
        return []



class actionUtensils(Action):

    def name(self) -> Text:
        return "action_utensilexplan"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        entities= tracker.latest_message['entities']
        print(entities)
        #message='test'
        name=''
        print(entities)
        for e in entities:
             if e['entity'] =='utensils':
                name = e['value']   
        print(name)
        if name == "bowl":
                message = "A cooking container that is usually larger than a cup and kept in a cupboard in the kitchen, it is typically made from glass, ceramic, plastic."
        if name == "spoon":
               message = "an eating or cooking utensil consisting of a small shallow bowl with a relatively long handle made from metal, plastic, wood it is usually kept in the kitchen, in drawer."
        if name == "sieve":
               message = "A metal or plastic device with meshes or perforations through which finer particles of a mixture are sifted, it is usually kept in a kitchen and stored in a cupboard."
        if name == "pan":
               message = "A shallow and open cooking container made from metal, it is usually found in a kitchen and stored in a cupboard."
        if name == "baking tray":
               message = "A metal rectangular sheet with a rolled edge used for baking, it is usually found in a kitchen inside a cupboard or draw."
        if name == "whisk":
               message = "A metal or plastic wire utensil used for beating food by hand it is usually found in a kitchen inside a drawer."               
        if name == "oven":
               message = "a cooking chamber used for baking, heating, or drying it is usually found in a kitchen."               
        if name == "cellophane":
               message = "thin transparent plastic sheets used to package or cover food items, it is usually kept in a kitchen inside drawer or cupboard."               
        if name == "tea towel":
               message = "A fabric cloth used for drying dishes, it is typically found in a kitchen or airing cupboard."               
        if name == "frying pan":
               message = "an open metal container with a handle that is used for frying foods, it is usually found in a kitchen inside a cupboard."               
        if name == "kettle":
               message = "A metal or plastic vessel used for boiling liquids, it is usually found in a kitchen on a tabletop or inside a cupboard"
        if name == "kitchen knife":
               message = "A cutting instrument consisting of a sharp blade fastened to a handle, it is usually found in a kitchen inside a draw."               
        if name == "saucepan":
               message = "A small deep metal cooking pan with a handle it is usually kept in a kitchen cupboard."               
        if name == "greaseproof paper":
               message = "a heavy stiff waxed paper used in cooking and baking to prevent food from sticking to cooking trays it is usually kept inside a kitchen drawer."               
        if name == "cup":
               message = "A ceramic, porcelain or glass bowl-shaped drinking vessel usually kept in a kitchen cupboard."                   
        if name == "measuring jug":
               message = "A plastic or glass cup that has markings for measuring liquids when cooking, it is usually kept inside a kitchen cupboard."               
        if name == "dinner plate":
               message = "A ceramic large plate usually 10 inches in diameter used for the main course of a meal, it is usually kept in a kitchen cupboard. "               
        if name == "rolling pin":
               message = "a long wooden or plastic cylinder for rolling out dough, it is usually kept in a kitchen drawer."               
        if name == "food processor":
               message = "an electric kitchen appliance with a set of interchangeable blades revolving inside a container, it is usually kept in a kitchen cupboard."               
        if name == "fluted flan tin":
               message = "A metal cooking tin with a removable base, usually found in a kitchen drawer"               
        if name == "dinner fork":
               message = "a large metal fork with 3 or 4 tines, it is usually found in a kitchen drawer."
        if name == "pastry brush":
               message = "also known as a basting brush, it is a wooden or plastic cooking utensil used to spread butter, oil or glaze on food, it is usually kept in a kitchen  drawer."               
        if name == "round bladed knife":
               message = "also known as a butter knife is a non-sharp plastic or metal knife used to mix the butter chunks, it is usually found in a kitchen drawer."               
        if name == "fridge":
               message = "an appliance for keeping food or other items cool, it is usually found in a kitchen or utility room."               
        if name == "food bag":
               message = "A plastic sealable sleeve for preserving food items, it is usually kept in a kitchen cupboard."                   
        if name == "casserole dish":
               message = "a large and deep, glass or ceramic cooking bowl, it is usually kept in a kitchen cupboard."               
        if name == "teaspoon":
               message = "A small spoon that is used especially for eating soft foods and stirring beverages and that holds about one third of a tablespoon, it is usually stored in a kitchen drawer. "               
        if name == "mixing bowl":
               message = "A large ceramic or plastic bowl used in cooking for mixing ingredients, it is usually stored in a kitchen cupboard."               
        if name == "wooden spoon":
               message = "A large wooden spoon for stirring ingredients, it is usually stored in a kitchen drawer."               
        if name == "chop sticks":
               message = "a pair of slender plastic or wooden sticks held between thumb and fingers and used chiefly in Asian countries to lift food to the mouth, they are usually stored in a kitchen drawer."               
        if name == "colander":
               message = "A perforated plastic or metal cylinder for washing or draining food, it is usually stored in a kitchen cupboard."                   
        if name == "filleting knife":
               message = "A blunt metal concave knife or a flexible wire tool used to flesh a skin or hide, it is usually stored in a kitchen drawer."               
        if name == "fish slice":
               message = "A metal or plastic kitchen tool that has a handle which is bent upward, and a wide, thin blade used for lifting and turning foods on a hot surface, it is usually stored in a kitchen drawer."               
        if name == "bottle opener":
               message = "a tool used to remove metal tops from some bottles, it is usually stored in a kitchen draw."               
        if name == "dessert spoon":
               message = "a spoon intermediate in size between a teaspoon and a tablespoon for eating dessert, it is usually stored in a kitchen draw."               
        if name == "can opener":
               message = "A device that is used to open cans of food, it is usually stored in a kitchen draw or cupboard."               
        if name == "bread knife":
               message = "A knife with a long blade that has a serrated or scalloped edge, it is usually stored in a kitchen draw."
        if name == "dinner knife":
               message = "A large table knife usually with a steel or silver blade and a handle, it is usually stored in a kitchen draw."               
        if name == "ladle":
               message = "A deep-bowled long-handled spoon used especially for dipping up and conveying liquids, it is typically stored in a kitchen cupboard."               
        if name == "masher":
               message = "A utensil for mashing cooked, raw or boiled food, it is usually stored in a kitchen draw or cupboard."
        if name == "peeler":
               message = "A metal blade with a slot with a sharp edge attached to a handle, used to remove the outer layer (the skin or peel) of some vegetables such as potatoes, broccoli stalks, and carrots, and fruits such as apples and pears"                   
        if name == "pizza cutter":
               message = "also known as a roller blade or a pizza wheel is a round bladed utensil that is used to cut pizzas, it is usually kept in the kitchen inside a draw."               
        if name == "serving spoon":
               message = "A large spoon or ladle used to serve out individual portions of food, it is usually kept in a kitchen drawer."               
        if name == "soup spoon":
               message = "A soup spoon is a type of spoon with a large or rounded bowl, used for consuming soup, it is usually stored in a kitchen draw."               
        if name == "tongs":
               message = "A type of metal or plastic tool used to grip and lift objects instead of holding them directly with hands, they are usually stored in a kitchen drawer."               
        if name == "kitchen scissors":
               message = "scissors that are used for cutting and trimming foods such as meats, they are usually stored in a kitchen drawer."               
        if name == "mason jar":
               message = "Jars that have a two-part top a lid with a rubber ring on the underside, which creates a vacuum seal and an outer band with screw threads that are reusable. They are usually stored in a pantry or kitchen cupboard."
        if name == "food blender":
               message = "A machine that reduces solid food to a liquid or puree using rotating blades, they are usually stored in a kitchen cupboard."               
        if name == "bottle":
               message = "a glass container for liquids and preserves, they are usually stored in a pantry or kitchen cupboard."               
        if name == "paring knife":
               message = "A small sharp knife with a short blade, it is usually kept in a kitchen drawer."               
        if name == "garlic press":
               message = "An instrument used to crush raw garlic into smaller chunks, it is usually kept in a kitchen drawer."               
        if name == "food grater":
               message = "A device used to slice whole food into smaller parts, it is usually kept in a kitchen cupboard."               
        if name == "kitchen scales":
               message = "a device to weigh and measure foods, sauces and powders for cooking, it is usually found in a kitchen cupboard."               
        if name == "measuring spoon":
               message = "A spoon used to measure an amount of an ingredient, either liquid or dry, when cooking, it is usually located in a kitchen drawer."                   
        if name == "ovenproof dish":
               message = "A dish made from a heatproof material such as glass, metal or earthenware that can withstand temperatures of 250 degrees, gas mark 9 and is suitable for use in the oven, it can usually be found in a kitchen cupboard."               
        if name == "baking tray":
               message = "A a flat, rectangular metal pan used in an oven. It is often used for baking bread rolls, pastries and flat products such as cookies, sheet cakes, Swiss rolls and pizzas. It is usually kept in a kitche drawer or cupboard"               
        if name == "stirring spoon":
               message = "A spoon used for stirring liquids and drinks such as cocktails, it is usually kept in a kitchen drawer."    
        if name == "slotted spoon":
               message = "The term can be used to describe any spoon with slots, holes or other openings in the bowl of the spoon which let liquid pass through while preserving the larger solids on top, it is usually stored in a kitchen drawer."
        if name == "spatula":
               message = "A broad, flat, flexible blade used to mix, spread and lift material including foods, drugs, plaster and paints. It is usually kept in a kitchen drawer or cupboard."
        if name == "oven glove":
               message = "Also known as a oven mitt, is an insulated glove or mitten usually worn in the kitchen to easily protect the wearer's hand from hot objects such as ovens, stoves, cookware. They are usually located in the kitchen on a hook or in a drawer."                   
        if name == "pot holder":
               message = "A piece of textile or silicone used to cover the hand when holding hot kitchen cooking equipment, like pots and pans, it can usually be found in a kitchen cupboard."               
        if name == "meat thermometer":
               message = "Also known as a cooking thermometer is a thermometer used to measure the internal temperature of meat, especially roasts and steaks, and other cooked foods, it is usually kept in a kitchen drawer."               
        if name == "pasta fork":
               message = "A utensil used when preparing and serving various types of strand, ribbon or noodle pasta. The fork is spoon-shaped with upward pointing pieces, either dowel-like or prong-shaped, separated around or on the fork and lifter tool. It is usually kept in a kitchen drawer."                   
        if name == "corkscrew":
               message = "A tool for drawing corks from wine bottles and other household bottles that may be sealed with corks. In its traditional form, a corkscrew simply consists of a pointed metallic helix attached to a handle, which the user screws into the cork and pulls to extract it. It is usually stored in a kitchen drawer."               
        if name == "cling film":
               message = "Also known as, Plastic wrap, Saran wrap, cling wrap, Glad wrap or food wrap is a thin plastic film typically used for sealing food items in containers to keep them fresh over a longer period of time. It is usually stored in a kitchen cupboard."               
        if name == "kitchen foil":
               message = "A sheet of aluminium prepared in thin metal leaves used to protect food when heating inside an oven, it is usually stored inside a kitchen drawer or cupboard."                   
        if name == "cutting board":
               message = "A durable board on which to place material for cutting. The kitchen cutting board is commonly used in preparing food; other types exist for cutting raw materials such as leather or plastic. Kitchen cutting boards are often made of wood or plastic and come in various widths and sizes and are usually found in a kitchen drawer or cupboard."               
        if name == "salad spinner":
               message = "also known as a salad tosser, is a kitchen tool used to wash and remove excess water from salad greens. It uses centrifugal force to separate the water from the leaves, enabling salad dressing to stick to the leaves without dilution. They are usually found in a kitchen cupboard."          
        if name == "kitchen shears":
               message = "also known as kitchen scissors, are intended for cutting and trimming foods such as meats. They are usually stored in a kitchen drawer."              
        if name == "lemon squeezer":
               message = "A small kitchen utensil designed to extract juice from lemons or other citrus fruit such as oranges, grapefruit, or lime. It is designed to separate and crush the pulp of the fruit in a way that is easy to operate and usually stored in a kitchen drawer or cupboard."          
        if name == "sharpening rod":
               message = "sometimes referred to as sharpening steel, whet steel, sharpening rod, butcher's steel, and chef's steel, is a rod of steel, ceramic or diamond-coated steel used to re-align blade edges. They are usually kept in a kitchen drawer or cupboard. "          
        if name == "Knife sharpener":
               message = "A tool used to make a knife or similar tool sharp by grinding against a hard, rough surface, typically a stone, or a flexible surface with hard particles, such as sandpaper. Additionally, a leather razor strop, or strop, is often used to straighten and polish an edge. They are typically stored in a kitchen cupboard or drawer. "              
        if name == "skillet":
               message = "A flat-bottomed metal pan used for frying, searing, and browning foods. They are usually stored in a kitchen cupboard."          
        if name == "Saute pans":
               message = "a hybrid between a saucepan and a frying pan. An extremely versatile addition to a kitchen, it can be used for a huge variety of dishes, they are usually stored in a kitchen cupboard."               
        if name == "grill pan":
               message = "a pan that has raised edges with grill lines dispersed around 1 to 2 centimetres separated, they are usually stored in a kitchen cupboard."                   
        if name == "muffin pan":
               message = "also know as a cupcake tray is a mould in which muffins or cupcakes are baked, they are usually stored in a kitchen drawer or cupboard."               
        if name == "broiling pan":
               message = "a pan used to broil foods in an oven such as steaks, roasts, or various cuts of meat, poultry, and vegetables. They are usually found in a kitchen cupboard or hung on a rack."               
        if name == "Stock pot":
               message = "a generic name for one of the most common types of cooking pot used worldwide. A stock pot is traditionally used to make stock or broth, which can be the basis for cooking more complex recipes. It is usually stored in a kitchen cupboard or rack."                   
        if name == "trivet":
               message = "An object placed between a serving dish or bowl, and a dining table, usually to protect the table from heat damage. It is usually stored in a drawn in a kitchen or dining room."               
        if name == "splatter guard":
               message = "A device placed over a frying pan to prevent hot oil from spitting out of the pan, which often happens when pan frying at a high temperature. It is typically stored in a kitchen cupboard."               
        if name == "kitchen scales":
               message = "A household tool that is used to measure the weight of dry, liquid, or chopped ingredients. It is usually stored in a kitchen cupboard."                   
        if name == "sponge":
               message = "A cleaning aid made of soft, porous material. Typically used for cleaning impervious surfaces, sponges are especially good at absorbing water and water-based solutions. They are typically stored in a kitchen or cleaning cupboard."               
        if name == "dish rack":
               message = "A device used to separate and dry dishes after cleaning, they are usually kept in the kitchen on a sideboard, sink or in a cupboard."               
        if name == "ice cube tray":
               message = "a container designed to be filled with water, then placed in a freezer until the water freezes into ice, producing ice cubes. Ice trays are often flexible, so the frozen cubes can be easily removed by flexing the tray. When not in use, they are usually kept in a draw or cupboard in the kitchen."               
        if name == "bin bag":
               message = "also known as a rubbish bag, garbage bag, bin liner, trash bag or refuse sack is a disposable bag used to contain solid waste. They are usually found in a kitchen or cleaning cupboard."               
        if name == "serrated blade":
               message = "A a type of jagged blade used on saws and on some knives or scissors. It is also known as a dentated, sawtooth, or toothed blade. They are usually stored in the kitchen on a knife rack of inside a drawer."                   
        if name == "food turner":
               message = "An elongated and thinner version of the common metal spatula, designed to easily slip under delicate fillets of fish. They are typically stored inside a kitchen drawer."               
        if name == "zester":
               message = "A kitchen utensil for obtaining zest from lemons and other citrus fruit. They are typically found inside a kitchen drawer or cupboard."               
        if name == "microwave":
               message = "A oven (commonly referred to as a microwave) is an electric oven that heats and cook’s food by exposing it to electromagnetic radiation in the microwave frequency range. They are typically found in a kitchen on a sideboard."                   
        if name == "rice cooker":
               message = "An automated kitchen appliance designed to boil or steam rice. They are usually found in a kitchen inside a cupboard or on a worktop."               
        if name == "slow cooker":
               message = "Also known as a crock-pot, is a countertop electrical cooking appliance used to simmer at a lower temperature than other cooking methods, such as baking, boiling, and frying. They are usually found in a kitchen cupboard or on a sideboard."               
        if name == "electric grill":
               message = "a grilling unit that uses an electric element to supply a constant heat source. They are typically installed inside a worktop or inside a kitchen cupboard."                   
        if name == "air fryer":
               message = "a small countertop convection oven designed to simulate deep frying without submerging the food in oil. They are typically found in a kitchen cupboard or on a worktop."               
        if name == "bachelor grill":
               message = "also known as a mini oven or mini kitchen is a countertop kitchen appliance about the size of a microwave oven but instead can grill, bake, broil, or roast food. They are typically found inside a kitchen cupboard or on a countertop."               
        if name == "barbecue":
               message = "a cooking method, a cooking device, a style of food, and a name for a meal or gathering at which this style of food is cooked and served. They are usually found in a kitchen cupboard, garage or garden shed."                   
        if name == "beehive oven":
               message = "A dome-shaped beehive ovenbrick structure that looks a bit like an insect's nest, hence the name beehive. They are usually found in larger kitchens and gardens."               
        if name == "brazier":
               message = "A metal container used to burn charcoal or other solid fuel for cooking, heating, or cultural rituals. They are usually found in sheds and used in outdoor cooking spaces."               
        if name == "bread machine":
               message = "also known as a bread maker is a home appliance for turning raw ingredients into baked bread. They are usually found in a kitchen inside a cupboard or on a worktop."                   
        if name == "burjiko":
               message = "A Somali-style cooker or charcoal burning stove, it is usually found in outdoor eating areas or in professional restaurants."               
        if name == "butane torch":
               message = "A tool which creates an intensely hot flame using butane, a flammable gas. It is often used to flambe deserts and can usually be found in a kitchen draw or cupboard."               
        if name == "chapati maker":
               message = "a machine that flattens handmade dough balls into round roti’s and bakes them. They are typically found in a kitchen cupboard or on a worktop."                   
        if name == "cheese melter":
               message = "A cooking device used to melt cheese, it is usually found in a kitchen cupboard or on a worktop."               
        if name == "chocolatier":
               message = "A type of high-necked metal pot shaped like a pitcher used for the traditional preparation of hot chocolate drinks. They are typically found in a kitchen cupboard or on a worktop."               
        if name == "chorkor":
               message = "is an oven used for smoking fish, they are typically found in restaurants and outdoor eating areas."                   
        if name == "clome oven":
               message = "A type of masonry oven. It has a removable door made of clay or alternatively a cast-iron door. They are typically found in large kitchens and outdoor eating areas."               
        if name == "comal":
               message = "A pan that is used for cooking a variety of items. It is made of cast iron and is very heavy. It is typically found in a kitchen cupboard or rack."               
        if name == "combi oven":
               message = "A three-in-one oven which allows you to cook with steam, hot air (convection) or a combination of both, they are typically stand alone units in large kitchens."               
        if name == "convection microwave":
               message = "A stand alone oven that combines some of the features of two kitchen appliances, a microwave and a convection oven, allowing you to bake and roast foods in addition to heating them. They are typically located on a kitchen worktop."               
        if name == "convection oven":
               message = "An oven that has fans to circulate air around food which gives a very even heat. The increased air circulation causes a fan-assisted oven to cook food faster than a conventional non-fan oven, which relies only on natural convection to circulate the hot air. They are typically stand alone units found in large kitchens."                   
        if name == "corn roaster":
               message = "A large grill for cooking large batches of ears of corn at the same time, the are usually located in a kitchen cupboard or on a worktop."               
        if name == "crepe maker":
               message = "A cooking device used to make crepes, galettes, pancakes, blinis or tortillas. They are usually found in a kitchen cupboard or on a worktop."               
        if name == "deep fryer":
               message = "A kitchen appliance used for deep frying. Deep frying is a method of cooking by submerging food into oil at high heat. They are usually found in a kitchen cupboard or on a worktop."               
        if name == "earth oven":
               message = "Also known as a ground oven or cooking pit is one of the simplest and most ancient cooking structures. At its most basic, an earth oven is a pit in the ground used to trap heat and bake, smoke, or steam food. They are usually found in outdoor cooking areas."               
        if name == "electric cooker":
               message = "An electric powered cooking device for heating and cooking of food. An electric cooker often has four stoves and one or two ovens. They are usually built into kitchen worktops or if portable located in a kitchen cupboard."                   
        if name == "espresso machine":
               message = "A device that brews coffee by forcing pressurized water near boiling point through a puck of ground coffee and a filter in order to produce a thick, concentrated coffee called espresso. They are usually found in a kitchen cupboard or on a worktop."               
        if name == "fire pot":
               message = "A container, usually earthenware, for carrying fire. Fire pots have been used since prehistoric times to transport fire from one place to another, for warmth while on the move, for cooking, in religious ceremonies and even as weapons of war."               
        if name == "flattop grill":
               message = "A cooking appliance that resembles a griddle but performs differently because the heating element is circular rather than straight. They are typically located in a kitchen cupboard or on a worktop."               
        if name == "food steamer":
               message = "also known as a steam cooker, is a small kitchen appliance used to cook or prepare various foods with steam heat by means of holding the food in a closed vessel reducing steam escape. They are typically located in a kitchen cupboard or on a worktop."               
        if name == "fufu machine":
               message = "A kitchen appliance used to pound cooked starchy vegetables, particularly cassava, plantains, or yams, into the West and Central African staple food fufu. They are usually found in a kitchen cupboard or drawer. "                   
        if name == "griddle":
               message = "A cooking device consisting of a broad flat surface heated by gas, electricity, wood, or coal, with both residential and commercial applications. They are usually inbuilt into kitchen worktops or if portable stored in a kitchen cupboard."               
        if name == "halogen oven":
               message = "A halogen convection oven, or halogen cooking pot is a type of oven that utilizes a halogen lamp as its heating element. It is used primarily for cooking in large kitchen, they are typically built into kitchen worktops."               
        if name == "haybox":
               message = "also known as a straw box, fireless cooker, insulation cooker, wonder oven, self-cooking apparatus, Norwegian cooker or retained-heat cooker is a cooker that utilizes the heat of the food being cooked to complete the cooking process."               
        if name == "horno":
               message = "a mud adobe-built outdoor oven used by Native Americans and early settlers of North America. Originally introduced to the Iberian Peninsula by the Moors, it was quickly adopted and carried to all Spanish-occupied lands."               
        if name == "hot box":
               message = "A device used to continue cooking food after the food has been partially cooked on a stove. This is done by insulating a container and placing the pot of food in the container to be sealed up."                   
        if name == "hot plate":
               message = "A portable self-contained tabletop small appliance cooktop that features one or more electric heating elements or gas burners."               
        if name == "instant pot":
               message = "A Canadian brand of multicookers. The multicookers are electronically controlled, combined pressure cookers and slow cookers. The original cookers are marketed as 6-in-1 or more appliances designed to consolidate the cooking and preparing of food to one device."               
        if name == "kamado":
               message = "A traditional Japanese wood- or charcoal-fuelled cook stove, typically found in outdoor cooking areas and large kitchens."               
        if name == "kitchner range":
               message = "An oven with a cast-iron hotplate for over a fire with removable boiling rings. They are usually stand-alone units in large kitchens."               
        if name == "Kujiejun":
               message = "a type of bamboo stove and is also a special term for tea stove. Popular during Song Dynasty, the bamboo windscreen stove frame would fit on top of a brazier."                   
        if name == "kyoto box":
               message = "A solar cooker constructed from polypropylene with an acrylic plastic cover. The oven traps the sun’s rays, creating enough heat to cook or boil water. They are typically stored in sheds and garages and used for outdoor cooking."               
        if name == "makiyakinabe":
               message = "a square or rectangular cooking pan used to make Japanese-style rolled omelettes. The pans are commonly made from metals such as copper and tin and can also be coated with a non-stick surface. They are typically found in a kitchen cupboard or on a pan rack."               
        if name == "masonry oven":
               message = "colloquially known as a brick oven or stone oven, it is an oven consisting of a baking chamber made of fireproof brick, concrete, stone, clay, or cob. They are typically located in outdoor cooking areas."               
        if name == "multicooker":
               message = "an electric kitchen appliance for automated cooking using a timer. A typical multicooker can boil, simmer, bake, fry, deep fry, grill roast, stew, steam and brown food. They are typically found in large kitchens."               
        if name == "pancake machine":
               message = "An electrically powered machine that automatically produces cooked pancakes. They are typically found in a kitchen cupboard or on a worktop."               
        if name == "sandwich grill":
               message = "A kitchen countertop or stovetop grill that is used to make the traditional panini, a small Italian sandwich. Also referred to as a Panini Maker, Panini Press, or a Grill Press, the Panini Grill contains top and bottom ridged heat plates that press and grill the bread in one operation."                   
        if name == "popcorn maker":
               message = "A device used to pop popcorn. Since ancient times, popcorn has been a popular snack food, produced through the explosive expansion of kernels of heated corn. They are typically found in a kitchen cupboard or on a worktop."               
        if name == "pressure cooker":
               message = "pressure cooking is the process of cooking food under high pressure steam, employing water or a water-based cooking liquid, in a sealed vessel known as a pressure cooker. They are typically found in a kitchen cupboard or on a worktop."               
        if name == "pressure fryer":
               message = "A variation on pressure cooking where meat and cooking oil are brought to high temperatures while pressure is held high enough to cook the food more quickly. This leaves the meat very hot and juicy, they are typically found in a kitchen cupboard."               
        if name == "reflector oven":
               message = "A polished metal container, often made of tin. It is designed to enclose an article of food on all but one side, to cause it to bake by capturing radiant heat from an open fire, and reflecting the heat towards the food, avoiding smoke flavouring the food."               
        if name == "remoska":
               message = "A small portable electric oven with the cooking element housed in the lid of a pot. It consists of a Teflon-lined pan and a stand in addition to the lid mounted heating element. They are typically located in a kitchen cupboard or on a worktop."                   
        if name == "rice polisher":
               message = "A machine for buffing kernels of rice to change their appearance, taste, and texture or for transforming brown rice into white rice. Rice polishers are abrasive machines that use talc or some other very fine dust to buff the outer surface of rice kernels. They are typically found in a kitchen cupboard or on a worktop."               
        if name == "rotisserie":
               message = "also known as spit-roasting, is a style of roasting where meat is skewered on a spit – a long solid rod used to hold food while it is being cooked over a fire in a fireplace or over a campfire or roasted in an oven. They are typically located on a kitchen worktop or installed as a stand alone unit."               
        if name == "stove":
               message = "A device in which fuel is burned to heat either the space in which the stove is situated, or items placed on the heated stove or inside it in an oven."               
        if name == "tandoor":
               message = "also known as tannour is a cylindrical clay or metal oven used in cooking and baking, they are typically found in large and professional kitchens."               
        if name == "tangia":
               message = "An urn-shaped terra cotta cooking vessel. It is also the name of the stew cooked in the pot, they are typically found in a kitchen cupboard."                   
        if name == "toaster":
               message = "An electric small appliance designed to expose various types of sliced bread to radiant heat, browning the bread so it becomes toast. They are typically located in a kitchen cupboard or on a worktop."               
        if name == "turkey fryer":
               message = "An apparatus for deep-frying a turkey, they are typically found in large kitchens as stand alone units. "               
        if name == "vacuum fryer":
               message = "A deep-frying device housed inside a vacuum chamber. Vacuum fryers are fit to process low-quality potatoes that contain higher sugar levels than normal, as they frequently must be processed in spring and early summer before the potatoes from the new harvest become available. They are usually found in large and professional kitchens as standalone units."               
        if name == "waffle iron":
               message = "Also known as a waffle maker is a utensil or appliance used to cook waffles. It comprises two metal plates with a connecting hinge, moulded to create the honeycomb pattern found on waffles. They are typically found in kitchen cupboard or on a worktop."               
        if name == "wet grinder":
               message = "A tool for abrasive cutting of hard materials, or a food preparation appliance used especially in Indian cuisine for grinding food grains to produce a paste or batter. They are typically found in a kitchen cupboard or drawer."               
        if name == "food boiler":
               message = "A machine that generates steam or hot water to process, cook, or sanitize food products including meat, fruits, and vegetables, they are typically found in a kitchen cupboard or on a worktop."                   
        if name == "coffee percolator":
               message = "A type of pot used for the brewing of coffee by continually cycling the boiling or nearly boiling brew through the grounds using gravity until the required strength is reached, they are typically located in a kitchen cupboard or on a worktop."               
        if name == "apple corer":
               message = "A device for removing the core and pips from an apple. It may also be used for similar fruits, such as pears or quince. They are typically found in a kitchen drawer or cupboard."               
        if name == "apple slicer":
               message = "A device designed to both core and slices apples. They are typically located in a kitchen drawer or cupboard."               
        if name == "baster":
               message = "sometimes called a turkey baster, is a tube attached to a rubber bulb used to suck up and squirt cooking liquid from a pan onto roasting meat or poultry, thus moistening it. They are typically found in a kitchen drawer or cupboard."               
        if name == "beanpot":
               message = "A deep, wide-bellied, short-necked vessel used to cook bean-based dishes. Beanpots are typically made of ceramic, though some are made of other materials, such as cast iron. They are usually found in a kitchen cupboard or drawer."                   
        if name == "cookie press":
               message = "A device for making pressed cookies such as spritzgebäck. It consists of a cylinder with a plunger on one end, which is used to extrude cookie dough through a small hole at the other end. They are usually located in a kitchen cupboard."               
        if name == "browning dish":
               message = "A device used to simulate a frying pan or skillet so that foods such as steaks, chops, hamburgers, and even French toast can be prepared. They are usually located in a kitchen cupboard or on a pan rack."               
        if name == "pie server":
               message = "also called a cake shovel, pie knife, crepe spade, pie-getter, pie lifter, pie spatula, cake knife, or cake slice, is a serving utensil used in the cutting and serving of pies and cakes. They are usually located in a kitchen cupboard."               
        if name == "cheese cutter":
               message = "An implement for cutting cheese, especially by means of a wire which can be pulled through the cheese. They are usually found in a kitchen drawer in cupboard."               
        if name == "cheese knife":
               message = "A knife with a concaved blade made to cut hard cheeses, they are usually found in a kitchen drawer or on a knife rack."                   
        if name == "cheesecloth":
               message = "A loose-woven gauze-like carded cotton cloth used primarily in cheese making and cooking. They are usually located in a kitchen cupboard or drawer."               
        if name == "cherry pitter":
               message = "A device for removing the pit from a cherry, leaving the cherry relatively intact. They are usually stored in a kitchen drawer."               
        if name == "chinois":
               message = "A conical sieve with an extremely fine mesh. It is used to strain custards, purees, soups, and sauces, producing a very smooth texture. They are usually located in a kitchen cupboard."               
        if name == "clay pot":
               message = "A pot made of unglazed or glazed pottery, they are usually stored in a kitchen cupboard or on a rack."               
        if name == "cookie cutter":
               message = "A tool that is used for cutting cookies into a particular shape before you bake them. They are usually stored in a kitchen drawer or cupboard."                   
        if name == "crab cracker":
               message = "A device used to crack the tough shells of crabs, lobsters, and any other edible crustaceans, they are usually located in a kitchen drawer."               
        if name == "scraper":
               message = "A kitchen implement made of metal, plastics, wood, rubber or silicone rubber. They are usually located in a kitchen drawer or cupboard."               
        if name == "egg piercer":
               message = "A device that pierces the air pocket of an eggshell with a small needle to keep the shell from cracking during hard-boiling. If both ends of the shell are pierced, the egg can be blown out while preserving the shell. They are typically stored in a kitchen cupboard or drawer."               
        if name == "egg poacher":
               message = "A device that is used to poach eggs, a poached egg is an egg that has been cooked, outside the shell, by poaching, as opposed to simmering or boiling. They are usually stored in a kitchen cupboard or drawer."               
        if name == "egg separator":
               message = "A utensil used to separate the egg white from the egg yolk, they are usually stored in a kitchen drawer or cupboard."                   
        if name == "egg slicer":
               message = "A utensil used to slice peeled, hard-boiled eggs quickly and evenly. They are usually stored in a kitchen drawer or cupboard."               
        if name == "egg timer":
               message = "A device for timing the cooking of a boiled egg, traditionally a sealed glass container with a narrow neck in the middle through which, when the flask is inverted, sand flows for a fixed amount of time. They are typically stored in a kitchen drawer, cupboard or on a worktop."               
        if name == "fat separator":
               message = "A device that resembles measuring cups and are designed to drain liquid while keeping the fat layer contained. They are typically stored in a kitchen cupboard."               
        if name == "flour sifter":
               message = "A tool that breaks up any lumps in the flour and aerates it at the same time by pushing it through a gadget that is essentially a cup with a fine strainer at one end. They are typically stored in a kitchen cupboard."               
        if name == "food mill":
               message = "A food preparation utensil for mashing and sieving soft foods, they are typically stored in a kitchen cupboard."                   
        if name == "funnel":
               message = "A cooking tool with a large open top that slope down and decrease in size forming a small diameter outlet allowing placement into smaller areas. They are typically stored in a kitchen cupboard or cabinet."               
        if name == "grapefruit knife":
               message = "A special type of knife designed specifically for cutting grapefruit. Grapefruit knives are small with a curved serrated blade, designed to hug the curves of the grapefruit. They are usually stored in a kitchen drawer."               
        if name == "gravy strainer":
               message = "Also known as a gravy skimmer, fat separator, fat strainer is a device used to separate fats and juices from gravy’s, stocks and sauces. They are typically stored in a kitchen cupboard or cabinet."               
        if name == "herb chopper":
               message = "A cooking tool specifically designed for chopping fresh herbs. There are a variety of different designs and styles for herb choppers. They are usually stored in a kitchen drawer."               
        if name == "honey dipper":
               message = "A kitchen utensil used to collect viscous liquid (generally honey) from a container, which it then exudes to another location. They are usually stored in a kitchen drawer."                   
        if name == "lame":
               message = "A double-sided blade that is used to slash the tops of bread loaves in artisan baking. A lame is used to score bread just before the bread is placed in the oven. They are usually stored in a kitchen drawer or on a knife rack."               
        if name == "citrus reamer":
               message = "Also known as a lemon reamer or simply a reamer, is a small kitchen utensil used to extract the juice from a lemon or other small citrus fruit. They are usually stored in a kitchen drawer or cupboard."               
        if name == "lemon squeezer":
               message = "A small kitchen utensil designed to extract juice from lemons or other citrus fruit such as oranges, grapefruit, or lime. It is designed to separate and crush the pulp of the fruit in a way that is easy to operate. They are usually stored in a kitchen drawer or cupboard."               
        if name == "lobster pick":
               message = "Also known as a lobster fork is a long, narrow food utensil used to extract meat from joints, legs, claws, and other small parts of a lobster. Lobster picks are usually made of stainless steel and weigh as much as an average teaspoon, they are usually stored in a kitchen drawer."               
        if name == "mandoline":
               message = "A culinary utensil used for slicing and for cutting juliennes; with suitable attachments, it can make crinkle-cuts. Its name is derived from the wrist-motion of a skilled user of a mandoline, which resembles that of a player of the musical instrument mandolin. They are usually stored in a kitchen cupboard or cabinet."                   
        if name == "colander":
               message = "A kitchen utensil used to strain foods such as pasta or to rinse vegetables, they are usually stored in a kitchen cupboard or cabinet."               
        if name == "meat grinder":
               message = "A kitchen appliance for fine chopping and/or mixing of raw or cooked meat, fish, vegetables or similar food. They are typically stored in a kitchen cupboard or on a worktop."               
        if name == "melon baller":
               message = "A small spoon-like tool used to cut round- or oval-shaped sections of melon, known as melon balls, by pressing them into the melon's flesh and rotating. They are typically stored in a kitchen drawer or cabinet."               
        if name == "mezzaluna":
               message = "A knife consisting of one or more curved blades with a handle on each end, which is rocked back and forth chopping the ingredients below with each movement. They are typically stored in a kitchen drawer or knife rack."               
        if name == "milk frother":
               message = "A milk frother is a utensil for making milk froth, typically to be added to coffee. They are typically stored in a kitchen drawer."                   
        if name == "mortar and pestle":
               message = "Implements used since ancient times to prepare ingredients or substances by crushing and grinding them into a fine paste or powder. They are typically stored in a kitchen cupboard or cabinet."               
        if name == "nutmeg grater":
               message = "Also know as a nutmeg rasp, is a device used to grate a nutmeg seed. They are typically stored in a kitchen drawer. "               
        if name == "pastry bag":
               message = "A triangular-shaped bag made from cloth, paper, plastic, or the intestinal lining of a lamb, that is squeezed by hand to pipe semi-solid foods by pressing them through a hole. They are typically stored in a kitchen drawer or cupboard."               
        if name == "pastry blender":
               message = "A cooking utensil used to mix a hard fat into flour to make pastries. They are typically stored in a kitchen cupboard or cabinet."               
        if name == "pepper mill":
               message = "A device, of which you turn by hand to crush the peppercorns inside, they are typically stored in a kitchen cupboard, cabinet or left on a table."                   
        if name == "pie bird":
               message = "Also known as a pie vent, pie whistle, pie funnel, or pie chimney is a hollow ceramic device, originating in Europe, shaped like a funnel, chimney, or upstretched bird with open beak used for supporting or venting a pie. They are usually stored in a kitchen cupboard or cabinet."               
        if name == "roller docker":
               message = "Also known as a dough docker, roto-fork, or simply docker is a food preparation utensil which resembles either a small, spiked rolling pin, or a small rotary tiller. They are typically stored in a kitchen drawer or cupboard."               
        if name == "salt shaker":
               message = "also called a salt cellar in British English, are condiment dispensers used in Western culture that are designed to allow diners to distribute grains of edible salt. They are typically stored in a kitchen cupboard or on a table top."               
        if name == "tomato knife":
               message = "A small serrated kitchen knife designed to slice through tomatoes. The serrated edge allows the knife to penetrate the tomatoes’ skin quickly and with a minimum of pressure without crushing the flesh. They are typically stored in a kitchen drawer or on a knife rack."                   
        if name == "freezer":
               message = "A refrigerated cabinet or room for preserving food at very low temperatures. They are usually standalone units in kitchens."               
        if name == "skewer":
               message = "A thin metal or wood stick used to hold pieces of food together, they are usually stored in a kitchen drawer or cupboard."
        
                                            
        dispatcher.utter_message(text=message)
        return []

#class ActionHelloWorld(Action):
#rasa
#     def name(self) -> Text:
 #        return "action_hello_world"
#
 #    def run(self, dispatcher: CollectingDispatcher,
  #           tracker: Tracker,
   #          domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
 #        dispatcher.utter_message(text="Hello World!")
#
 #        return []

 




