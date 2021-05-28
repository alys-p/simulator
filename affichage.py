def definir_couleur(etat):
    code = {'decedee': 0, 'saine': 7, 'immunisee': 2, 'contaminee': 1}
    couleur_stat = 30 + code[etat]
    return "\033[{}m\033[{}m{}\033[0m".format(couleur_stat, couleur_stat + 10, " ")


def definir_etat(G):
    couleur = []

    for i in range(len(G)):
        if G[i][1]['etat'] == 'decedee':
            G[i][1]['couleur'] = definir_couleur('decedee')
        elif G[i][1]['etat'] == 'saine':
            G[i][1]['couleur'] = definir_couleur('saine')
        elif G[i][1]['etat'] == 'contaminee':
            G[i][1]['couleur'] = definir_couleur('contaminee')
        else:
            G[i][1]['couleur'] = definir_couleur('immunisee')
    return G


def afficher_grille(G):
    G = definir_etat(G)
    for i in range (len(G)):
        print(G[i])
    for i in range(len(G)):
        if G[i][0][1] == 0:
            print()
            print(G[i][1]['couleur'], end='')
        else:
            print(G[i][1]['couleur'], end='')
