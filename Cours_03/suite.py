from math import pi


def suite(n):
    if n == 0:
        return 0
    return 1/(n**2) + suite(n-1)


n = 500
res = suite(n)
lim = pi**2/6
ecart = abs((res - lim) / lim)

print(f"Ecart avec la limite: {ecart * 100}")
