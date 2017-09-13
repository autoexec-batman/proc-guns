from gun import Gun
import random
import yaml
import helpers
      
makers = yaml.load(open("makers.yml"))
guntypes = yaml.load(open("guntypes.yml"))
qualities = yaml.load(open("qualities.yml"))

manufacturer = random.choice(makers)
guntype = random.choice(guntypes)
quality = helpers.weighted_choice(qualities)

chome = Gun(guntype, manufacturer, quality)

nice_damage = chome.damage + (chome.damage * chome.nice_multiplier)
expected_damage = (chome.damage * (1 - chome.nice_chance)) + (nice_damage * chome.nice_chance)
time_to_magdump = chome.magazine_size / chome.fire_rate
damage_per_mag = expected_damage * chome.magazine_size
DPS_per_mag = damage_per_mag / time_to_magdump

print ("")
print (chome.display_name)
print ("Manufacturer: ", chome.manufacturer['name'])
print ("Damage per bullet: ", chome.damage)
print ("Bullets per magazine: ", chome.magazine_size)
print ("Bullets fired per second: ", chome.fire_rate)
print ("Seconds per magazine change :", chome.reload_time)
print ("Chance of Nice! shot: ", chome.nice_chance)
print ("Nice! shot damage multiplier: ", chome.nice_multiplier)
print ("Nice! shot damage: ", nice_damage)
print ("")
print ("Average damage per shot: ", expected_damage)
print ("Average damage per magazine: ", damage_per_mag)
print ("Seconds to magdump: ", time_to_magdump)
print ("Average DPS per magdump: ", DPS_per_mag)
print ("")
print (chome.gun_affixes)
