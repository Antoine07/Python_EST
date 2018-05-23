import random as r 

both_girls = 0 # les deux sont des filles
older_girl = 0 # l'aîné est une fille
either_girl = 0 # au moins l'un des deux est une fille

"""
1 ) L'enfant aîné est une fille. Quelle est la probabilité que les deux enfants soient des filles ?
2)  Au moins l'un des deux est une fille. Quelle est la probabilité que les deux enfants soient des filles ?

Avec un tableau on aurait respectivement pour 1) et 2)
sachant BG GG donc une chance sur 2 : 1/2
sachant BG GG GB et donc : 1/3

Moralité : 
si on sait que au moins un des deux est une fille alors on a deux fois plus de chance que le deuxième enfant soit un garçon.
"""

def generate_kids():
    return r.choice(['boy', 'girl'])

for _ in range(10000):
    younger = generate_kids()
    older = generate_kids()

    if older == "girl":
        older_girl += 1
    if older == "girl" and younger=="girl":
        both_girls += 1
    if older == "girl" or younger == "girl":
        either_girl += 1

print("P(both | older )", both_girls/older_girl ) # proba 1/2
print("P(both | either)", both_girls/either_girl ) # proba 1/3