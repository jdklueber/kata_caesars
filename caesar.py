import typer
from caesar.core import encrypt, decrypt, vignere_decrypt, vignere_encrypt


def main(
    key: str,
    message: str,
    d: bool = False,
    vignere: bool = False,
    reverse: bool = False,
):
    result = ""
    if d:
        if vignere:
            result = vignere_decrypt(key, message)
        else:
            key = int(key)
            result = decrypt(key, message)
        if reverse:
            result = "".join(reversed(message))
    else:
        if reverse:
            message = "".join(reversed(message))
        if vignere:
            result = vignere_encrypt(key, message)
        else:
            key = int(key)
            result = encrypt(key, message)

    print(result)


if __name__ == "__main__":
    typer.run(main)
