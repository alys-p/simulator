def definir_couleur(etat):
    code = {'decedee': 0, 'saine': 7, 'immunisee': 2, 'contaminee': 1}
    couleur_stat = 30 + code[etat]
    return "\033[{}m\033[{}m{}\033[0m".format(couleur_stat, couleur_stat + 10, " ")


def definir_etat(G):
    y = []
    for i in range(G[-1][0][0]):
        x = []
        for j in range(len(G)//G[-1][0][0]):
            if G[j + i][1]['etat'] == "decedee":
                c = [(i, j), definir_couleur('decedee')]
                x.append(c)
            elif G[j + i][1]['etat'] == "saine":
                c = [(i, j), definir_couleur('saine')]
                x.append(c)
            elif G[j + i][1]['etat'] == "immunisee":
                c = [(i, j), definir_couleur('immunisee')]
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
