# IMPORTS

from parametres import *
from creation_config import *

def parcours_cell (G):
    for i in range(len(G)):
        transition(G, i)

def transition (G, C):
    nb_contaminee = 0
    nb_immunisee = 0
    nb_saine = 0

    if G[C][1]["etat"] == "saine":
        for k in range(G[C][0][0]-1, G[C][0][0]+2):
            for l in range(G[C][0][1]-1, G[C][0][1]+2):
                for m in range(len(G)):
                    if G[m][0] == (k, l):
                        if G[m][1]["etat"] == "contaminee":
                            nb_contaminee = nb_contaminee +1
                            print(G[m])
    if G[C][1]["etat"] == "contaminee":
        G[C][1]["valeur"] = G[C][1]["valeur"] +1
        print("cellule contaminee: ", G[C][0])

        #if nb_contaminee != 0

transition(configuration_initial (v, n, p))


parcours_cell(configuration_initial (v, n, p))