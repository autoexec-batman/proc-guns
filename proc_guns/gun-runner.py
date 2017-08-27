from gun import Gun
import random
import yaml

def weighted_choice(list):
    weighted_list = []
    for weighted_item in list:
        for i in range(weighted_item["weight"]):
            weighted_list.append(weighted_item)
    #print (weighted_list)
    return random.choice(weighted_list)
    
    
makers = yaml.load(open("makers.yml"))
guntypes = yaml.load(open("guntypes.yml"))
qualities = yaml.load(open("qualities.yml"))

manufacturer = random.choice(makers)
guntype = random.choice(guntypes)
quality = weighted_choice(qualities)

chome = Gun(guntype, manufacturer, quality)
display_name = "{0} {1} {2}".format((chome.manufacturer['qualities'][chome.quality["name"]]), chome.manufacturer["name"], chome.guntype["name"])

print (display_name)
print ("Damage per bullet: ", chome.damage)
print ("Bullets per magazine: ", chome.magazine_size)
print ("Bullets fired per second: ", chome.fire_rate)
print ("Seconds per magazine change :", chome.reload_time)
