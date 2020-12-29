from math import ceil


def sort_types(pool_of_cards, card_type):
    # Sorting cards into lists of types
    card_list = []
    for card in pool_of_cards:
        if card_type in card["types"]:
            card_list.append(card)
    return card_list


def sort_cmc(pool_of_cards):
    # Returns a array of lists sorted by cmc 0 through 5 and then one final 6+
    cmc = [[], [], [], [], [], [], []]
    for card in pool_of_cards:
        if card['convertedManaCost'] == 0.0:
            cmc[0].append(card)
        elif card['convertedManaCost'] == 1.0:
            cmc[1].append(card)
        elif card['convertedManaCost'] == 2.0:
            cmc[2].append(card)
        elif card['convertedManaCost'] == 3.0:
            cmc[3].append(card)
        elif card['convertedManaCost'] == 4.0:
            cmc[4].append(card)
        elif card['convertedManaCost'] == 5.0:
            cmc[5].append(card)
        else:
            cmc[6].append(card)
    return cmc


def sort_colours(pool_of_cards):
    # Returns a array of lists sorted by colour in WUBRG-C-Gold order
    colours = [[], [], [], [], [], [], []]
    for card in pool_of_cards:
        if card['colorIdentity'] == ['W']:
            colours[0].append(card)
        elif card['colorIdentity'] == ['U']:
            colours[1].append(card)
        elif card['colorIdentity'] == ['B']:
            colours[2].append(card)
        elif card['colorIdentity'] == ['R']:
            colours[3].append(card)
        elif card['colorIdentity'] == ['G']:
            colours[4].append(card)
        elif not card['colorIdentity']:
            colours[5].append(card)
        else:
            colours[6].append(card)
    return colours


def sort_rarity(pool_of_cards, cube_size):
    # Returns an array of lists sorted by rarity Common, Uncommon, Rare, Mythic
    rarity = [[], [], [], []]
    card_list = []
    rare_limit = [ceil(cube_size * 0.2), ceil(cube_size * 0.2), ceil(cube_size * 0.3), ceil(cube_size * 0.3)]
    rare_count = [0, 0, 0, 0]

    for card in pool_of_cards:
        if card['rarity'] == 'common':
            rarity[0].append(card)
        elif card['rarity'] == 'uncommon':
            rarity[1].append(card)
        elif card['rarity'] == 'rare':
            rarity[2].append(card)
        else:
            rarity[3].append(card)

    for iteration in rarity:
        for card in iteration:
            if rare_count[0] < rare_limit[0]:
                card_list.append(card)
                rare_count[0] += 1
            elif rare_count[1] < rare_limit[1]:
                card_list.append(card)
                rare_count[1] += 1
            elif rare_count[2] < rare_limit[2]:
                card_list.append(card)
                rare_count[2] += 1
            elif rare_count[3] < rare_limit[3]:
                card_list.append(card)
                rare_count[3] += 1

    return card_list
