def partition(T, g, d):
    assert g <= d
    v, m = T[g], g

    for i in range(g + 1, d):
        if T[i] < v:
            m += 1
            T[i], T[m] = T[m], T[i]
    if m != g:
        T[g], T[m] = T[m], T[g]
    return m


def tri_rapide_rec(T, g, d):
    while g < d - 1:
        m = partition(T, g, d)
        if (m - g) < (d - m - 1):
            tri_rapide_rec(T, g, m)
            g += 1
        else:
            tri_rapide_rec(T, m + 1, d)
            d = m


def tri_rapide(T):
    tri_rapide_rec(T, 0, len(T))
    return T


print(tri_rapide([9, 5, 7, 3, 4, 0, 1]))
