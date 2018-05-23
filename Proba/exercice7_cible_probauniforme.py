import math, random as r
from decimal import *
getcontext().prec = 6

ray = 2  # rayon du cercle

impacts = 0
N = 1000000


# fonction permettant de calculer la distance
def distance(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# On calcule maintenant les impacts à la cible
for _ in range(N):
    d = distance([0, 0], [r.randint(-10, 10), r.randint(-10, 10)])
    if d <= 2:
        impacts += 1

# puis on affiche l'estimation des impacts
print(impacts / N)

print((math.pi * 4) / 400)