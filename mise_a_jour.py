# IMPORTS

from parametres import *
from creation_config import *
import random


def parcours_cell(G):
    """
    Permet juste d'alléger la fonction transition et de répéter cette dernière le nombre de fois qu'il y a de cellules.
    :param G: Grille
    :return: rien il s'agit aussi d'une procédure
    """
    for i in range(len(G)):
        transition(G, i, R)


def transition(G, C, R):
    """
    :param G: Grille
    :param C: Cellule dont on regarde l'environment
    :return: aucun il s'agit d'une procédure
    """
    nb_contaminee = 0

    if G[C][1][
        "etat"] == "saine":  # parcourir l'environment d'une cellule pour compter le nombre de cellule voisine
        # contaminées
        for k in range(G[C][0][0] - 1, G[C][0][0] + 2):  # parcour de l'enironemet de la cellule
            for l in range(G[C][0][1] - 1, G[C][0][1] + 2):
                for m in range(len(G)):
                    if G[m][0] == (
                    k, l):  # recherche les voisines dans la liste pour accédé a leur dictionaire et donc savoir si
                        # elle sont contaminées.
                        if G[m][1]["etat"] == "contaminee":
                            nb_contaminee = nb_contaminee + 1

        if nb_contaminee == 1:  # application simple du pourcentage de chance de contamination
            valeur_random = random.randint(0, 100)
            if valeur_random > R:
                G[C][1]["etat"] = "contaminee"
        if nb_contaminee > 1:  # cas plus complex ou plus il y a de cellules plus la probabilitée de contamination
            # augmente.
            R = 1 - (1 - R) ** nb_contaminee
            valeur_random = random.randint(0, 100)
            if valeur_random > R:
                G[C][1]["etat"] = "contaminee"

    if G[C][1]["etat"] == "contaminee":
        if G[C][1]["valeur"] == t_maladie - 1:      # mettre fin a la contamination lorsque le compteur atteint une
            # valeur fixer de durée de la maladie (t_maladie)
            valeur_random = random.randint(0, 100)
            if valeur_random >= taux_mortalite:     # pourcentage de survit
                G[C][1]["etat"] = "immunisee"
                G[C][1]["valeur"] = 0
            else:
                G[C][1]["etat"] = "decedee"     # pourcentage de déces
                G[C][1]["valeur"] = 0
        else:
            G[C][1]["valeur"] = G[C][1]["valeur"] + 1       # compteur du temps que la cellule a passé contaminée

    if G[C][1]["etat"] == "immunisee":
        if G[C][1]["valeur"] == t_immunitee - 1:        # mettre fin a l'immunitée d'une cellule après qu'elle est
            # dépassé une certaine valeur avec le même système que pour la contamination.
            G[C][1]["etat"] = "saine"
            G[C][1]["valeur"] = 0
        else:
            G[C][1]["valeur"] = G[C][1]["valeur"] + 1       # compteur du temps que la cellule a passé immunisée
