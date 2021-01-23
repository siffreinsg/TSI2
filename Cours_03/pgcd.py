def pgcd(a, b):
    if b == 0:
        return a
    r = a % b
    return pgcd(b, r)


def pgcd_liste(liste):
    if len(liste) == 1:
        return liste[0]

    div = pgcd(liste[0], liste[1])
    return pgcd_liste([div] + liste[2:])
