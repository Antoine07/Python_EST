import math as m 
import random as r 
import numpy as np

def binomiale(n, p):
    sum = 0
    # simulation de 30 lancés 
    for k in range(n):
        sum += np.floor(r.random()+p) # partie entière supérieur

    return sum

n, p = 30, (5/30.)
N = 200000

simulateBinomial = [ binomiale(n,p) for _ in range(N)]
frequences = [ (simulateBinomial.count(k)/N) for k in range(n+1) ]

print(frequences)

# comparaison avec la loi de poisson 

poisson = []
u = np.exp(-5)
poisson.append(u)

for k in range(1, n+1):
    u = u*5/k 
    poisson.append(u)

print(poisson)

# mesure de l'écart des fréquence entre les deux lois 

deviation = 0 

for k in range(n+1):
    deviation += np.abs(frequences[k] - poisson[k])

print(deviation/31)