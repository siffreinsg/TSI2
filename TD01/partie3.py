def mdp2hex(password_text):
    result = ""
    for char in password_text:
        result += hex(ord(char))[2:]
    return result.upper()


def hex2mdp(password_hex):
    result = ""
    for k in range(0, len(password_hex), 2):
        result += chr(int(password_hex[k: k + 2], base=16))
    return result
