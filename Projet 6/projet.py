from os import chdir
from math import sin, sqrt, cos, asin, pi
import matplotlib.pyplot as plt

# chdir(r"C:\Users\Siffrein JACOBE\Documents\Coding\TSI2_info\Projet 6")
chdir(r"D:\Documents\Coding\TSI2\Projet 6")

fid = open("OuCest.kml", "r")
file = fid.readlines()
fid.close()


# Question 1
def Affiche_n(n):
    for line in file[:n]:
        print(line)


"""
La fonction print crée une nouvelle ligne à chaque fois. Mais en plus, la chaîne de caractère "line" représentant chaque ligne du fichier contient elle-aussi les caractères de fin de ligne. Cela resulte en une ligne supplémentaire à l'affichage.
"""


# Question 2
def is_char_in_string(searched_char, string):
    for character in string:
        if searched_char == character:
            return True
    return False


# Question 3
def is_word_in_string(word, string):
    n = len(word)
    for i in range(len(string)):
        if string[i:i+n] == word:
            return True
    return False


# Question 4
def Affiche_GPS_n(n):
    i = j = 0
    while j < n and i < len(file):
        if is_word_in_string("<when>", file[i]):
            print(file[i], "\n", file[i+1])
            i += 1  # On saute deux lignes
            j += 1  # On a affiché un couple supplémentaire
        i += 1


# Question 5
def heure(ligne):
    if "when" in ligne:
        heure = ligne[ligne.find("T") + 1: ligne.find("Z")]
        h = heure.split(":")
        return [float(h[0]), float(h[1]), float(h[2])]
    return None


# Question 6
def coordonnée(ligne):
    if "gx:coord" in ligne:
        coords = ligne[ligne.find(">") + 1: ligne.find("</")].split(" ")
        return [float(coords[0]), float(coords[1]), float(coords[2])]
    return None


# Question 7
def tableau_donnees(fichier):
    tableau = []
    i = 0
    while i < len(fichier):
        if is_word_in_string("<when>", fichier[i]):
            tableau += [heure(fichier[i]) + coordonnée(fichier[i+1])]
            i += 1
        i += 1
    return tableau


# Question 8
def orthodromie(loA, laA, loB, laB):
    """loA, laA, loB, laB représentent les longitudes et latitudes de points exprimés en degrés"""
    R = 6371
    loA = loA * pi / 180
    loB = loB * pi / 180
    laA = laA * pi / 180
    laB = laB * pi / 180
    d = 2 * R * asin(sqrt((sin((laB-laA)/2))**2 + cos(laA)*cos(laB)*(sin((loB-loA)/2))**2))
    return d


def distance(T):
    return [orthodromie(T[p][3], T[p][4], T[p+1][3], T[p+1][4]) for p in range(len(T) - 1)]


# Question 9
def distance_total(distances):
    return sum(distances)


# Question 10
def denivele(T):
    total = 0
    for p in range(1, len(T)):
        if T[p][5] > T[p-1][5]:
            total += T[p][5] - T[p-1][5]
    return total


# Question 11
def distance_cumulee(T):
    distances = distance(T)
    distances_cumulees = []

    for i, d in enumerate(distances):
        denivele = T[i+1][5] - T[i][5]
        distances_cumulees += [((d * 1000)**2 + denivele**2)**(1/2)]

    return distances_cumulees


# Question 12
def vitesse(T):
    distances = distance(T)
    vitesses = []
    for p in range(1, len(T)):
        delta_d = distances[p-1]
        delta_t = (T[p][0] + T[p][1] / 60 + T[p][2] / 3600) - (T[p-1][0] + T[p-1][1] / 60 + T[p-1][2] / 3600)
        vitesses.append(delta_d / delta_t)
    return vitesses


T = tableau_donnees(file)
distances = distance(T)
distances_cumulees = distance_cumulee(T)

x_axis = [0]
altitudes = [T[0][5]]
vitesses = [0.0] + vitesse(T)

for k in range(1, len(T)):
    x_axis += [x_axis[k-1] + distances[k-1]]
    altitudes += [T[k][5]]


fig, ax1 = plt.subplots()
ax1.set_xlabel("Distance (km)")
ax1.set_ylabel("Altitude (km)", color="red")
ax1.plot(x_axis, altitudes, color="red")
ax1.tick_params(axis='y', labelcolor="red")

ax2 = ax1.twinx()
ax2.set_ylabel("Vitesse (km/h)", color="blue")
ax2.plot(x_axis, vitesses, color="blue")
ax2.tick_params(axis="y", labelcolor="blue")


print("Distance totale:", distance_total(distances))
print("Dénivelé positif:", denivele(T))

fig.suptitle("Profil du parcours", fontsize=16)
plt.show()


# Question 13
def vitesse_moy(T):
    vitesses = vitesse(T)
    return sum(vitesses) / len(vitesses)


print("Vitesse moyenne:", vitesse_moy(T))
