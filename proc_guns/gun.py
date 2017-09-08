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
		
        affixes = set()
		available_parts = ['barrel', 'sight', 'magazine']
		random.shuffle[available_parts]
		parts = set()
		
		part_count = random.randint(0,3)
		
		
		
		
		self.damage = int(base_damage)
        self.magazine_size = int(base_magazine_size)
        self.fire_rate = base_fire_rate 
        self.reload_time = base_reload_time
        self.nice_chance = base_nice_chance
        self.nice_multiplier = base_nice_multiplier