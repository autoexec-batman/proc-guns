from gun import Gun
import random
import enums

BASE_BULLET_DAMAGE = 10 #per bullet
BASE_MAGAZINE_SIZE = 30
BASE_FIRE_RATE = 2.0 #bullets per second
BASE_RELOAD_SPEED = 3.0 #seconds per reload

random.seed()
manufacturer = enums.Manufacturer(random.randint(1,5))
quality = enums.Quality(random.randint(1,5))

chome = Gun(BASE_BULLET_DAMAGE, BASE_MAGAZINE_SIZE, BASE_FIRE_RATE, BASE_RELOAD_SPEED, quality, manufacturer)

print ("Damage per bullet: ", chome.damage)
print ("Bullets per magazine: ", chome.magazine_size)
print ("Bullets fired per second: ", chome.fire_rate)
print ("Seconds per magazine change :", chome.reload_speed)
print ("Selected Manufacturer: ", chome.manufacturer)
print ("Selected Quality: ", chome.quality)