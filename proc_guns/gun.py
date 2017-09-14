import affixes
import random
class Gun:
    
    def __init__(self, guntype, manufacturer, quality):  
        self.manufacturer = manufacturer
        self.guntype = guntype
        self.quality = quality
		
        base_damage = guntype['base_stats']['bullet_damage'] * manufacturer['modifiers']['damage'] * quality['modifiers']['damage']
        base_magazine_size = guntype['base_stats']['magazine_size'] * manufacturer['modifiers']['mag_size']
        base_fire_rate = guntype['base_stats']['fire_rate'] * manufacturer['modifiers']['fire_rate']
        base_reload_time = guntype['base_stats']['reload_time'] *  manufacturer['modifiers']['reload_time']
        base_nice_chance = guntype['base_stats']['nice_chance'] * manufacturer['modifiers']['nice_chance']
        base_nice_multiplier = guntype['base_stats']['nice_multiplier'] * manufacturer['modifiers']['nice_multiplier']
		
       	raw_affix_modifiers = dict(
                                   raw_extra_nice_chance=0,                              
                                   raw_extra_nice_multiplier=0, 
                                   raw_extra_damage=0,					   
		                           raw_extra_magazine_size=0,  
                                   raw_extra_fire_rate=0,
                                   raw_faster_reload_time=0
                                  )
        percent_affix_modifiers = dict(
                                       percent_extra_nice_chance=1.00,
                                       percent_extra_nice_multiplier=1.00,
                                       percent_extra_damage=1.00,
                                       percent_extra_magazine_size=1.00,
                                       percent_extra_fire_rate=1.00,
                                       percent_faster_reload_time=1.00
                                      )
	
        available_parts = ['barrel', 'sight', 'magazine']
        available_slots = ['prefix', 'infix', 'suffix']
        random.shuffle(available_parts)
        random.shuffle(available_slots)
        gun_affixes = []
				
        part_count = random.randint(0,3)
        for i in range(0,part_count):
         current_part = available_parts.pop()
         current_slot = available_slots.pop()
         gun_affixes.append(affixes.select(current_part, current_slot))
		
        prefix = ""
        infix = ""
        suffix = ""
        self.raw_affix_text_data = []
		self.percent_affix_text_data = []
        affix_text_lines =[]
                
        
        
        for affix in gun_affixes:
         if affix['effect_name'] in raw_affix_modifiers:
          raw_affix_modifiers[affix['effect_name']] +=  affix['roll']
          self.raw_affix_text_data.append((affix['effect_text'}, affix['roll'])
         if affix['effect_name'] in percent_affix_modifiers:
          percent_affix_modifiers[affix['effect_name']] *= affix['roll']
          self.percent_affix_text_data.append((affix['effect_text'], affix['roll']))
         if affix['slot'] == 'prefix':
          prefix = affix['name']
         if affix['slot'] == 'infix':
          infix = affix['name']
         if affix['slot'] == 'suffix':
          suffix = affix['name']
                  

        self.damage = int((base_damage + raw_affix_modifiers['raw_extra_damage']) * percent_affix_modifiers['percent_extra_damage'])
        self.magazine_size = int((base_magazine_size + raw_affix_modifiers['raw_extra_magazine_size']) * percent_affix_modifiers['percent_extra_magazine_size'])
        self.fire_rate = (base_fire_rate + raw_affix_modifiers['raw_extra_fire_rate']) * percent_affix_modifiers['percent_extra_fire_rate']
        self.reload_time = (base_reload_time + raw_affix_modifiers['raw_faster_reload_time']) * percent_affix_modifiers['percent_faster_reload_time']
        self.nice_chance = (base_nice_chance + raw_affix_modifiers['raw_extra_nice_chance']) * percent_affix_modifiers['percent_extra_nice_chance']
        self.nice_multiplier = (base_nice_multiplier + raw_affix_modifiers['raw_extra_nice_multiplier']) * percent_affix_modifiers['percent_extra_nice_chance']
        self.gun_affixes = gun_affixes
        display_name = "{0} {1} {2} {3} {4}".format(prefix, manufacturer['qualities'][quality['name']], infix, guntype['name'], suffix)
        self.display_name = ' '.join(display_name.split()) #eliminates extra spaces from missing affixes
        