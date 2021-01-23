from pile import creer_pile, depiler, empiler, est_vide


def parentheses(s: str):
    pile = creer_pile(len(s))
    couples = []

    for i, character in enumerate(s):
        if character == "(":
            empiler(pile, i)
        if character == ")":
            if est_vide(pile):
                return False
            j = depiler(pile)
            couples.append((j, i))

    return couples if est_vide(pile) else False


print("AVEC ()()")
print(parentheses("()()"))

print("AVEC (()()")
print(parentheses("(()()"))

print("AVEC ()())")
print(parentheses("()())"))

print("AVEC (()())")
print(parentheses("(()())"))


def parentheses_OK(s):
    pile = creer_pile(len(s))

    for i, character in enumerate(s):
        if character == "(":
            empiler(pile, i)
        if character == ")":
            if est_vide(pile):
                return False
            depiler(pile)

    return est_vide(pile)
