class Gun:
    
    def __init__(self, bullet_damage, magazine_size, fire_rate, reload_time, manufacturer):  
        self.manufacturer = manufacturer
        self.damage = int(bullet_damage * manufacturer['modifiers']['damage'])
        self.magazine_size = int(magazine_size * manufacturer['modifiers']['mag_size'])
        self.fire_rate = fire_rate * manufacturer['modifiers']['fire_rate']
        self.reload_time = reload_time * manufacturer['modifiers']['reload_time']
        