import json
import requests
from Cards import get_cards
from SortCards import sort_types, sort_cmc, sort_colours
from Generator import white_creatures
from math import ceil


sets_response = requests.get('https://mtgjson.com/api/v5/SetList.json')
sets_dictionary = sets_response.text
sets_read = json.loads(sets_dictionary)
sets_data = sets_read['data']

# number_of_sets = int(input("How many sets do you want to build your cube from? "))
# print_list = input("Do you want to see a list of set codes? (Y/N) ").upper()
# cube_size = int(input("How many cards in your cube? "))
cube_size = 200
# set_code = input("Please enter a set code: ").upper()
set_code = 'RAV'
card_pool = get_cards(set_code)
cube_list = []


# for i in range(number_of_sets):
#     set_code = input("Please enter a set code: ").upper()
#     card_pool.append(get_cards(set_code))

creature_limit = ceil(cube_size * 0.54)
creatures = sort_types(card_pool, "Creature")
colours = sort_colours(creatures)


for card in white_creatures(cube_size, colours, cube_list):
    cube_list.append(card)

for card in cube_list:
    print(card['name'])

print(len(cube_list))

