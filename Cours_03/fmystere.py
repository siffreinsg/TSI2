def dk(L1, L2):
    if L1 == []:
        return L2

    s = L1.pop(0)
    if s not in L2:
        L2.append(s)
    return dk(L1, L2)


print(dk([34, 2, 3, 11, 11, 2, 34, 7, 1, 7, 7, 11, 3, 11], []))

# Cette fonction retourne les éléments de la liste sans doublon
