from Curve_Gen import creature_curve
from SortCards import sort_cmc


w_creature_count = [0, 0, 0, 0, 0, 0, 0]
u_creature_count = [0, 0, 0, 0, 0, 0, 0]
b_creature_count = [0, 0, 0, 0, 0, 0, 0]
r_creature_count = [0, 0, 0, 0, 0, 0, 0]
g_creature_count = [0, 0, 0, 0, 0, 0, 0]
c_creature_count = [0, 0, 0, 0, 0, 0, 0]
gold_creature_count = [0, 0, 0, 0, 0, 0, 0]


def white_creatures(cube_size, colours, cube_list):
    creature_limit = creature_curve(cube_size, ["W"])
    creature_count = sum(creature_limit)
    creatures_sorted = sort_cmc(colours[0])
    cmc_count = 0
    card_list = []

    while len(card_list) < creature_count:
        for cmc in creatures_sorted:
            for card in cmc:
                if card['name'] not in cube_list and card['name'] not in card_list:
                    card_list.append(card)
                    w_creature_count[cmc_count] += 1
            cmc_count += 1
    return card_list


def blue_creatures(cube_size, colours, cube_list):
    creature_limit = creature_curve(cube_size, ["U"])
    creatures_sorted = sort_cmc(colours[1])
    cmc_count = 0
    card_list = []
    for cmc in creatures_sorted:
        for card in cmc:
            if card['name'] not in cube_list and u_creature_count[cmc_count] < creature_limit[cmc_count]:
                card_list.append(card)
                w_creature_count[cmc_count] += 1
        cmc_count += 1
    return card_list


def black_creatures(cube_size, colours, cube_list):
    creature_limit = creature_curve(cube_size, ["B"])
    creatures_sorted = sort_cmc(colours[2])
    cmc_count = 0
    card_list = []
    for cmc in creatures_sorted:
        for card in cmc:
            if card['name'] not in cube_list and b_creature_count[cmc_count] < creature_limit[cmc_count]:
                card_list.append(card)
                w_creature_count[cmc_count] += 1
        cmc_count += 1
    return card_list


def red_creatures(cube_size, colours, cube_list):
    creature_limit = creature_curve(cube_size, ["R"])
    creatures_sorted = sort_cmc(colours[3])
    cmc_count = 0
    card_list = []
    for cmc in creatures_sorted:
        for card in cmc:
            if card['name'] not in cube_list and r_creature_count[cmc_count] < creature_limit[cmc_count]:
                card_list.append(card)
                w_creature_count[cmc_count] += 1
        cmc_count += 1
    return card_list


def green_creatures(cube_size, colours, cube_list):
    creature_limit = creature_curve(cube_size, ["G"])
    creatures_sorted = sort_cmc(colours[4])
    cmc_count = 0
    card_list = []
    for cmc in creatures_sorted:
        for card in cmc:
            if card['name'] not in cube_list and g_creature_count[cmc_count] < creature_limit[cmc_count]:
                card_list.append(card)
                w_creature_count[cmc_count] += 1
        cmc_count += 1
    return card_list


def colourless_creatures(cube_size, colours, cube_list):
    creature_limit = creature_curve(cube_size, [])
    creatures_sorted = sort_cmc(colours[5])
    cmc_count = 0
    card_list = []
    for cmc in creatures_sorted:
        for card in cmc:
            if card['name'] not in cube_list and c_creature_count[cmc_count] < creature_limit[cmc_count]:
                card_list.append(card)
                w_creature_count[cmc_count] += 1
        cmc_count += 1
    return card_list


def gold_creatures(cube_size, colours, cube_list):
    creature_limit = creature_curve(cube_size, ["Gold"])
    creatures_sorted = sort_cmc(colours[6])
    cmc_count = 0
    card_list = []
    for cmc in creatures_sorted:
        for card in cmc:
            if card['name'] not in cube_list and gold_creature_count[cmc_count] < creature_limit[cmc_count]:
                card_list.append(card)
                w_creature_count[cmc_count] += 1
        cmc_count += 1
    return card_list
