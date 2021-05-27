# IMPORT

from parametres import *
import random
import pprint # juste pour un print plus jolie et repérer facilement les erreurs potentielles

# CREATION DE LA GRILLE DE BASE

def configuration_initial (v, n, p):
    """
    :param n: dimension de la grille (tuple) pour determiner l'espace et donc le nombre de cellules vivante possible.
    :param v: pourcentage de cellules vivante par rapport au maximum d'espace (n[0]*n[1])
    :param p: pourcentage de cellules contaminé dans les cellules vivantes
    :return: la grille G complète et prète pour démarer la simulation avec un tuple de position et un dico pour chaque cellule
    """

    G = []  # création de la grille et remplissage progressif
    for i in range(0, n[0]):
        for j in range(0, n[1]):
            dico_cell = {}
            C = [(i, j), dico_cell]
            dico_cell["etat"] = "morte"
            dico_cell["valeur"] = 0
            G.append(C)
    m = 0       # variable d'incrémentation parceque c'est un while donc pas il y a pas d'incrémentation de 1 automatique
    L = []
    while m <= ((n[0]*n[1]*(v/100))-1):
        valeur_random = random.randint(0, n[0]*n[1]-1)
        if G[valeur_random][1]["etat"] == "morte":      # verification que la cellue est bien morte pour en avoir le bon nombre
            G[valeur_random][1]["etat"] = "saine"     # de vivante and pa un cellule attribué vivante 2 fois ou plus
            L.append(valeur_random)
            m = m +1
    o = 0       # variable d'incrémentation parceque c'est un while donc pas il y a pas d'incrémentation de 1 automatique
    while o <= ((m*(p/100))-1):
        valeur_random_2 = random.choice(L)
        G[valeur_random_2][1]["etat"] = "contaminee"
        o = o +1
    return G

pprint.pprint(configuration_initial(v, n, p))

