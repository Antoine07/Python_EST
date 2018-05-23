import random as r

P = 10000
pois = []
proba = 0.5

for _ in range(P):
    genome = ''
    for _ in range(2):
        if r.random() < proba :
            genome += 'L'
        else:
            genome += 'r'

    pois.append(genome)

observation = {'lisse' : 0, 'ride' : 0} # L pour lisse r pour ridé

for np in pois:
    if np in {'Lr', 'rL', 'LL'}:
        observation['lisse'] += 1
    else:
        observation['ride']+=1

print(observation)
print("Proportion de lisse empirique {} et ridé : {}".format(observation['lisse'], observation['ride']))
print("Proportion théorique de lisse : {} et ridé : {}".format(10000*3/4., 10000*1/4.))