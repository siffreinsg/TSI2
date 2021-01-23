def tri_permutation(T):
    n = len(T)
    for TC in range(n):
        for i in range(n - 1, TC, -1):
            if T[i-1] > T[i]:
                T[i-1], T[i] = T[i], T[i-1]
    return T


print(tri_permutation([9, 5, 7, 3, 4, 0, 1]))
