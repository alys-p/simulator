# PARAMETRES

longueur = int(input("Entrer la longueur de la grille: "))
largeur = int(input("Entrer la largeur de la grille: "))
n = (longueur, largeur)     # tuple des dimensions de la grille

print(n)

nb_tours = int(input("Entrer la durée de la simulation (jours): "))

v = int(input("densité de cellule vivante initialement (%): "))     # on concidère qu'une cellule fait 1 par 1 et donc il y a dans une
                                                                    # cellule un maximum de n[0]*n[1] cellule. Ici on demenade juste
                                                                    # le pourcentage du maximum de cellule possible est vivante.

p = int(input("densité de cellule comtaminées initialement (%): "))     # même idée qu'au dessus mais ici il s'agit du pourcentatage des
                                                                    # cellules vivante qui sont contaminé à l'origine.

t_maladie = int(input("durée de la maladie (jours): "))
t_immunitee = int(input("durée de l'immunitée (jours): "))
taux_mortalite = int(input("probabilité de mourir de la maladie (%): "))
R = int(input("probabilité qu'une cellule entouré d'une cellule contaminée soit contaminée: "))

