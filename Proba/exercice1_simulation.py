import random as r

# simulation du lancé de dé
def simulation(m = 10000):
    simulate = {'1' : 0, '2' : 0, '3' : 0, '4' :0, '5' :0 , '6' :0}
    count = 0
    while count < m:
        d = r.random()
        if d < 1/6.:
            simulate['1'] += 1
        elif 1/6. < d < 2/6.:
            simulate['2'] += 1
        elif 2/6. < d < 3/6.:
            simulate['3'] += 1
        elif 3/6. < d < 4/6. :
            simulate['4'] += 1
        elif 4/6. < d < 5/6. :
            simulate['5'] += 1
        else:
            simulate['6'] += 1
        
        count += 1
    
    return list(map(lambda x: x/m, simulate.values()))


simulate =  simulation()

print(simulate)
print()
print(1/6)

def simulation2(N=10000):
    count = 0
    simulate = {'1' : 0, '2' : 0, '3' : 0, '4' :0, '5' :0 , '6' :0}    
    while count < N:
        d = r.randint(1,6)
        d = f"{d}" # d = "{}".format(d)
        simulate[d] += 1
        count += 1

    return simulate
    return list(map(lambda x: x/N, simulate.values()))

print(simulation())

print(1/6.)
