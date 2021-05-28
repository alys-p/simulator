from os import system, name
from time import sleep


def definir_couleur(etat):  # cette fonction permet de definir la couleur d'une case en fonction de l'état de la cellule

    code = {'decedee': 0, 'saine': 7, 'immunisee': 2, 'contaminee': 1}  # je crée un dictionaire a qui j'associe
    # un nombre en fonction de la couleur
    couleur_stat = 30 + code[etat]  # en ajoutant 30 au code couleur, j'obtient le nombre necessaire pour afficher
    # quelquechose en couleur

    return "\033[{}m\033[{}m{}\033[0m".format(couleur_stat, ' ', "✺")  # la fonction retourne ce qu'on doit print pour
    # obtenir une case de couleur


def definir_etat(G):  # cette fonction permet d'ajouter un attribut au dictionnaire de chaque cellule
    # qui correspondera a sa couleur

    for i in range(len(G)):  # pour accéder aux informations sur toutes les cellules il faut parcourir la liste G

        if G[i][1]['etat'] == 'decedee':  # avec ces conditions on peut ajouter un attribut couleur qui sera defini
            # dans le dictionnaire
            # grâce à la fonction definir_couleur et l'état de la cellule
            G[i][1]['couleur'] = definir_couleur('decedee')

        elif G[i][1]['etat'] == 'saine':
            G[i][1]['couleur'] = definir_couleur('saine')

        elif G[i][1]['etat'] == 'contaminee':
            G[i][1]['couleur'] = definir_couleur('contaminee')

        else:
            G[i][1]['couleur'] = definir_couleur('immunisee')

    return G  # cette fonction retourne la nouvelle liste pour qui les cellules ont un attribut couleur


def afficher_grille(G):  # cette fonction permet d'afficher la grille de cellules
    G = definir_etat(G)  # on defini d'abord la grille pour lui ajouter les attributs couleur

    for i in range(len(G)):  # on parcours la liste G pour accéder à toutes les cellules

        if G[i][0][1] == 0:  # G[i][0][1] est l'ordonnée de la cellule qui se trouve à la place i dans G.
            # or, si l'ordonnée est nul, cela veut dire qu'on a changer de ligne
            print()  # ainsi il faut passer à la ligne suivante
            print()
            print(G[i][1]['couleur'], ' ', end='')  # apres avoir changer de ligne, on imprime la cellule d'ordonnée 0
        else:
            print(G[i][1]['couleur'], ' ', end='')  # si on ne change pas de ligne, alors on imprime simplement
            # la cellule

    sleep(1)  # j'utilise sleep pour que l'affichage se fasse en decalé

    # après avoir afficher la grille, on efface la console pour afficher la grille suivante

    if name == 'nt':  # cette condition en fonction de l'ordinateur utilisé nous permet d'utilser la fonction necessaire
        _ = system('cls')  # cette instruction efface ce qui a été imprimé précèdamment
    else:
        _ = system('clear')
