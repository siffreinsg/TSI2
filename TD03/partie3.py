import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

sys.setrecursionlimit(1000)

# QUESTION 1 et 2
t = np.arange(0, 10, 1/2000)

f_t = 2 * np.sin(2 * np.pi * 0.2 * t)
g_t = (0.15 / 2) * np.sin(2 * np.pi * 50 * t)
f_t_bruite = f_t + g_t

# plt.plot(t, f_t, "--", color="blue", label="Signal")
# plt.plot(t, f_t_bruite, color="green", label="Signal mesuré")
# plt.legend()
# plt.show()


# QUESTION 3 à 6
def filtrage_premier_ordre_iteratif(e, t_div_te):
    S = [e[0]]
    for k in range(1, len(e)):
        S.append(t_div_te / (1 + t_div_te) * S[k - 1] + 1 / (1 + t_div_te) * e[k])
    return S


print(filtrage_premier_ordre_iteratif(list(range(10)), 1))
# On obtient [0, 0.5, 1.25, 2.125, 3.0625, 4.03125, 5.015625, 6.0078125, 7.00390625, 8.001953125]
# Ceci est correct
# La complexité est 6 * n


# QUESTION 7 à 10
def filtrage_premier_ordre_recursif(e, t_div_te):
    if len(e) == 1:
        return [e[0]]

    r = t_div_te / (1 + t_div_te)
    a = 1 / (1 + t_div_te)

    S = filtrage_premier_ordre_recursif(e[:-1], t_div_te)
    S += [r * S[-1] + a * e[-1]]

    return S


print(filtrage_premier_ordre_recursif(list(range(10)), 1))
# On obtient [0, 0.5, 1.25, 2.125, 3.0625, 4.03125, 5.015625, 6.0078125, 7.00390625, 8.001953125]
# Ceci est correct
# Complexité : 6*n


# QUESTION 11
f_t_filtre = filtrage_premier_ordre_iteratif(f_t_bruite, 20)

# plt.plot(t, f_t, "--", color="blue", label="Signal parfait")
# plt.plot(t, f_t_bruite, color="green", label="Signal mesuré")
# plt.plot(t, f_t_filtre, color="red", label="Signal filtré")
# plt.legend()
# plt.show()


# QUESTION 12, 13
t = np.arange(0, 6, 1 / 300)

f_t = signal.square(2 * np.pi * 0.5 * t)
g_t = (0.25 / 2) * np.sin(2 * np.pi * 50 * t)
f_t_bruite = f_t + g_t

t_div_te = (1/5) / (1/50)
f_t_filtre = filtrage_premier_ordre_iteratif(f_t_bruite, t_div_te)

plt.plot(t, f_t, "--", color="blue", label="Signal parfait")
plt.plot(t, f_t_bruite, color="green", label="Signal mesuré")
plt.plot(t, f_t_filtre, color="red", label="Signal filtré")
plt.legend()
plt.show()
