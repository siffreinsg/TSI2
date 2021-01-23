def tri_insertion(T):
    n = len(T)
    for TC in range(1, n):
        temp = T[TC]
        p = TC - 1

        while p >= 0 and temp < T[p]:
            T[p + 1] = T[p]
            p -= 1
        T[p + 1] = temp
    return T


print(tri_insertion([9, 5, 7, 3, 4, 0, 1]))
