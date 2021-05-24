def afficher_status(status):
    code = {'morte': 1, 'vivante': 2, 'immune': 4}
    couleur_stat = 30 + code[status]
    return("\033[{}m\033[{}m{}\033[0m".format(couleur_stat, couleur_stat, " "))


def creation_grille(n):
    for j in range(n[1]):
        for i in range(n[2]):
            L = []
            L.append(i)
        ind = []
        ind.append(L)
    return(ind)



