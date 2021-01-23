"""
DM des grandes vacances - Informatique
Siffrein JACOBE
TSI2
"""
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

os.chdir(r"C:\\Users\\Siffrein JACOBE\\Documents\\Coding\\tsi2\\DM_aout")


img1 = mpimg.imread("im1.png")
img2 = mpimg.imread("im2.png")


# QUESTION 1
seuilsRGB = [0.5, 1, 0, 1, 0, 1]


# QUESTION 2
def seuillage_pixel(p, seuil):
    if (seuil[0] <= p[0] <= seuil[1]
            and seuil[2] <= p[1] <= seuil[3]
            and seuil[4] <= p[2] <= seuil[5]):
        return [1, 1, 1]
    return [0, 0, 0]


# QUESTION 3
def seuillage(im, seuil):
    im_seuillee = np.zeros_like(im)

    for i_ligne, ligne in enumerate(im):
        for i_colonne, pixel in enumerate(ligne):
            im_seuillee[i_ligne, i_colonne] = seuillage_pixel(pixel, seuil)

    return im_seuillee


# QUESTION 4
img1_seuillee = seuillage(img1, seuilsRGB)
plt.imshow(img1_seuillee)
plt.show()

"""
Le seuillage à partir d'une image au format RGB est délicat car les 3 composantes de couleur sont utilisées pour donner la couleur affichée.
Ainsi, se concentrer sur une seule composante (ici le rouge) peut donc donner lieu à beaucoup de faux positifs car une composante ne reflète pas la couleur affichée.
Par exemple, le noir est codé par toutes les composantes à 1. Ainsi notre seuillage retourne un résultat indésirable en capturant la couleur noire.
"""


# QUESTION 5
# Ces fonctions ne marcheront pas pour une liste vide (pas grave dans notre cas)
def mini(liste):
    minimum = liste[0]
    for value in liste:
        if value < minimum:
            minimum = value
    return minimum


def maxi(liste):
    maximum = liste[0]
    for value in liste:
        if value > maximum:
            maximum = value
    return maximum


# QUESTION 6
def RGB_to_HSV(rgb):
    hsv = [0, 0, 0]
    delta = maxi(rgb) - mini(rgb)
    c_max = hsv[2] = maxi(rgb)

    if not -10**-8 <= delta <= 10**-8:
        if rgb[0] == c_max:
            hsv[0] = (((rgb[1] - rgb[2]) / delta) % 6) / 6
        if rgb[1] == c_max:
            hsv[0] = (2 + (rgb[2] - rgb[0]) / delta) / 6
        if rgb[2] == c_max:
            hsv[0] = (4 + (rgb[0] - rgb[1]) / delta) / 6

    if not - 10 ** -8 <= c_max <= 10 ** -8:
        hsv[1] = delta / c_max

    return hsv


# QUESTION 7
def conversion_RGB_HSV(im_rgb):
    im_hsv = np.zeros_like(im_rgb)

    for i_ligne, ligne in enumerate(im_rgb):
        for i_colonne, pixel in enumerate(ligne):
            im_hsv[i_ligne, i_colonne] = RGB_to_HSV(pixel)

    return im_hsv


"""
Pour vérifier que la fonction est correct, j'ai utilisé une fonction de matplotlib pour reconvertir en RGB pour voir si on récupérait l'image originale.

img1_hsv = conversion_RGB_HSV(img1)
plt.imshow(hsv_to_rgb(img1_hsv))
plt.show()
"""


# QUESTION 8
seuilsHSV = [0.7, 1, 0.5, 1, 0, 1]


# QUESTION 9
img1_hsv = conversion_RGB_HSV(img1)
img1_seuillee = seuillage(img1_hsv, seuilsHSV)
plt.imshow(img1_seuillee)
plt.show()

"""
Le seuillage est beaucoup mieux. On a toujours quelques faux positifs mais comparé au seuillage précédent, c'est négligable.
"""


# QUESTION 10
# On défini une fonction seuillage_pixel2 exclusif au contexte de la question
def seuillage_pixel2(p, seuil):
    # On sait que seuil[0] > seuil[1]
    if (0 <= p[0] <= seuil[1]
            and seuil[2] <= p[1] <= seuil[3]
            and seuil[4] <= p[2] <= seuil[5]):
        return [1, 1, 1]
    # J'aurai pu utilisé le comparateur "or" mais le code était pas très lisible
    if (seuil[0] <= p[0] <= 1
            and seuil[2] <= p[1] <= seuil[3]
            and seuil[4] <= p[2] <= seuil[5]):
        return [1, 1, 1]

    return [0, 0, 0]


def seuillage2(im, seuil):
    im_seuillee = np.zeros_like(im)

    for i_ligne, ligne in enumerate(im):
        for i_colonne, pixel in enumerate(ligne):
            if seuil[0] > seuil[1]:  # Si H_min est supérieure à H_max, on utilise la nouvelle fonction
                im_seuillee[i_ligne, i_colonne] = seuillage_pixel2(pixel, seuil)
            else:  # Sinon on utilise la fonction originale
                im_seuillee[i_ligne, i_colonne] = seuillage_pixel(pixel, seuil)

    return im_seuillee


img2_hsv = conversion_RGB_HSV(img2)
img2_seuillee = seuillage2(img2_hsv, [0.8, 0.2, 0.5, 1, 0, 1])
plt.imshow(img2_seuillee)


# QUESTION 12
def cherche_centre(im):
    '''détermine le centre de gravité avec les formules du barycentre,
    utilisation des fonctions numpy pour réaliser la somme , im est l'image
    seuillée'''
    h = im.shape[0]  # hauteur de l'image en pixels
    l = im.shape[1]  # largeur de l'image en pixels
    im2D = im[:, :, 0]  # conversion de l'image : le contenu d'un pixel sera un
    # nombre (ex : 1) au lieu d'une liste de 3 nombres
    # identiques (ex : [1,1,1])
    sL = np.sum(im2D, 0)  # liste contenant la somme des lignes pour chaque colonne
    nC = np.arange(l)  # liste contenant les indexs des colonnes : commence à zéro
    pos_p_x = sL*nC  # liste contenant les positions pondérées
    sC = np.sum(im2D, 1)  # liste contenant la somme des colonnes pour chaque ligne
    nL = np.arange(h)  # liste contenant les indexs des lignes
    pos_p_y = sC*nL  # liste contenant les positions pondérées
    s = (np.sum(sL, 0))  # somme de tous les éléments de la matrice
    if s > 0:  # calcul dans le cas où s n'est pas nul
        xg = np.sum(pos_p_x, 0)/s  # somme sur les colonnes des positions pondérées
        yg = np.sum(pos_p_y, 0)/s  # somme sur les lignes des positions pondérées
    else:  # si tous les pixels sont noirs, on place le cdg au centre de l'image
        xg = l/2
        yg = h/2
    return xg, yg


xg, yg = cherche_centre(img2_seuillee)
plt.plot([xg], [yg], 'g^')
plt.show()
# Et ça fonctionne bien :)
