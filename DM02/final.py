"""
Nom: JACOBE
Prénom: Siffrein
Classe: TSI2
Fait sur Visual Studio Code avec Python 3.8.6 64 bits dans un environnement virtuel pipenv
"""
import os
import csv
from timeit import default_timer as timer  # time.clock est obsolète depuis Python 3.3 (sorti en 2012)

from matplotlib.image import imread
import matplotlib.pyplot as plt
import numpy as np

os.chdir(r"C:\Users\Siffrein JACOBE\Documents\Coding\TSI2_info\DM02")

img1 = imread("im1.png")
img1s = imread("im1_s.png")

img2 = imread("im2.png")
img2s = imread("im2_s.png")


# QUESTION 1
def somme(im):
    s = 0
    for ligne in im:
        for pixel in ligne:
            s += pixel
    return s
    # return np.sum(im)


# QUESTION 2
def cherche_centre1(im):
    s = somme(im)
    x_g = y_g = 0

    for i, ligne in enumerate(im):
        for j, p in enumerate(ligne):
            x_g += p * j
            y_g += p * i

    return (x_g / s, y_g / s)


# QUESTION 3 & 4
"""
Avec cet algorithme,
le barycentre de l'image 1 est trouvé en 1.4582469000000002s
et celui de l'image 2 en 1.2419331999999992s.
"""


# QUESTION 5
def cherche_centre2(im):
    s = somme(im)
    x_g = y_g = 0

    for i, ligne in enumerate(im):
        for j, p in enumerate(ligne):
            if p == 1:
                x_g += j
                y_g += i

    return (x_g / s, y_g / s)


# QUESTION 6 & 7
"""
Avec cet algorithme, le barycentre de l'image 1 est trouvé en 0.5699740000000002s et celui de l'image 2 en 0.5845333000000004s.
Il est donc approximativement 2x plus rapide que le précédent.
Ainsi l'utilisation d'une condition plutôt qu'une multiplication ici est plus performant.

Note : Cela n'est pas toujours vrai. Dans les langages de bas niveau, il est souvent préférable d'utiliser des opérations arithmétiques plutôt que des branches (conditions, ...). Une pratique d'optimisation appelée branchless programming :)
"""


# QUESTION 8
def cree_SL(im):
    return [np.sum(ligne) for ligne in im]


def cree_SC(im):
    return [np.sum(im[:, j]) for j in range(im.shape[1])]


# QUESTION 9
# Pour être compatible avec une future fonction, le paramètre seuil est optionnel de valeur par défaut 2
def cherche_centre3(im, seuil=2):
    SL = cree_SL(im)
    SC = cree_SC(im)

    # A l'aide de Numpy, on cherche le premier élément supérieur à seuil dans la liste SL et SC
    limHaute = np.argwhere(np.array(SL) >= seuil)[0][0]
    limGauche = np.argwhere(np.array(SC) >= seuil)[0][0]

    # Après avoir les avoir inverser, on cherche le premier élément dans ces listes supérieur à seuil. On calcule ensuite l'index original pour avoir la limite basse et droite.
    limBasse = len(SL) - np.argwhere(np.array(SL[::-1]) >= seuil)[0][0]
    limDroite = len(SC) - np.argwhere(np.array(SC[::-1]) >= seuil)[0][0]

    x_g = (limGauche + limDroite) / 2
    y_g = (limHaute + limBasse) / 2
    return x_g, y_g


# QUESTION 10 & 11
"""
Avec cet algorithme, le barycentre de l'image 1 est trouvé en 0.031034999999999258s et celui de l'image 2 en 0.020765300000000764s.
Bien que très rapide (presque 20x plus rapide que le précédent), cet algorithme a un défaut majeur: le barycentre de la 2nd image est mal placé à cause des faux positifs du seuillage.
Ainsi il n'est à couplé qu'à un seuillage performant.
"""


