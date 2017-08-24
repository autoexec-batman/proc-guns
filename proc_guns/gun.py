class Gun:
    
    def __init__(self, guntype, manufacturer, quality):  
        self.manufacturer = manufacturer
        self.guntype = guntype
        self.quality = quality
		
        base_damage = guntype['base_stats']['bullet_damage'] * manufacturer['modifiers']['damage'] * quality['modifiers']['damage']
        base_magazine_size = guntype['base_stats']['magazine_size'] * manufacturer['modifiers']['mag_size']
        base_fire_rate = guntype['base_stats']['fire_rate'] * manufacturer['modifiers']['fire_rate']
        base_reload_time = guntype['base_stats']['reload_time'] *  manufacturer['modifiers']['reload_time']
		
        self.damage = int(base_damage)
        self.magazine_size = int(base_magazine_size)
        self.fire_rate = base_fire_rate 
        self.reload_time = base_reload_time        