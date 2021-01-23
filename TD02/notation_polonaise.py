import operator
import math
from pile import creer_pile, depiler, empiler

ops2 = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
}

ops1 = {
    'abs': operator.abs,
    'opp': lambda x: -x,
    'sq': lambda x: x ** 2,
    'sqrt': math.sqrt
}


def npi(expression):
    pile = creer_pile(len(expression))

    for op in expression:
        if isinstance(op, (int, float)):
            empiler(pile, op)
            continue

        resultat = 0

        if op in ops1.keys():
            operande = depiler(pile)

            resultat = ops1[op](operande)
        elif op in ops2.keys():
            operande1 = depiler(pile)
            operande2 = depiler(pile)

            resultat = ops2[op](operande2, operande1)
        else:
            raise Exception("Unknown operator")

        empiler(pile, resultat)

    return depiler(pile)


print(npi([2, 3, "+", 4, "*"]))
print(npi([2, 3, "-", 4, "/"]))
print(npi([4, 7, "*", "opp"]))
print(npi([4, -3, "**", "abs"]))
