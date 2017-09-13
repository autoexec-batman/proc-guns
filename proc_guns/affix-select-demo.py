import yaml
import random

barrels = yaml.load(open("affix_barrel.yml"))
sights = yaml.load(open("affix_sight.yml"))
magazines = yaml.load(open("affix_magazine.yml"))
print (barrels)
print (sights)
print (magazines)
print ("")

barrel_class = random.choice(barrels)
sight_class = random.choice(sights)
magazine_class = random.choice(magazines)
print (barrel_class)
print (sight_class)
print (magazine_class)
print("")

barrel_affix = random.choice(barrel_class['tiers'])
sight_affix = random.choice(sight_class['tiers'])
magazine_affix = random.choice(magazine_class['tiers'])
print (barrel_affix)
print (sight_affix)
print (magazine_affix)
print ("")