# IMPORTS

from parametres import *
from creation_config import *

def transition (G):
    nb_contaminee = 0
    nb_immunisee = 0
    nb_saine = 0
    for i in range(len(G)):
        if G[i][1]["etat"] == "saine":
            for k in range(G[i][0][0] -1, G[i][0][0] +2):
                for l in range(G[i][0][1] -1, G[i][0][1] +2):
                    for m in range(len(G)):
                        if G[m][0] == (k, l):
                            if G[m][1]["etat"] == "contaminee":
                                nb_contaminee = nb_contaminee +1
                                print("nb", nb_contaminee)
        nb_contaminee = 0

        #if nb_contaminee != 0

transition(configuration_initial (v, n, p))

