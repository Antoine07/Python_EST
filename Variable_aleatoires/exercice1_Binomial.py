from random import *

def binomiale(n, p):
    x = 0
    for _ in range(n):
        if random() <= p: 
            x +=1 
    return x

n, p= 5,0.3

simulate = [ binomiale(n,p) for _ in range(20000)]

emp =  simulate.count(3)/20000.
theo = 10*((0.3)**3)*(0.7)**2
print('P(X=3) = ',emp)
print('valeur théorique ',theo )

# estimation de l'erreur :

print('erreur {}'.format( abs(emp - theo) ))
