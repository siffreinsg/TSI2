def compte_a(s):
    if len(s) == 0:
        return 0
    return compte_a(s[1:]) + (1 if s[0] == "a" else 0)

print(compte_a(""))
print(compte_a("sciences de l'ingénieur"))
print(compte_a("abracadabra"))
print(compte_a("mathématiques"))
