import affichage
from creation_config import *
from parametres import *
from mise_a_jour import *

G = configuration_initial(v, n, p)
affichage.afficher_grille(G)
parcours_cell(G)
