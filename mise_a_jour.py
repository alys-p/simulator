# IMPORTS

from parametres import *
from creation_config import *

def transition (G):
    nb_contaminee = 0
    nb_immunisee = 0
    nb_saine = 0
    for i in range(len(G)):
        for x in range(G[i][0][0] -1, G[i][0][0] +2):
            for y in range(G[i][0][1] -1, G[i][0][1] +2):
                if x <= n[0] or x >= 0 or y <= n[1] or y >= 0:
                    if G[i][1]["etat"] == "immunisee":
                        nb_immunisee = nb_immunisee +1
                    if G[i][1]["etat"] == "contaminee":
                        nb_contaminee = nb_contaminee +1
                    if G[i][1]["etat"] == "saine":
                        nb_saine = nb_saine +1
                    print(nb_saine, nb_contaminee, nb_immunisee)
            print()
            print(x,y)
        nb_contaminee = 0

        #if nb_contaminee != 0

transition(configuration_initial (v, n, p))