# QUESTION 12
def cherche_centre4(im):
    h = im.shape[0]  # Hauteur de l'image
    l = im.shape[1]  # Largeur de l'image

    sL = np.sum(im, 0)  # Liste de la somme des éléments de chaque colonne
    nC = np.arange(l)  # Subdivision avec l points : liste des index des colonnes
    pos_p_x = sL * nC  # Positions pondérés

    sC = np.sum(im, 1)  # Liste de la somme des éléments de chaque ligne
    nL = np.arange(h)  # Subdivisions avec h points : liste des index des lignes
    pos_p_y = sC * nL  # Positions pondérés
    s = np.sum(sL, 0)  # Somme de tous les éléments de la matrice image

    if s > 0:  # Si la somme est non nulle (il y a des pixels blancs)
        xg = np.sum(pos_p_x, 0) / s  # On calcule xg
        yg = np.sum(pos_p_y, 0) / s  # et yg
    else:  # Sinon (il n'y a aucun pixel)
        xg = l / 2  # Le barycentre est le centre de l'image parce qu'il faut bien le définir quelque part
        yg = h / 2

    return xg, yg  # On retourne les valeurs calculées
    # Le principe est d'exploiter les propriétés de multiplications de tableaux numpy ainsi que les autres fonctions proposées par le module pour calculer le barycentre.
    # Cet algorithme diffère des autres car la plupart des calculs sont laissés à numpy et qu'aucune boucle n'est utilisée.


# QUESTION 13
"""
Le grand gagnant de ces algorithmes, il présente des temps d'exécution quasiment 3000x plus rapide que le premier algorithme. Enorme !
"""


# QUESTION 14
def benchmark(imS, cherche_centre, motif, numeroAlgo, numeroImage):
    t = timer()  # time.clock est obsolète depuis python 3.3 sorti en 2012
    x_g, y_g = cherche_centre(imS)  # Pas d'erreurs car toutes les fonctions "cherche_centreN" ont le même nombre d'arguments obligatoires grâce à la modif de cherche_centre3
    delta_t = timer() - t

    print(f"[Algo {numeroAlgo}] Barycentre trouvé en {delta_t}s aux coordonnées ({x_g};{y_g}).")

    plt.imshow(imS, cmap="gray")
    plt.title(f"Image {numeroImage}")
    plt.plot([x_g], [y_g], motif)

    return delta_t, x_g, y_g


print("IMAGE 1")
im1algo1 = benchmark(img1s, cherche_centre1, "bs", 1, 1)
im1algo2 = benchmark(img1s, cherche_centre2, "bs", 2, 1)
im1algo3 = benchmark(img1s, cherche_centre3, "ro", 3, 1)
im1algo4 = benchmark(img1s, cherche_centre4, "g^", 4, 1)
plt.show()

print("IMAGE 2")
im2algo1 = benchmark(img2s, cherche_centre1, "bs", 1, 2)
im2algo2 = benchmark(img2s, cherche_centre2, "bs", 2, 2)
im2algo3 = benchmark(img2s, cherche_centre3, "ro", 3, 2)
im2algo4 = benchmark(img2s, cherche_centre4, "g^", 4, 2)
plt.show()


with open("resultats1.csv", "w", newline="") as res1:
    writer1 = csv.writer(res1, delimiter=";", lineterminator="\n")
    writer1.writerows([
        ["Nom de l'algorithme", "Temps d'exécution", "Xg (pixels)", "Yg (pixels)"],
        ["Cherche_centre_1", *im1algo1],
        ["Cherche_centre_2", *im1algo2],
        ["Cherche_centre_3", *im1algo3],
        ["Cherche_centre_4", *im1algo4]
    ])

with open("resultats2.csv", "w", newline="") as res2:
    writer2 = csv.writer(res2, delimiter=";", lineterminator="\n")
    writer2.writerows([
        ["Nom de l'algorithme", "Temps d'exécution", "Xg (pixels)", "Yg (pixels)"],
        ["Cherche_centre_1", *im2algo1],
        ["Cherche_centre_2", *im2algo2],
        ["Cherche_centre_3", *im2algo3],
        ["Cherche_centre_4", *im2algo4]
    ])
