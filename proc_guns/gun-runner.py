from gun import Gun
import random
import enums
import yaml

BASE_BULLET_DAMAGE = 10 #per bullet
BASE_MAGAZINE_SIZE = 30
BASE_FIRE_RATE = 2.0 #bullets per second
BASE_RELOAD_SPEED = 3.0 #seconds per reload

makers = yaml.load(open("makers.yml"))

random.seed()
manufacturer_id = (random.randint(0,len(makers) -1))
manufacturer = makers[manufacturer_id]
quality_id = enums.Quality(random.randint(1,5)).name
quality = makers[manufacturer_id]['qualities'][quality_id]

chome = Gun(BASE_BULLET_DAMAGE, BASE_MAGAZINE_SIZE, BASE_FIRE_RATE, BASE_RELOAD_SPEED, quality, manufacturer)

print ("Damage per bullet: ", chome.damage)
print ("Bullets per magazine: ", chome.magazine_size)
print ("Bullets fired per second: ", chome.fire_rate)
print ("Seconds per magazine change :", chome.reload_speed)
print ("Selected Manufacturer: ", chome.manufacturer["name"])
print ("Selected Quality: ", chome.quality)