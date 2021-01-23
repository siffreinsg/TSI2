# NOM : ’’’à compléter’’’
# Prénom : ’’’à compléter’’’
# TSI2 promo 2020-2021
#**************************************

# Import des librairies

from math import *
import matplotlib.pyplot as plt
plt.close('all')
import numpy as np

# Données pour tout le programme

R10 = 1         # rad/s
L1 = 50 * 0.001 # m

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
K = np.zeros([3,3])

K[0,0] = 1
K[0,1] = 1
K[2,2] = 1
K[1,0] = L2 * sin(O21_r + O10_r)
K[2,0] = - L2 * cos(O21_r + O10_r)

# Création du vecteur F
F0 = - R10
F1 = L1 * sin(O10_r) * R10
F2 = - L1 * cos(O10_r) * R10
F = np.array([F0,F1,F2])

# Question 2 : Résolution
Sol = np.linalg.solve(K,F)
print("K = ",K)
print("F = ",F)
print("Solution [R32,R21,V03] = ",Sol)

# Question 3 : Mise en place d'une fonction de résolution
def resolution(O10_d,r):
    O10_r = O10_d * pi / 180
    L2 = r * L1
    c = -(L1/L2)*cos(O10_r)
    O21_r = - O10_r - acos(c)
    K = np.zeros([3,3])
    K[0,0] = 1
    K[0,1] = 1
    K[2,2] = 1
    K[1,0] = L2 * sin(O21_r + O10_r)
    K[2,0] = - L2 * cos(O21_r + O10_r)
    F0 = - R10
    F1 = L1 * sin(O10_r) * R10
    F2 = - L1 * cos(O10_r) * R10
    F = np.array([F0,F1,F2])
    Sol = np.linalg.solve(K,F)
    return Sol

# Question 4 : affichage sur 2 tours
def affiche_liste(fig_i,Liste_X,Liste_Y,Legende):
    fig = plt.figure(fig_i)
    plt.plot(Liste_X,Liste_Y,label=Legende)
    plt.ylabel('Données')
    plt.legend()
    plt.show()

# Résolution
Tps = []
R32 = []
R21 = []
V03 = []
for i in range(720):
    Temps = i / (R10 * 180 / pi)
    [r32,r21,v03] = resolution(i,r)
    v30 = - v03
    Tps.append(Temps)
    R32.append(r32)
    R21.append(r21)
    V03.append(v03)

# Affichage
Fig = 0
affiche_liste(Fig,Tps,R32,"R32")
affiche_liste(Fig,Tps,R21,"R21")
Fig += 1
affiche_liste(Fig,Tps,V03,"V03")

# Question 5 : Calcul accélération 0/3
def derivee(Liste_x,Liste_y):
    Liste_Derivee = []
    N = len(Liste_x) - 1
    for i in range(N):
        dt = Liste_x[i+1] - Liste_x[i]
        dy = Liste_y[i+1] - Liste_y[i]
        Acc = dy / dt
        Liste_Derivee.append(Acc)
    Liste_X = Liste_x[0:N]
    return Liste_X,Liste_Derivee

T03,A03 = derivee(Tps,V03)

# affichage
Fig += 1
affiche_liste(Fig,T03,A03,"A03")

# Question 7 : Mise en place d'une fonction
def etude_r(r):
    Tps = []
    R32 = []
    R21 = []
    V30 = []
    for i in range(720):
        Temps = i / (R10 * 180 / pi)
        [r32,r21,v03] = resolution(i,r)
        v30 = - v03
        Tps.append(Temps)
        R32.append(r32)
        R21.append(r21)
        V30.append(v30)
    T30,A30 = derivee(Tps,V30)
    return T30,A30

# Question 8 : affichage
Fig += 1
Plage_r = [i/10 for i in range(11,50,5)]
for i in range(len(Plage_r)):
    r = Plage_r[i]
    T30,A30 = etude_r(r)
    affiche_liste(Fig,T30,A30,str(r))
    
# Question 9 : conclusion
'''Plus r est petit, moins le moteur est encombrant.
A partir de 3, l’accélération parasite disparaît, et qui dit accélération dit
force, et donc vibrations'''

