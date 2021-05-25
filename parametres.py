# PARAMETRES

longueur = int(input("Entrer la longueur de la grille: "))
largeur = int(input("Entrer la largeur de la grille: "))
n = (longueur, largeur)     # tuple des dimensions de la grille

print(n)

v = int(input("densité de cellule vivante initialement (%): "))     # on concidère qu'une cellule fait 1 par 1 et donc il y a dans une
                                                                    # cellule un maximum de n[0]*n[1] cellule. Ici on demenade juste
                                                                    # le pourcentage du maximum de cellule possible est vivante.

p = int(input("densité de cellule comtaminées initialement (%): "))     # même idée qu'au dessus mais ici il s'agit du pourcentatage des
                                                                    # cellules vivante qui sont contaminé à l'origine.

R = int(input("nombre d'individue contaminé par chaque malade: "))      # nombre d'individue contaminées dans le vosinage de la cellule
                                                                        # soit en général dans un visinage de 8
t_maladie = int(input("durée de la maladie (jours): "))
taux_mortalite = float(input("probabilité de mourir de la maladie (%): "))

