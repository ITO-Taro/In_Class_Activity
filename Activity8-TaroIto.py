# write a program to check the greatest among 3 numbers
# write a prigram to imitate a traffic light. Think about the information you need to generater to make your program mimnic the real world

# 1. Find the greatest number

a = 8
b = 52
c = 100
 
if (a>b and a>c):
    print("a is the greatest number")
elif (b>a and b>c):
    print("b is the greatest number")
elif (c>b and c>a):
    print ("c is the greatest number")
else:
    print("have not learned how to address these yet")


# 2. Imitate a traffic light
import random
color = ("red", "yellow", "green", "greenArrowLeft", "redArrowRight")
lc = random.choice(color)
def light(color):
    return random.choice(color)    
if (light(color)=="red"):
    print("STOP")
elif(light(color)=="yellow"):
    print("Slow Down")
elif(light(color)=="greenArrowLeft"):
    print("Clear to Turn Left")
elif (light(color)=="redArrowLRight"):
    print("No Right Turn on Red")
else:
    print("Clear to Proceed")
