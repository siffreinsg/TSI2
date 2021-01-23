def compte(numero):
    if numero > 0:
        print(numero)
        compte(numero - 1)
    else:
        print("Décollage")


compte(5)
