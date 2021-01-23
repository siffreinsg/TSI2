def dec2bin(dec, length):
    result = ""
    rest = dec

    while rest != 0:
        result += str(rest % 2)
        rest //= 2

    return result[::-1].zfill(length)


def dec2bin_v2(dec):
    result = ""
    rest = dec

    while rest = /=


def dec2bins(dec, length):
    abs_bin = dec2bin(abs(dec), length).lstrip("0")

    reverted = ""
    for char in abs_bin:
        reverted += "0" if char == "1" else "1"

    characters = list(reverted)
    for k in range(len(characters)):
        if characters[-1 - k] == "0":
            characters[-1 - k] = "1"
            break

        characters[-1 - k] = "0"

        if k == (len(characters) - 1):
            characters.insert(0, "1")

    if dec < 0:
        characters.insert(0, "1")

    return "".join(characters).zfill(length)


def _int(binary):
    dec = 0
    for index, char in enumerate(binary):
        if char == "1":
            dec += 2 ** (len(binary) - index - 1)
    return dec

# à finir
