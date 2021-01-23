# -*- coding: utf-8 -*-
"""
Exploitation des mesures d'un accelerometre : application sur un Tramway ligne T3a
"""
from os import chdir
from matplotlib import pyplot as plt
import numpy as np
chdir(r"C:\Users\Siffrein JACOBE\Documents\Coding\TSI2_info\TD04")

# comptage du nombre de ligne
fichier = open('tramway.txt', 'r')    # Ouverture d'un fichier en lecture:
lecture = fichier.readlines()
nb_lignes = len(lecture)
fichier.close()                      # Fermeture du fichier

# extraction des données utiles
fichier = open('tramway.txt', 'r')
fichier.readline()  # saut d'une ligne (non prise en compte des intitulés temps,..)

# initialisation des listes
temps = []
acceleration_x = []
acceleration_y = []

for i in range(nb_lignes-2):
    ligne = fichier.readline()            # lecture d'une ligne
    ligne = ligne.rstrip("\n\r")         # suppression retour chariot
    ligne = ligne.replace(",", ".")        # changement , en .
    ligne_data = ligne.split("\t")        # découpage aux tabulations

    # Création des listes
    temps.append(ligne_data[1])
    acceleration_x.append(ligne_data[3])  # extraction acceleration latérale (selon x)
    acceleration_y.append(ligne_data[5])  # extraction acceleration longitudinal (selon y)

    i = i+1                               # compteur boucle for

fichier.close()  # Fermeture du fichier

# Question 1
temps = [float(t) for t in temps]
acceleration_x = [float(a) for a in acceleration_x]
acceleration_y = [float(a) for a in acceleration_y]

print(temps[0] + temps[1])
print(acceleration_y[0] + acceleration_y[1])

# Question 2
acceleration_x_ms2 = [a * 9.81 for a in acceleration_x]
acceleration_y_ms2 = [a * 9.81 for a in acceleration_y]


# Question 3
def affiche(L):
    plt.plot(temps, L)
    plt.show()


# affiche(acceleration_x_ms2)
# affiche(acceleration_y_ms2)


# Question 5
def maxi(L, i, j):
    l = L[i:j]
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return l[0]

    milieu = len(l) // 2
    max1 = maxi(l, 0, milieu)
    max2 = maxi(l, milieu, len(l))

    return max1 if max1 > max2 else max2


print("Accélération longitudinale max:", maxi(acceleration_y_ms2, 0, len(acceleration_y_ms2)), "m.s^(-2)")


# Question 6
def moy_ecarts(L, ti, tj):
    L_t = []
    l = []

    for t, Lv in zip(temps, L):
        if ti <= t <= tj:
            L_t.append(t)
            l.append(Lv)

    n = len(l)
    moy = sum(l) / n
    ecart = (np.sum((np.array(l) - moy) ** 2) / n) ** (1/2)

    return moy, ecart


print(moy_ecarts(acceleration_y_ms2, 8, 12))


# Question 7
def filtre_mg(L, N):
    L_t_filtree = L[N:]
    L_filtree = []

    for i in range(N, len(L)):
        L_filtree.append(sum(L[i - N:i]) / N)

    return L_t_filtree, L_filtree


L_t, l_y = filtre_mg(acceleration_y_ms2, 3)
plt.plot(L_t, l_y)
plt.show()
