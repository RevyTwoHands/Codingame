import sys
import math


def dist(lonB, lonA, latB, latA):
    x = (lonB - lonA) * math.cos((latA + latB)/2)
    y = latB - latA
    return math.sqrt(x**2 + y**2)*6371

to_float = lambda x: float(x.replace(',', '.'))

lonA = to_float(input())
latA = to_float(input())

dmin = math.inf
defname = ''

n = int(input())
for i in range(n):
    defib = input().split(';')
    lonB = to_float(defib[4])
    latB = to_float(defib[5])

    d = dist(lonB, lonA, latB, latA)
    if d < dmin:
        dmin = d
        defname = defib[1]


print(defname)
