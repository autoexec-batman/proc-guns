import yaml
import random

barrels = yaml.load(open("affix_barrel.yml"))
print (barrels)
print ("")

affix_class = random.choice(barrels)
print (affix_class)
print("")

affix = random.choice(affix_class['tiers'])
print (affix)
print ("")