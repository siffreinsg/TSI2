# NOM : JACOBE
# Prénom : Siffrein
# TSI2 promo 2020-2021
# **************************************

# Import des librairies
import numpy as np
from math import *
import matplotlib.pyplot as plt
plt.close('all')

# Données pour tout le programme
R10 = 1  # rad/s
L1 = 50 * 0.001  # m

# Question 1
# Données
r = 2
O10_d = 45  # °
# Création de variables intermédiaires
O10_r = O10_d * pi / 180
L2 = r * L1
c = -(L1/L2)*cos(O10_r)
O21_r = - O10_r - acos(c)
# Création de la matrice cinématique K
’’’à compléter’’’
# Création du vecteur F
’’’à compléter’’’
# Question 2 : Résolution
Sol = ’’’à compléter’’’
print("K = ", K)
print("F = ", F)
print("Solution [R32,R21,V03] = ", Sol)
# Question 3 : Mise en place d'une fonction de résolution


def resolution(O10_d, r):
    ’’’à compléter’’’
    return Sol
# Question 4 : affichage sur 2 tours


def affiche_liste(fig_i, Liste_X, Liste_Y, Legende):
    fig = plt.figure(fig_i)
    plt.plot(Liste_X, Liste_Y, label=Legende)
    plt.ylabel('Données')
    plt.legend()
    plt.show()


# Résolution
’’’à compléter’’’
# Affichage
Fig = 0
affiche_liste(Fig, Tps, R32, "R32")
affiche_liste(Fig, Tps, R21, "R21")
