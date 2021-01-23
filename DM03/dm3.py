"""
Auteur: Siffrein JACOBE
Promo: TSI2 2020-2021
Fait sur Visual Studio Code, testé sur Pyzo
"""
import sys
import time
import random
import math
import matplotlib.pyplot as plt

sys.setrecursionlimit(200000)

FichierEvts = open(r"C:\Users\Siffrein JACOBE\Documents\Coding\TSI2_info\DM03\Evenements.txt", "r")
Evts = FichierEvts.readlines()
FichierEvts.close()

IDet = []
Tps = []
i = 0
while i < len(Evts):
    IDet.append(int(Evts[i].split()[0]))
    Tps.append((float(Evts[i].split()[1])))
    i = i+1


# Question 2
def position(x, L):
    a, b = 0, len(L)  # On commence aux bornes extrêmes de la liste L. len(L) permet de pouvoir placer l'élément x après tous les autres éléments de la liste si nécessaire.
    while a != b:  # Tant qu'on a pas trouvé la position
        c = (a+b) // 2  # On prend le milieu de l'intervalle
        if x > L[c]:  # Si x est dans l'intervalle [c+1, b]
            a = c + 1  # On recommencera la recherche dans cet intervalle
        else:  # Sinon (x est dans [a,c])
            b = c  # On recommencera la recherche dans cet intervalle
    return a  # On a == b, la position de x


# Avec une fonction récursive
def position_rec(x, L, a=0, b=None):  # "a" a pour valeur par défaut 0 ; on ne peut pas mettre len(L) comme valeur par défaut de b ici
    if b is None:  # Si b n'est pas renseigné
        b = len(L)  # On défini b à len(L)
    if a == b:  # Si a == b, on a trouvé la position
        return a

    c = (a + b) // 2  # Milieu de l'intervalle [a,b]
    if x > L[c]:  # Si x est dans l'intervalle [c+1, b]
        return position_rec(x, L, c + 1, b)  # On cherche la position dans cette intervalle
    return position_rec(x, L, a, c)  # Sinon on le cherche dans l'intervalle [a, c]


L = [1, 3, 5]
print("Question 2: position(x, L)")
print("    Position de 0:", position(0, L))
print("    Position de 1:", position(1, L))
print("    Position de 2:", position(2, L))
print("    Position de 3:", position(3, L))
print("    Position de 4:", position(4, L))
print("    Position de 5:", position(5, L))
print("    Position de 6:", position(6, L))


# Question 3
def tri_insertion_rec(L, n):
    if len(L[:n]) >= 1:
        tri_insertion_rec(L, n-1)
        x = L.pop()
        pos = position(x, L[:n])
        L.insert(pos, x)


# Question 4
def tri_insertion2(L):
    L_copie = L[:]  # On fait une copie de la liste
    tri_insertion_rec(L_copie, len(L) - 1)  # On travaille sur cette copie pour ne pas modifier l'originale
    return L_copie  # On retourne la liste triée


L = list(range(0, 10)) * 2  # On crée une liste aléatoire contenant tous les chiffre, deux fois pour s'assurer que la fonction réagit correctement aux doublons
random.shuffle(L)  # On mélange cette liste
L_triee = tri_insertion2(L)  # Et on la trie

print("Question 4: tri_insertion2(L)")
print("    Liste:", L)
print("    Triée:", L_triee)


# Question 5
t = time.time()
# tri_insertion2(Tps)  # Plante si len(Tps) > 1550 environ
tri_insertion2(Tps[:1500])  # Pour avoir des résultats, je trie seulement les 1500 premiers éléments de Tps
delta_t = time.time() - t

print("Question 5: tri_insertion2(Tps)")
print("    Triée en", delta_t, "secondes.")


# Question 6
def tri_insertion(L):
    for i in range(1, len(L)):
        x = L[i]
        j = i
        while j > 0 and x < L[j-1]:
            L[j] = L[j-1]
            j = j-1
        L[j] = x


t = time.time()
tri_insertion(Tps[:1500])
delta_t = time.time() - t

print("Question 6: tri_insertion(Tps)")
print("    Triée en", delta_t, "secondes.")


