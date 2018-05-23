import random as r 

res = [(x,y) for x in range(1,7) for y in range(1,7) if x + y == 6]

print(res)
N = 10000
pA = 0
for _ in range(N):
    x = r.randint(1,6)
    y = r.randint(1,6)

    if (x,y) in res:
        pA += 1

print(pA/N)

print(5/36.)