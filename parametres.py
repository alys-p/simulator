# PARAMETRES

choix = str(input("vous avez 2 options : lancer la simulation "
                  "avec les paramètre de base en entrant 'base' ou bien accédé au paramètre en entrant 'parametres': "))

if choix == 'base':
    n = (13, 40)        # taille de la grille
    v = 90      # pourcentage de cellules vivantes
    p = 5       # pourcentage de cellules vivantes contaminées
    t_maladie = 3       # durée de la maladie
    t_immunitee = 5     # durée de l'immunitée
    taux_mortalite = 3      # taux de mortallité après contamination
    R = 100     # probabiltée qu'une cellule soit contaminé si l'une de ses voisines l'ai
    nb_tours = 25

if choix == 'parametres':
    choix = str(input("choisissez parmis les configuration suivante: 'explosif', 'classique' ou bien les re taper 'paramtres' pour "
                      "entrer chaque paramètre manuelement: "))
    if choix == 'explosif':
        n = (13, 40)
        v = 100
        p = 30
        t_maladie = 2
        t_immunitee = 2
        taux_mortalite = 50
        R = 10
        nb_tours = 10

    elif choix == 'classique':
        n = (13, 40)
        v = 80
        p = 25
        t_maladie = 2
        t_immunitee = 3
        taux_mortalite = 35
        R = 20
        nb_tours = 20

    elif choix == 'parametres':
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

