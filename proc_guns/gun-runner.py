from gun import Gun
import random
import enums
import yaml

BASE_BULLET_DAMAGE = 10 #per bullet
BASE_MAGAZINE_SIZE = 30
BASE_FIRE_RATE = 2.0 #bullets per second
BASE_RELOAD_TIME = 3.0 #seconds per reload

makers = yaml.load(open("makers.yml"))

manufacturer = random.choice(makers)
quality_id = random.choice(list(enums.Quality)).name

chome = Gun(BASE_BULLET_DAMAGE, BASE_MAGAZINE_SIZE, BASE_FIRE_RATE, BASE_RELOAD_TIME, manufacturer)

print ("Selected Manufacturer: ", chome.manufacturer["name"])
print ("Selected Quality: ", chome.manufacturer["qualities"][quality_id])
print ("Damage per bullet: ", chome.damage)
print ("Bullets per magazine: ", chome.magazine_size)
print ("Bullets fired per second: ", chome.fire_rate)
print ("Seconds per magazine change :", chome.reload_time)
