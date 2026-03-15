CHARACTERS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encode_base62(num):
    if num == 0:
        return CHARACTERS[0]

    base62 = []

    while num > 0:
        remainder = num % 62
        base62.append(CHARACTERS[remainder])
        num = num // 62

    base62.reverse()
    return "".join(base62)