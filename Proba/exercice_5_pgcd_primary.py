import random as r

# Fonction permettant de calculer le pgcd de deux nombres
def pgcd(a,b):

    # on réordonne les paramètres si besoin
    if b > a:
        a, b = b, a

    if a % b == 0:
        return b 
    else: 
        return pgcd(b, a%b)

print(pgcd(42, 15))

def nb_primary(n):
    i = 0
    number_primary = 0

    for _ in range(N):
        a = r.randint(1,n)
        b = r.randint(1,n)

        if pgcd(a,b) == 1:
            number_primary += 1

    return number_primary

# cette probabilité tend quand n tend vers l'infini vers 6/pi^2
n, N = 100000, 100000

print(nb_primary(n)/n)