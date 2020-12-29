import json
import random

import requests


def get_cards(enter_set_code=''):
    # Returns a list of dictionaries of cards
    response = requests.get(f'https://mtgjson.com/api/v5/' + enter_set_code + '.json')
    dictionary = response.text
    read = json.loads(dictionary)
    data = read['data']
    card_list = random.sample(data['cards'], data['totalSetSize'])
    return card_list
