"""
Une planche de Galton est un dispositif 
inventé par Sir Francis Galton qui illustre 
la convergence d'une loi binomiale vers une loi normale.

"""
from random import *
import matplotlib.pyplot as plt

LEVEL = 10
NUMBER_BALLS = 5000

def ball():
    route = ''
    for _ in range(LEVEL):
        if random() < 0.5:
            route += 'L'
        else:
            route += 'R'

    return route


"""
Pour simuler le parcours l'algo est le suivant si on part à gauche au premier tour alors on ne pourra plus 
être dans le réservoir totalemnt à droite. Ainsi de suite, si on repart maintenant à droite on ne pourra plus 
être dans le réservoir totalement à gauche, etc.

"""

def throw_ball():
    target = [0] * LEVEL
    route = ball()
    tanks = [n for n in range(LEVEL + 1)]

    for d in route:
        if d == 'L':
            tanks.pop()
        else:
            tanks.pop(0)

    return tanks[0]


# print(throw_ball())


def simulate(number):
    heaps = [0] * (LEVEL + 1)
    for _ in range(number):
        heaps[throw_ball()] += 1

    return heaps

""" 
représentation graphique avec matplotlib
"""

bornes = [n for n in range(LEVEL+1)]

print(simulate(50000))
print(bornes)

plt.bar(bornes, simulate(5000))

plt.show()