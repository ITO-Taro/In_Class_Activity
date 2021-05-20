print("Problem #1")
import random
i = 1
brand = (" ", "Channel Island's Flyer ", "Firewire's Cymatic 5'1", "Firewire's No Brainer", "Firewire's Sci-Fi 2.0", "Lost's Round Nose Fish", "Firewire's El Tomo Fish", "JS Industries' Monsta Box 2020", "JS Industries' Raging Bull", "Lost's Sword-Fish", "Firewire's Houdini", "Tokoro's Hiper", "Tokoro's Mojo" )
# b = random.choice(brand)
for i in range (1, 13):
    b = random.choice(brand)
    print(f"On the {i} day of Christmas my true love sent to me a {brand[i]} surfboard")
    i = i + 1

print("Problem #2")
num = 0
for x in range(1, 26):
    num = num + x
print(num)
