from __future__ import division
from math import log


def menscredit(C, IA, N):
    I = IA/1200  # IA en %, IA/12 en %, IA/1200 en pourcent numérique
    M = C * I * (1 - 1 / (1 - (1 + I) ** N))
    return M


print("La mensualité du prêt est de :", menscredit(200000, 2, 240), "€")


def moiscredit(C, IA, M):
    I = IA / 1200
    N = log(1-1/(1-M/(C*I)))/log(1+I)
    return N


print("Le nombre de mois de crédit est de :", moiscredit(200000, 2, 1000), "mois")


def capcredit(IA, M, N):
    I = IA / 1200
    C = M / (I * (1 - (1 / (1 - (1 + I) ** N))))
    return C


print("La capacité de crédit est de :", capcredit(2, 1000, 240), "€")


def intcredit(C, M, N):
    # M-C*I*(1-1/(1-(1+I)**N)) = 0
    I = 10 / 1200
    f_I = M - C * I * (1 - 1 / (1 - (1 + I) ** N))
    dI = I/10

    while True:
        f_IdI = M - C * (I + dI) * (1 - 1 / (1 - (1 + (I + dI)) ** N))

        if abs(f_IdI) > abs(f_I):
            dI = -dI/2
        elif
