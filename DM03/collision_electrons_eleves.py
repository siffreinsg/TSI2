import matplotlib.pyplot as plt
import time
import random
import sys
sys.setrecursionlimit(10000)
plt.close()

FichierEvts = open("F:\\à modifier\\Evenements.txt", "r")
Evts = FichierEvts.readlines()
FichierEvts.close()

NEvts = len(Evts)

print("Nombre d'évènements à trier : ", NEvts)

# initialisation des listes
IDet = []
Tps = []
i = 0
while (i < NEvts):
    IDet.append(int(Evts[i].split()[0]))
    Tps.append((float(Evts[i].split()[1])))
    i = i+1

# Question 2
"""à compléter"""

# pour tester
# print("Question 2")
# L=[1,3,5]
# print(" Liste : ",L)
# print(" Position de 1 : ",position(1,L),"\n Position de 2 : ",position(2,L),"\n Position de 3 : ",position(3,L),"\n Position de 4 : ",position(4,L),"\n Position de 5 : ",position(5,L),"\n Position de 6 : ",position(6,L))

# Question 3
"""à compléter"""

# Question 4
"""à compléter"""

# pour tester
# print("Question 4")
# L=[12,11,1,3,8,5,14]
# print(" Liste :       ",L)
# print(" Liste triée : ",tri_insertion2(L))

# Question 5
"""à compléter"""

# Question 6
"""fonction donnée"""
Tps_ins2 = Tps[:]  # pour tri insersion classique


def tri_insertion(L):
    for i in range(1, len(L)):
        x = L[i]
        j = i
        while j > 0 and x < L[j-1]:
            L[j] = L[j-1]
            j = j-1
        L[j] = x


"""à compléter"""

# Question 7
print("Question 7")
print("Complexité de tri_insertion2 : à compléter")
print("Complexité de tri_insertion  : à compléter")

# Question 8
"""fonctions données"""
Tps_rap = Tps[:]  # copie pour tri rapide classique


def Echange(T, i, j):
    T[i], T[j] = T[j], T[i]


def Partition(T, g, d):
    assert g < d  # On suppose qu’il y a au moins un élément dans ce segment
    p = T[g]          # p : le pivot
    m = g             # m : indice du tableau déjà parcouru
    for i in range(g+1, d):
        if T[i] < p:
            m = m+1
            Echange(T, i, m)
    if m != g:
        Echange(T, g, m)
    return m


def Tri_rapide_rec(T, g, d):
    while g < d-1:    # tant qu’il reste un élément à trier
        m = Partition(T, g, d)
        if m-g < d-m-1:
            Tri_rapide_rec(T, g, m)
            g = m+1
        else:
            Tri_rapide_rec(T, m+1, d)
            d = m


def tri_rapide(T):
    Tri_rapide_rec(T, 0, len(T))
    return T


print("Question 8")
# L=[12,11,1,3,8,5,14]
# print(" Liste :       ",L)
# print(" Liste triée : ",tri_rapide(L))
"""à compléter"""

# Question 9
"""à compléter"""

# pour tester
# print("Question 9")
# print(" Liste aléatoire : ",liste_aleatoire(10))

# Question 10
"""à compléter"""

# pour tester
# print("Question 10")
# print(" Liste ordonnée : ",liste_ordonnee(10))

# Question 11
"""fonctions données"""


def Fusion(T1, T2):
    if T1 == []:
        return T2
    if T2 == []:
        return T1
    if T1[0] < T2[0]:
        return [T1[0]]+Fusion(T1[1:], T2)
    else:
        return [T2[0]]+Fusion(T1, T2[1:])


def tri_fusion(T):
    if len(T) <= 1:
        return T
    T1 = T[0:len(T)//2]
    T2 = T[len(T)//2:len(T)]
    return Fusion(tri_fusion(T1), tri_fusion(T2))


n = 3400
"""à compléter"""

# pour tester
print("Question 11")
print(" La courbe doit s'ouvrir toute seule")

# Affichage des courbes
"""à compléter"""
