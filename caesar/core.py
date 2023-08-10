import string

ALPHABET = string.ascii_lowercase


def _encrypt_letter(key: int, plaintext: str):
    idx = ALPHABET.find(plaintext.lower())
    if idx > -1:
        idx += key
        if idx >= len(ALPHABET):
            idx -= len(ALPHABET)
        elif idx < 0:
            idx += len(ALPHABET)

        if plaintext.isupper():
            return ALPHABET[idx].upper()
        else:
            return ALPHABET[idx]
    else:
        return plaintext


def _decrypt_letter(key: int, ciphertext: str):
    return _encrypt_letter(key * -1, ciphertext)


def encrypt(key, plaintext: str):
    result = ""
    for letter in plaintext:
        result += _encrypt_letter(key, letter)

    return result


def decrypt(key, ciphertext: str):
    return encrypt(key * -1, ciphertext)
