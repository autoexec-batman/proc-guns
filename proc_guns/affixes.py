import helpers
import random
import yaml

def select(current_part, current_slot):
 filename = "affix_" + current_part + ".yml"
 parts = yaml.load(open(filename))
 part_choices = []
 for part in parts:
  if part['slot'] == current_slot:
   part_choices.append(part)
 part_group = helpers.weighted_choice(part_choices)
 specific = helpers.weighted_choice(part_group['tiers'])
 roll = random.uniform(specific['min'], specific['max'])
 
 return dict(name=specific['name'], effect_name=part_group['effect_name'], effect_text=part_group['effect_text'], roll=roll)