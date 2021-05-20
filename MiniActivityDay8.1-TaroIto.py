print("Problem #1")
import random
i = 0
brand = ("Channel Island's Flyer ", "Firewire's Cymatic 5'1", "Firewire's No Brainer", "Firewire's Sci-Fi 2.0", "Lost's Round Nose Fish", "Firewire's El Tomo Fish", "JS Industries' Monsta Box 2020", "JS Industries' Raging Bull", "Lost's Sword-Fish", "Firewire's Houdini", "Tokoro's Hiper", "Tokoro's Mojo")
while(i < 12):
    b = random.choice(brand)
    print(f"On the {i+1} day of Christmas my true love sent to me a {b} surfboard")
    i = i + 1


print("Problem #2")
num = [1, 2, 3, 4, 5, 7, 8, 12, 34, 56, 78, 130, 67, 888]
i = 0
sum = 0
while(i < len(num)):
    sum = sum + num[i]
    i = i + 1
print(sum)

# i = 0
# day = 1
# while (day < 13):
#     print (f"On the {day} of christmas, {brand[i]}")
#     day = day + 1
#     i = i + 1

