from cmath import exp
from math import cos, pi
import matplotlib.pyplot as plt


# Question 1
def f1(t, A, fs):
    return A * cos(2 * pi * fs * t)


# Question 2
def Affiche(fig, Lx, Ly, Col):
    plt.plot(Lx, Ly, color=Col, marker="o", linestyle="dashed")
    plt.title(fig)
    plt.show()


# Question 3
def Donnees(N, fe, f):
    Te = 1/fe
    Lt = [k * Te for k in range(0, N)]
    Ly = [f(t) for t in Lt]
    Lf = [fe * i / N for i in range(0, int(N / 2) + 1)]

    return (Lt, Ly, Lf)


# Question 4
A = 1
N = 16
fs = 1
fe = N * fs

Lt, Ly, Lf = Donnees(
    N,
    fe,
    lambda t: f1(t, A, fs)
)

Affiche("f1", Lt, Ly, "black")


# Question 5
def f_ck(Ly, k):
    ck = 0
    N = len(Ly)

    for n in range(0, N):
        ck += Ly[n] * exp(-1j * 2 * pi * k * n / N)

    return ck


# Question 6
def dft(Ly):
    N = len(Ly)
    return [f_ck(Ly, k) for k in range(int(N/2) + 1)]


# Question 7
print(dft(Ly))
