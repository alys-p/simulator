def definir_couleur(etat):
    code = {'morte': 0, 'vivante': 7, 'immune': 2, 'contaminee': 1}
    couleur_stat = 30 + code[etat]
    return ("\033[{}m\033[{}m{}\033[0m".format(couleur_stat, couleur_stat+10, " "))


def definir_etat(G):
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
    y = definir_etat(G)
    for i in range(len(y)):
        for j in range(len(y[i])):
            print(y[i][j][1], end='')
        print()

def afficher_configuration():
    afficher_grille