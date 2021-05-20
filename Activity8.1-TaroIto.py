# Create a function that takes in integers as parameters. Perform some operation that will compare these values and order the numbers from least to greatest.
# Return these values as a set in a tuple.
# Remember to check the data type of the value you are returning. Your function assumes that data type.

# Did this yesterday (18MAY2021) as self study 
num =[63, 45, 58, 1, 2, 7, 41, 108, 3, 89, 11, 1011]
def Math(x):
    return (tuple(sorted(x)))
if (type(Math(num)) == list):
    print(Math(num))
elif (type(Math(num)) == dict):
    print(Math(num))
elif (type(Math(num)) == str):
    print(Math(num))
else: print(Math(num), "is indeed Tuple")

# Today's (19MAY2021) work
a = 1
b = 0
c = 0
def func(x, y, z):
    if (x>y and x>z and y>z) or (x>y and y==z):
        return tuple((x, y, z))
    elif (x>y and x>z and z>y) or (x>y and x==z):
        return tuple((x, z, y))
    elif (y>x and x>z and y>z) or (y>x and x==z):
        return tuple((y, x, z))
    elif (y>x and x<z and y>z) or (y==z and y>x):
        return tuple((y, z, x))
    elif (z>x and y<z and y>x):
        return tuple((z, y, x))
    elif (z>x and z>y and x>y) or (z>x and x==y):
         return tuple((z, x, y))
    else:
        print("Inconclusive")
if (type(func(a, b, c) == tuple)):
    print (func(a, b, c), "is indedd a Tuple")


smallestNum = 0
middleNum = 0
biggestNum = 0
def sort3(l = 51, m = 50, n = 10101):
    
    if (l < m and l < n):
        smallestNum = l
    elif (m < l and m > n):
        biggestNum = l
    else:
        middleNum = l
    if (m < l and m < n):
        smallestNum = m
    elif (m > l and m > n):
        biggestNum = m
    else:
        middleNum = m
    if (n < l and n < m):
        smallestNum = n
    elif (n > l and n > m):
        biggestNum = n
    else:
        middleNum = n
    solution = (smallestNum, middleNum, biggestNum)
    print(solution)

print(sort3())

