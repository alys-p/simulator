# IMPORT
from parametres import *
import random
import pprint

# CREATION DE LA GRILLE DE BASE

def configuration_initial (v, n):
    G = []
    print(v)
    for i in range(0, n[0]):
        for j in range(0, n[1]):
            dico_cell = {}
            C = [(i, j), dico_cell]
            dico_cell["etat"] = "morte"
            dico_cell["valeur"] = 2
            print(C)
            G.append(C)
    m = 0
    while m <= ((n[0]*n[1]*(v/100))-1):
        valeur_random = random.randint(0, n[0]*n[1]-1)
        if G[valeur_random][1]["etat"] == "morte":
            G[valeur_random][1]["etat"] = "vivante"
            m = m +1
    return G

pprint.pprint(configuration_initial(v, n))

