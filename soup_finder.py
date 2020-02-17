all_soups = {
    'mushroom_mountain'  : {
            'price'      : 80,
            'ing1'       : 'bluecap',
            'ing2'       : 'bluecap'
    },
    'meteoric_mushroom'  : {
            'price'      : 100,
            'ing1'       : 'greenstalk',
            'ing2'       : 'bluecap'
    },
    'double_mush_potage' : {
            'price'      : 70,
            'ing1'       : 'greenstalk',
            'ing2'       : 'greenstalk'
    },
    'purple_haze'        : {
            'price'      : 220,
            'ing1'       : 'poisonpuff',
            'ing2'       : 'bluecap'
    },
    'mushstrone'         : {
            'price'      : 120,
            'ing1'       : 'poisonpuff',
            'ing2'       : 'greenstalk'
    }
}

# Create list of all potential ingredients by combining ing1 and ing2 and removing duplicates
# price_1 = all_soups['mushstrone']['price']
# price_2 = all_soups['purple_haze']['price']
# print([price_1, price_2])

"""Creates unique list of all ingredients in game"""
undiscovered_ingredients = []
for soup, soup_info in all_soups.items():
    if soup_info['ing1'] not in undiscovered_ingredients:
        undiscovered_ingredients.append(soup_info['ing1'])
# print(undiscovered_ingredients)

# for p_id, p_info in people.items():
    # print("\nPerson ID:", p_id)

    # for key in p_info:
        # print(key + ':', p_info[key])

# Input ingredients as they are found and remove that ingredient from ingredient_list
message = "Please input your ingredients as they are discovered. The undiscovered ingredients are: \n" + str(undiscovered_ingredients)
message += "\nEnter 'quit' to end program or 'new' to start over.\n"
message += "Ingredient: "
available_ingredients = []
while True:
    discovered_ingredient = input(message)
    available_ingredients.append(discovered_ingredient)
    if discovered_ingredient == 'quit':
        break
    elif discovered_ingredient == 'new':
        undiscovered_ingredients = []
        for soup, soup_info in all_soups.items():
            if soup_info['ing1'] not in undiscovered_ingredients:
                undiscovered_ingredients.append(soup_info['ing1'])
        available_ingredients = []
    else:
        for soup_id, soup_info in all_soups.items():
            for ingredient in available_ingredients:
                if ingredient == soup_info['ing1']:
                    print("\n" + str(soup_id) + ':', soup_info['price'], soup_info['ing1'], soup_info['ing2'])
                elif ingredient == soup_info['ing2']:
                    print("\n" + str(soup_id) + ':', soup_info['price'], soup_info['ing1'], soup_info['ing2'])
                # for p_id, p_info in people.items():
                    # print("\nPerson ID:", p_id)

                    # for key in p_info:
                        # print(key + ':', p_info[key])
        print("\t\nYour available ingredients are: " + str(available_ingredients) + "\n")
    # Add new ingredients to list of available ingredients
    # Add option to reinitialize program with new game


# Create available_soup dictionary using the available ingredients to identify which soup can be made

#  Sort by price from highest to lowest
# for soup in all_soups:
    # print(soup['price'])
    # [available_soups] = [soup['price']]
    # print(available_soups)

# Output list of soups available to make and then prompt for more ingredient input
