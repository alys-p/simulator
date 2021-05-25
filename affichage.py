def afficher_status(status): # what is a status?
    code = {'morte': 1, 'vivante': 2, 'immune': 4}
    couleur_stat = 30 + code[status]
    return("\033[{}m\033[{}m{}\033[0m".format(couleur_stat, couleur_stat, " "))


def creation_grille(n):
    for j in range(n[1]):
        for i in range(n[2]):   # n[2] doesn't exist i think you mean n[0] and n[1] also i thing this function is useless, i did
            L = []              # this already in config initial but correct me if im wrong, im a bit lost rn.
            L.append("")
        ind = []
        ind.append(L)
    return(ind)

def definir_status():



