
populations = [
    { "id" : 0, "name" : "Alan" },
    { "id" : 1, "name" : "Albert" },
    { "id" : 2, "name" : "Jhon" },
    { "id" : 3, "name" : "Brice" },
    { "id" : 4, "name" : "Alexendra" },
    { "id" : 5, "name" : "Brad" },
    { "id" : 6, "name" : "Carl" },
    { "id" : 7, "name" : "Dallas" },
    { "id" : 8, "name" : "Dennis" },
    { "id" : 9, "name" : "Edgar" },
    { "id" : 10, "name" : "Erika" },
    { "id" : 11, "name" : "Isaac" },
    { "id" : 12, "name" : "Ian" }
]

"""
les relations entre les personnes de la population les tuples correspondent aux 
coordonnées de la matrice population et indique les relations entre les individus
"""
relationships = [
    (0,1), (0,2), (1,2), (1,4),(2,3), (2,5),
    (3,4), (3,7), (4,5),(4,8), (4,9), (5,7),
    (5,9), (6,7), (6,8), (7,1), (7,8), (8,9),
    (10,1),(10,2),(10,3),(11,12),(11,2),(11,5)
]

# on ajoute une clé à la liste
for user in populations:
    user['relation'] = []

# print(populations)

"""
Ajouter les relations dans la liste populations PARTIE 1
"""
for i, j in relationships:
    populations[i]['relation'].append(populations[j])
    # réciproquement j a pour relation i
    populations[j]['relation'].append(populations[i])

# print(len(populations))

print(f"relation de 0 : {len(populations[0]['relation']) }" )

"""
Calculer la moyenne des relations entre les individus de cette population PARTIE 2
"""

# Calculer le nombre moyen de relation
def number_relation_user(user):
    return len(user['relation'])

total_relation = sum(number_relation_user(user) for user in populations)

# print(total_relation)

avg_relation = total_relation/len(populations)

print(avg_relation)

"""
Représenter une liste des users et de leurs nombre de relation PARTIE 3
""" 

relation_user_id = [(user['id'], number_relation_user(user) ) for user in populations]
relation_user_id.sort(key=lambda student: student[1], reverse=True)

"""
Chaque utilisateur du tableau population a des relations, trouvez les amis des amis de ces relations 
pour un utilisateur donné
"""

def relation_of_relation(user):
    return [(user['id'], r['id'], fof['id']) for r in user['relation'] for fof in r['relation']]

print(relation_of_relation(populations[0]))

print('--------------end')