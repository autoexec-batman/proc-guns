from gun import Gun
import random
import yaml

makers = yaml.load(open("makers.yml"))
guntypes = yaml.load(open("guntypes.yml"))
qualities = yaml.load(open("qualities.yml"))

manufacturer = random.choice(makers)
guntype = random.choice(guntypes)
quality = random.choice(qualities)

chome = Gun(guntype, manufacturer, quality)
display_name = "{0} {1} {2}".format((chome.manufacturer['qualities'][chome.quality["tier"]]), chome.manufacturer["name"], chome.guntype["name"])

print (display_name)
print ("Damage per bullet: ", chome.damage)
print ("Bullets per magazine: ", chome.magazine_size)
print ("Bullets fired per second: ", chome.fire_rate)
print ("Seconds per magazine change :", chome.reload_time)
