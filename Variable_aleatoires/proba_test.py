
from random import *
import numpy as np 
import pylab as pl

F = 100
malades = [n for n in range(1, F+1)]

POPULATION = 1000
M = 0 # personne non malade
T = 0 # 

nT = 0 # nombre de fois où le test est positif
nTM = 0 # représente le nombre de fois où le test est positif et la personne est malade
L = [] # fréquence des personnes malade sachant que leur test est positif 

population = list(range(1, POPULATION + 1))

shuffle(population)

malades = population[0:100]
accuMalades = []

for malade in malades:

    accuMalades.append(malade)

    for k in range(1, POPULATION + 1):
        choice = randint(0,POPULATION+1)

        if choice in accuMalades:
            M = 1 
            if random() < 0.01 :
                T = 2 
            else:
                T = 1 # test positif et personne malade
        else:
            M = 0
            if random() < 0.01 :
                T = 3 # test positif et personne non malade
            else:
                T = 4 # test négatif et personne non malade

        if T in [1,3]:
            nT += 1
        
        if T == 1:
            nTM += 1
    
    L.append(nTM/nT)


# bornes = np.arange(100)

# pl.plot(bornes, L)

# pl.show()

"""
Les faux positifs augment si la population f diminue

PT(Mbar) = (1 - f)/(1 + 98f)  lorsque f tend vers 0 alors cette proba tend vers 1 
ce qui pose problème ... Le test est donc à considérer en fonction de cette remarque
Si la maladie est rare alors le test est peu fiable 

"""

def f(x):
    return ((1-x)/(1+ 98*x) )

t = np.linspace(0, 100, 10000)

pl.plot(t, f(t))

pl.show()



