# PARAMETRES

def carre_rectangle (n):
    if n == "carre":
        c = int(input("valeur du coté: "))
        n = (c, c)
    elif n == "rectangle":
        h = int(input("hauteur de la grille: "))
        k = int(input("longueur de la grille: "))
        n = (h, k)
    return(n)

n = input("entrer 'carre' ou 'rectangle' en fonction de la forme de grille désirée: ")
while n != "carre" and n != "rectangle":
    n = input("entrer 'carre' ou 'rectangle' en fonction de la forme de grille désirée: ")

n = carre_rectangle(n)
print(n)

dense_C = int(input("densité de cellule contaminé initialement (%): "))
R = int(input("nombre d'individue contaminé par chaque malade: "))
t_maladie = int(input("durée de la maladie (jours): "))
taux_mortalite = float(input("probabilité de mourir de la maladie (%): "))

