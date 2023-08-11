import typer
from caesar.core import encrypt, decrypt, vignere_decrypt, vignere_encrypt


def main(
    key: str,
    d: bool = False,
    vignere: bool = False,
    reverse: bool = False,
    message: str = None,
    infile: str = None,
    outfile: str = None,
):
    if infile:
        with open(infile, "r", encoding="UTF-8") as fh:
            message = fh.read()
            if not message:
                print(f"{infile} not found.")
                exit()

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

    if outfile:
        with open(outfile, "w", encoding="UTF-8") as fh:
            fh.write(result)
    else:
        print(result)


if __name__ == "__main__":
    typer.run(main)
