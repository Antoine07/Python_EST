import math as m 
import numpy as np 
import random as r

N = 10000
money =  [0, 30, 10]

def game():
    rand = r.random()
    if  rand <= 1/10. :
        return 30
    elif rand <= 3/10. :
        return 10
    else:
        return 0

simulate = [game() for _ in range(N)]

frequences = [simulate.count(k)/N for k in money]

print(frequences)

print( sum( k*simulate.count(k)/N for k in money ) )
