def creer_pile(c):
    p = (c + 1) * [None]
    p[0] = 0
    return p


def depiler(p):
    n = p[0]
    assert n > 0
    p[0] = n - 1
    return p[n]


def empiler(p, v):
    n = p[0]
    assert n < len(p) - 1
    n = n + 1
    p[0] = n
    p[n] = v


def taille(p):
    return p[0]


def est_vide(p):
    return taille(p) == 0


def sommet(p):
    assert taille(p) > 0
    return p[p[0]]
