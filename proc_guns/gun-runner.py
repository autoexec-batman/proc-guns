from gun import Gun
import random
import enums

random.seed()
manufacturer = enums.Manufacturer(random.randint(1,5))
quality = enums.Quality(random.randint(1,5))

chome = Gun()

print ("Damage per bullet: ", chome.damage)
print ("Bullets per magazine: ", chome.magazine_size)
print ("Bullets fired per second: ", chome.fire_rate)
print ("Seconds per magazine change :", chome.reload_speed)
print ("Selected Manufacturer: ", manufacturer)
print ("Selected Quality: ", quality)