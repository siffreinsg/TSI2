from os import chdir
from math import sin, sqrt, cos, asin, pi
from time import strftime
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

chdir(r"C:\Users\Siffrein JACOBE\Documents\Coding\TSI2_info\Projet 6")

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
            i += 1  # On saute deux lignes
            j += 1  # On a affiché un couple supplémentaire
        i += 1


# Question 5
def heure(ligne):
    if "when" in ligne:
        # <when>2014-01-05T09:41:07.580Z</when>
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
    return [orthodromie(T[p][4], T[p][5], T[p+1][4], T[p+1][5]) for p in range(len(T) - 1)]


# Question 9
def distance_total(D):
    return sum(D)


# Question 10
def denivele(T):
    total = 0
    for p in range(len(T) - 1):
        if T[p+1][5] > T[p][5]:
            total += T[p + 1][5] - T[p][5]
    return total / 1000


# Question 11
def distance_cumulee(T):
    D = distance(T)
    return [distance_total(D), denivele(T)]


# Question 12
T = tableau_donnees(file)

distances_entre_points = distance(T)
distance_total_parcourue, denivele_positif = distance_cumulee(T)


vitesses = [0.0]

for p in len(1, len(T)):
    delta_t = (T[p][0] + T[p][1] / 60 + T[p][2] / 3600) - (T[p - 1][0] + T[p - 1][1] / 60 + T[p - 1][2] / 3600)
    delta_d = distances_entre_points[p - 1] // 1000
    vitesses += [delta_d / delta_t]


# abscisses, ordonnees = [], []
# for position in T[1:]:
#     # position = [heures, minutes, secondes, longitude, latitude, altitude]
#     abscisses += [position[0] * 3600 + position[1] * 60 + position[2]]
#     ordonnees += []
