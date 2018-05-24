from random import *

values = {'7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As'}
colors = {'carreau', 'coeur', 'pique', 'trefle'}
game = [v + ' de ' + c for v in values for c in colors]

# mélanger avec shuffle
shuffle(game)

# Le jeu 
# print(game) # pour vérifier que vous avez bien mélanger le jeu

count = 0
while True:
    # on tire au hasard dans un jeu déjà mélanger ça rajoute du suspend
    choice = int(random() * (32))
    count +=1
    if "As" in game[choice]:
        print(f"Vous avez gagné en {count} coup(s), en trouvant l'{game[choice]}")
        break