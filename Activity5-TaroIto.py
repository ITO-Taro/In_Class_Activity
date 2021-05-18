# tl = ("mac", 150, True, "iPhpone")
# print(tl)
import datetime
bd = datetime.date(1985, 3, 26)
print(bd)
tl1 = ("mac", 150, True, "iPhpone", bd)
print(tl1[-1])
print(tl1[3], tl1[-4])
from operator import itemgetter
print(*itemgetter(3, -4)(tl1))
print(len(tl1))
print(tl1)