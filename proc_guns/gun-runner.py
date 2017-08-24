from gun import Gun
import random
import enums
import yaml

BASE_BULLET_DAMAGE = 10 #per bullet
BASE_MAGAZINE_SIZE = 30
BASE_FIRE_RATE = 2.0 #bullets per second
BASE_RELOAD_TIME = 3.0 #seconds per reload

makers = yaml.load(open("makers.yml"))
guntypes = yaml.load(open("guntypes.yml"))

manufacturer = random.choice(makers)
guntype = random.choice(guntypes)
quality_id = random.choice(list(enums.Quality)).name

chome = Gun(guntype, manufacturer)
display_name = "{0} {1} {2}".format((chome.manufacturer["qualities"][quality_id]), chome.manufacturer["name"], chome.guntype["name"])

print (display_name)
print ("Damage per bullet: ", chome.damage)
print ("Bullets per magazine: ", chome.magazine_size)
print ("Bullets fired per second: ", chome.fire_rate)
print ("Seconds per magazine change :", chome.reload_time)
