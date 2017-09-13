import random

def weighted_choice(list):
    weighted_list = []
    for weighted_item in list:
        for i in range(weighted_item["weight"]):
            weighted_list.append(weighted_item)
    #print (weighted_list)
    return random.choice(weighted_list)