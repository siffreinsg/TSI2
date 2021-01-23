def fusion(T1, T2):
    if T1 == []:
        return T2
    if T2 == []:
        return T1
    if T1[0] < T2[0]:
        return [T1[0]] + fusion(T1[1:], T2)

    return [T2[0]] + fusion(T1, T2[1:])


def trifusion(T):
    if len(T) <= 1:
        return T
    milieu = len(T) // 2
    T1 = T[:milieu]
    T2 = T[milieu:]
    return fusion(trifusion(T1), trifusion(T2))


print(trifusion([9, 5, 7, 3, 4, 0, 1]))
