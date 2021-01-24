"""
Siffrein JACOBÉ
TSI2
Fait sous Visual Studio Code
Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
"""
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


print("=== Question 1: Affiche_n")
print("""La fonction 'print' crée une nouvelle ligne à chaque fois.
Mais la chaîne de caractère 'line' représentant chaque ligne du fichier contient elle-aussi les caractères de fin de ligne.
Cela resulte en une ligne supplémentaire à l'affichage.""")


# Question 2
def is_char_in_string(searched_char, string):
    for character in string:
        if searched_char == character:
            return True
    return False


print("=== Question 2: is_char_in_string")
print("'k' dans 'Amphibologique':", is_char_in_string("k", "Amphibologique"))
print("'p' dans 'Apopathodiaphulatophobe':", is_char_in_string("p", "Apopathodiaphulatophobe"))


# Question 3
def is_word_in_string(word, string):
    n = len(word)
    for i in range(len(string)):
        if string[i:i+n] == word:
            return True
    return False


print("=== Question 3: is_word_in_string")
print("'fromage' dans 'Si vis pacem para bellum':", is_word_in_string("fromage", "Si vis pacem para bellum"))
print("'gum' dans 'Prenez un chewing gum Emile':", is_word_in_string("gum", "Prenez un chewing gum Emile"))


# Question 4
def Affiche_GPS_n(n):
    i = j = 0
    while j < n and i < len(file):
        if is_word_in_string("<when>", file[i]):  # Une ligne "<when>" est forcément suivie d'une ligne "<gx:coord>"
            print(file[i] + file[i+1])
            i += 1  # On sautera deux lignes au lieu d'une seule
            j += 1  # On a affiché un couple supplémentaire
        i += 1  # On saute une ligne


print("=== Question 4: Affiche_GPS_n")
print("")
Affiche_GPS_n(3)


# Question 5
def heure(ligne):
    if "when" in ligne:
        heure = ligne[ligne.find("T") + 1: ligne.find("Z")]
        h = heure.split(":")
        return [float(h[0]), float(h[1]), float(h[2])]
    return None


print("""=== Question 5: heure
1: Si le mot "when" est dans la ligne
2:     heure est la chaîne de caractères extraire de la ligne du caractère suivant la lettre T jusqu'à la lettre Z exclus
3:     h contient le triplet de chaînes de caractères (heures, minutes, secondes)
4:     on retourne une liste de 3 flottants : [heure, minutes, secondes]
5: Sinon
6:     la ligne ne contient pas l'heure, on retourne "None"
7:""")


# Question 6
def coordonnée(ligne):
    if "gx:coord" in ligne:
        coords = ligne[ligne.find(">") + 1: ligne.find("</")].split(" ")
        return [float(coords[0]), float(coords[1]), float(coords[2])]
    return None


print("=== Question 6: coordonnée")
print("Ligne 23:", coordonnée(file[22]))
print("Ligne 24:", coordonnée(file[23]))
print("Ligne 25:", coordonnée(file[24]))


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


T = tableau_donnees(file)
print("=== Question 7: tableau_donnees")
print("3 premiers éléments du tableau:")
print(T[0])
print(T[1])
print(T[2])


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


distances = distance(T)
print("=== Question 8: distance")
print("Distance entre le 1er et le 2e point:", distances[0])
print("Distance entre le 2e et le 3e point:", distances[1])


# Question 9
def distance_total(distances):
    return sum(distances)


print("=== Question 9: distance_total")
print("Distance total parcourue:")
print(distance_total(distances), "km")


# Question 10
def denivele(T):
    total = 0
    for p in range(1, len(T)):
        if T[p][5] > T[p-1][5]:
            total += T[p][5] - T[p-1][5]
    return total


print("=== Question 10: denivele")
print("Dénivelé positif total:")
print(denivele(T), "km")


# Question 11
def distance_cumulee(T):
    distances = distance(T)
    distances_cumulees = []

    for i, d in enumerate(distances):
        denivele = T[i+1][5] - T[i][5]
        distances_cumulees += [((d * 1000)**2 + denivele**2)**(1/2)]

    return distances_cumulees


distances_cumulees = distance_cumulee(T)
print("=== Question 11: distance_cumulee")
print("Distance cumulée entre le 1er et le 2e point:", distances_cumulees[0])
print("Distance cumulée entre le 2e et le 3e point:", distances_cumulees[1])


# Question 12
def vitesse(T):
    distances = distance(T)
    vitesses = []
    for p in range(1, len(T)):
        delta_d = distances[p-1]
        delta_t = (T[p][0] + T[p][1] / 60 + T[p][2] / 3600) - (T[p-1][0] + T[p-1][1] / 60 + T[p-1][2] / 3600)
        vitesse = delta_d / delta_t

        # On obtient parfois des vitesses de 300 km/h à cause d'erreurs de mesure GPS.
        # Pour filtrer ces résultats, on regarde si la vitesse calculée est supérieure à 40 km/h. Si oui, on conserve la vitesse précédente.
        if len(vitesses) > 0 and vitesse > 40:
            vitesses.append(vitesses[-1])
        else:
            vitesses.append(vitesse)
    return vitesses


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


print("=== Question 12")
print("Distance totale:", distance_total(distances), "km")
print("Dénivelé positif:", denivele(T), "km")

fig.suptitle("Profil du parcours", fontsize=16)
plt.show()


# Question 13
def vitesse_moy(T):
    vitesses = vitesse(T)
    return sum(vitesses) / len(vitesses)


print("=== Question 13")
print("Vitesse moyenne:", vitesse_moy(T), "km/h")


# Question 14
def creation_fichier(T):
    with open("resultats.txt", "w") as file:
        for loc in T:
            file.write("\t".join(map(str, loc)) + "\n")


creation_fichier(T)

print("=== Question 14")
print("Fichier créé sous le nom 'resultats.txt'.")
