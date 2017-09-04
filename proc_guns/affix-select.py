import yaml
import random

barrels = yaml.load(open("affix_barrel.yml"))
sights = yaml.load(open("affix_sight.yml"))
print (barrels)
print(sights)
print ("")

barrel_class = random.choice(barrels)
sight_class = random.choice(sights)
print (barrel_class)
print(sight_class)
print("")

barrel_affix = random.choice(barrel_class['tiers'])
sight_affix = random.choice(sight_class['tiers'])
print (barrel_affix)
print (sight_affix)
print ("")