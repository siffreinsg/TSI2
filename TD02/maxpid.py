from scipy import stats
import matplotlib.pyplot as plt
from os import chdir

chdir("C:\\Users\\Siffrein JACOBE\\Documents\\Coding\\TSI2_info\\TD02")

fichier = open("linearite.csv", "r")
variable = fichier.readline().rstrip('\n\r').split(";")
unite = fichier.readline().rstrip('\n\r').split(";")

x = []
y = []

for ligne in fichier:
    ligne = ligne.replace(',', '.')
    donnees = ligne.rstrip('\n\r').split(";")
    x.append(float(donnees[1]))
    y.append(float(donnees[0]))
fichier.close()

plt.plot(x, y)
plt.xlabel("Position angulaire du rotor du moteur par rapport au stator du moteur en degré")
plt.ylabel("Position angulaire du bras par rapport à la chaise en degré")

a, b, r, p, std_err = stats.linregress(x, y)

# QUESTION 1 et 2
y_reg = [a*x + b for x in x]
plt.plot(x, y_reg)

print("L'équation de la droite est:")

eq = "y = " + str(a) + "* x "
if b >= 0:
    eq += "+ "
eq += str(b)

print(eq)
print("avec un coefficient de regression", "\n", "r² = ", r)

plt.show()


# QUESTION 3
while abs(r) < 0.999:
    x.pop()
    y.pop()
    a, b, r, p, std_err = stats.linregress(x, y)


print("L'équation de la droite est:")

eq = "y = " + str(a) + "* x "
if b >= 0:
    eq += "+ "
eq += str(b)

print(eq)
print("avec un coefficient de regression")
print("r² = ", r)

plt.plot(x, y)
plt.xlabel("Position angulaire du rotor du moteur par rapport au stator du moteur en degré")
plt.ylabel("Position angulaire du bras par rapport à la chaise en degré")

y_reg = [a * x + b for x in x]
plt.plot(x, y_reg)
plt.show()


# QUESTION 4
r = 0
while (abs(r) < 0.999):
    x.pop(0)
    y.pop(0)
    a, b, r, p, std_err = stats.linregress(x, y)


print("L'équation de la droite est:")

eq = "y = " + str(a) + "* x "
if b >= 0:
    eq += "+ "
eq += str(b)

print(eq)
print("avec un coefficient de regression")
print("r² = ", r)

plt.plot(x, y)
plt.xlabel("Position angulaire du rotor du moteur par rapport au stator du moteur en degré")
plt.ylabel("Position angulaire du bras par rapport à la chaise en degré")

y_reg = [a * x + b for x in x]
plt.plot(x, y_reg)
plt.show()
