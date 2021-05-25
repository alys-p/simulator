def definir_couleur(status):
    code = {'morte': 1, 'vivante': 2, 'immune': 4, 'contaminee': 5}
    couleur_stat = 30 + code[status]
    return("\033[{}m\033[{}m{}\033[0m".format(couleur_stat, couleur_stat, " "))

def definir_status(G):
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j][2]["etat" == "morte"