# Question 7
print("Question 7: Complexités")
print("    Complexité de tri_insertion2 : O(n*log n)")
print("    Complexité de tri_insertion  : O(n^2)")

"""
Les tests ont été réalisés sur une liste de 1500 éléments extraite de Tps.

Temps d'exécutions
tri_insertion: 0.005 s
tri_insertion2: 0.075s

Cependant on remarque que la complexité dans le meilleur des cas (quand la liste est quasiment triée pour tri_insertion est O(n) alors que tri_insertion2 elle reste O(n*log n).
Or on note que la liste Tps est déjà presque triée, ce qui explique les temps d'exécutions.
Ce comportement se confirmera à la fin de ce DM à l'affichage du graph.
"""


# Question 8
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


Tps_rap = Tps[:1500]  # On prend que les 1500 premiers éléments pour ne pas planter

t = time.time()
tri_rapide(Tps_rap)
delta_t = time.time() - t

print("Question 8: tri_rapide(Tps)")
print("    Triée en", delta_t, "secondes.")


# Question 9
def liste_aleatoire(n):
    # Avec la fonction random.random :
    return [math.floor(random.random() * 100000 + 1) for _ in range(n)]
    # Sinon, une possibilité plus explicite mais moins rapide:
    # return [r.randint(1, 100000) for _ in range(n)]


print("Question 9: liste_aleatoire(n)")
print("    n=10 :", liste_aleatoire(10))


# Question 10
def liste_ordonne(n):
    return [*range(1, n+1)]


print("Question 10: liste_ordonnee(n)")
print("    n=10 :", liste_ordonne(10))


# Question 11
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


# Mesure le temps d'exécution d'une fonction tri "f_tri" sur une liste de taille n
def mesurer_temps(n, f_tri):
    l_aleatoire = liste_aleatoire(n)
    l_ordonnee = liste_ordonne(n)

    t = time.time()
    f_tri(l_aleatoire)
    dt1 = time.time() - t

    t = time.time()
    f_tri(l_ordonnee)
    dt2 = time.time() - t

    return dt1, dt2


# On stocke les résultats dans un dict qu'on exploitera plus tard pour l'affichage
# On pourrait également enregistrer ces résultats dans un fichier pour être réutilisés plus tard
# J'ai fais ce choix parce que c'est tout d'abord plus simple à visualiser et plus facile à manipuler
# (dans mes tests notamment j'avais écris ces résultats dans un fichier que j'importais ensuite au lieu que de tout recalculer)
resultats = {
    "tailles_listes": range(0, 3400, 50),
    "aleatoire": {
        "insertion": [],
        "insertion2": [],
        "rapide": [],
        "fusion": [],
    },
    "ordonnee": {
        "insertion": [],
        "insertion2": [],
        "rapide": [],
        "fusion": [],
    }
}

# Pour toujours garder les mêmes couleurs dans le graph.
couleurs = {
    "insertion": "blue",
    "insertion2": "green",
    "rapide": "red",
    "fusion": "cyan",
}

# On effectue les mesures de temps
for n in resultats["tailles_listes"]:  # Pour chaque taille n des listes
    for f_tri in [tri_insertion, tri_insertion2, tri_rapide, tri_fusion]:  # Pour chaque algorithme de tri
        temps_mesures = mesurer_temps(n, f_tri)  # On mesure le temps nécessaire aux calculs
        nom_tri = f_tri.__name__[4:]  # On récupère le nom de l'algorithme de tri à partir de la fonction associée
        resultats["aleatoire"][nom_tri].append(temps_mesures[0])  # On enregistre le résultat pour une liste aléatoire
        resultats["ordonnee"][nom_tri].append(temps_mesures[1])  # Et de même pour une liste ordonnée


# On affiche les résultats
for liste in ["aleatoire", "ordonnee"]:  # Pour chaque type de liste
    plt.title("Liste " + liste)  # On définit le nom du graph
    for nom_tri in resultats[liste]:  # Pour chaque algorithme de tri
        # On trace la courbe du temps en fonction de la taille de liste avec la couleur choisie et une légende
        plt.plot(resultats["tailles_listes"], resultats[liste][nom_tri], label="Tri " + nom_tri, color=couleurs[nom_tri])
    plt.legend()
    plt.show()  # Puis on trace le tout
