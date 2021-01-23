def dec2bin(dec):
    if dec == 0:
        return "0"
    return dec2bin(dec // 2) + str(dec % 2)


print(dec2bin(3))
