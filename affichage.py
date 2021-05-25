def definir_couleur(status):
    code = {'morte': 1, 'vivante': 2, 'immune': 4, 'contaminee': 5}
    couleur_stat = 30 + code[status]
    return ("\033[{}m\033[{}m{}\033[0m".format(couleur_stat, couleur_stat, " "))


def definir_status(G):
    y = []
    for i in range(len(G)):
        x = []
        for j in range(len(G[i])):

            if G[i][j][1]["etat"] == "morte":
                c = [(i, j), definir_couleur('morte')]
                x.append(c)
            elif G[i][j][1]["etat"] == "vivante":
                c = [(i, j), definir_couleur('vivante')]
                x.append(c)
            elif G[i][j][1]["etat"] == "immune":
                c = [(i, j), definir_couleur('immune')]
                x.append(c)
            else:
                c = [(i, j), definir_couleur('contaminee')]
                x.append(c)
        y.append(x)
    return y


def afficher_grille(G):
    y = definir_status(G)
    for i in range(len(y)):
        for j in range(len(y[i])):
            print(y[i][j][1], end='')
        print()