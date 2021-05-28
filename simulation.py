import affichage
from creation_config import *
from parametres import *
from mise_a_jour import *

G = configuration_initial(v, n, p)

for i in range(nb_tours):
    print()
    affichage.afficher_grille(G)
    print()
    print()
    parcours_cell(G)

affichage.afficher_grille(G)
