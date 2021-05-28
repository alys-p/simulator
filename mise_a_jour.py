# IMPORTS

from parametres import *
from creation_config import *
import random


def parcours_cell(G):
    for i in range(len(G)):
        transition(G, i)


def transition(G, C):
    nb_contaminee = 0
    nb_immunisee = 0
    nb_saine = 0

    if G[C][1]["etat"] == "saine":
        for k in range(G[C][0][0] - 1, G[C][0][0] + 2):
            for l in range(G[C][0][1] - 1, G[C][0][1] + 2):
                for m in range(len(G)):
                    if G[m][0] == (k, l):
                        if G[m][1]["etat"] == "contaminee":
                            nb_contaminee = nb_contaminee + 1

        if nb_contaminee > R-1:
            G[C][1]["etat"] = "contaminee"

    if G[C][1]["valeur"] == t_maladie -1:
        if G[C][1]["etat"] == "contaminee":
            valeur_random = random.randint(0, 100)
            if valeur_random > taux_mortalite:
                G[C][1]["etat"] = "immunisee"
            else:
                G[C][1]["etat"] = "decedee"
                G[C][1]["valeur"] = 0

    if G[C][1]["etat"] == "contaminee":
        G[C][1]["valeur"] = G[C][1]["valeur"] + 1
