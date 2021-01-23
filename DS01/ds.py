# Nom : JACOBE
# Prénom : Siffrein
# Classe : TSI2
# Réalisé sous Visual Studio Code avec Python 3.8.6

from math import sin, cos, acos, pi
from numpy import array, linspace, arange
from numpy.linalg import solve
import matplotlib.pyplot as plt

R10 = 1
L1 = 50 * 0.001


# QUESTION 1
r = 2
theta10 = 45 * pi/180

L2 = r * L1
theta21 = -theta10 - acos(-L1 / L2 * cos(theta10))

K = array([
    [1, 1, 0],
    [L2 * sin(theta21 + theta10), 0, 0],
    [-L2 * cos(theta21 + theta10), 0, 1]
])
F = array([[-R10], [L1 * sin(theta10) * R10], [-L1 * cos(theta10) * R10]])

# QUESTION 2
U = solve(K, F)

print("K = ", K)
print("F = ", F)
print("Solution [R32,R21,V03] = ", U)


# QUESTION 3
def resolution(theta10_deg, r):
    theta10 = theta10_deg * pi / 180
    L2 = r * L1
    theta21 = -theta10 - acos(-L1 / L2 * cos(theta10))
    K = array([
        [1, 1, 0],
        [L2 * sin(theta21 + theta10), 0, 0],
        [-L2 * cos(theta21 + theta10), 0, 1]
    ])
    F = array([[-R10], [L1 * sin(theta10) * R10], [-L1 * cos(theta10) * R10]])
    return solve(K, F)


def affiche_liste(fig_i, Liste_X, Liste_Y, Legende):
    plt.figure(fig_i)
    plt.plot(Liste_X, Liste_Y, label=Legende)
    plt.ylabel('Données')
    plt.legend()


# QUESTION 4
l_t = linspace(0, 4*pi, 720)
l_theta10 = l_t
R32 = []
R21 = []
V03 = []

for theta10 in l_theta10:
    U = resolution(theta10 * 180/pi, 2)
    R32.append(U[0])
    R21.append(U[1])
    V03.append(U[2])

Fig = 0

affiche_liste(Fig, l_t, R32, "R32")
affiche_liste(Fig, l_t, R21, "R21")
plt.show()

affiche_liste(Fig, l_t, V03, "V03")
plt.show()


# QUESTION 5
def derivee(Liste_x, Liste_y):
    l_x = []
    l_y = []
    for k in range(len(Liste_y) - 1):
        l_x.append(Liste_x[k])
        l_y.append((Liste_y[k+1] - Liste_y[k])/(Liste_x[k+1] - Liste_x[k]))
    return (l_x, l_y)


# QUESTION 6
l_t_der, A03 = derivee(l_t, V03)
affiche_liste(Fig, l_t_der, A03, "A03")
plt.show()


# QUESTION 7
def Etude_r(r):
    l_t = linspace(0, 4*pi, 720)
    l_theta10 = l_t
    V03 = [resolution(theta10 * 180 / pi, r)[2] for theta10 in l_theta10]

    return derivee(l_t, V03)


# QUESTION 8
for r in arange(1.1, 5, 0.5):
    l_t, A03 = Etude_r(r)
    A30 = [-y for y in A03]
    affiche_liste(Fig, l_t, A30, str(r))

plt.show()


# QUESTION 9
"""
On remarque que pour des valeurs de r proche de 3, le moteur n'a pas besoin de changer de sens de rotation pour "créer" une accélération négative.
Cela évite les a-coups et abime moins le moteur.
"""
