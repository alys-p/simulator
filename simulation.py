import affichage
from creation_config import *
from parametres import *
from mise_a_jour import *
from time import sleep

def simulation():
    S = {'decedees': 0, 'contaminees': 0, 'gueries': 0, }
    G = configuration_initial(v, n, p)
    for i in range(nb_tours):
        print()
        affichage.afficher_grille(G)
        affichage.statistiques(G, S)
        print()
        print("cellules:")
        print("decedées:", S['decedees'], "  contaminées:", S['contaminees'],
            "  guerries:", S['gueries'], "  malades en ce moment:", S['malades'])
        sleep(1)  # j'utilise sleep pour que l'affichage se fasse en decalé
        print()
        print()
        parcours_cell(G)

    affichage.afficher_grille(G)
    affichage.statistiques(G, S)
    print()
    print("cellules:")
    print("decedées:", S['decedees'], "  contaminées:", S['contaminees'],
          "  guerries:", S['gueries'], "  malades en ce moment:", S['malades'])
    sleep(1)  # j'utilise sleep pour que l'affichage se fasse en decalé

simulation()
