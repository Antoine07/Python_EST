import random as r
import itertools as iter 

# simulation du lancé de dé
def simulation(m = 10000):
    count = 0
    N = 0 # nombre de combinaison 
    permutation = list(iter.permutations('142',3)) # permutation
    while count < m:
        hits = 3 # trois lancers
        res = []
        while hits > 0 :
            d = r.random()
            if d < 1/6.:
                number = '1'
            elif 1/6. < d < 2/6.:
                number = '2'
            elif 2/6. < d < 3/6.:
                number = '3'
            elif 3/6. < d < 4/6.:
                number = '4'
            elif 4/6. < d < 5/6.:
                number = '5'
            else:
                number = '6'

            res.append(number)
            hits -=1

        if tuple(res) in permutation:
            N += 1
        
        count += 1
    
    return N/m

simulate = simulation()

print(simulate)

P = 10000
permut421 = list( iter.permutations('142',3) )
number421 = 0
for _ in range(P):
  
  d = ( str(r.randint(1,6)), str(r.randint(1,6)), str(r.randint(1,6)) )		
	
  if d in permut421:
    number421 +=1
    
print(number421)
print(number421/P)

print(1/36.)