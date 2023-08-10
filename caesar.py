import typer
from caesar.core import encrypt, decrypt


def main(key: int, message: str, d: bool = False):
    if d:
        print(decrypt(key, message))
    else:
        print(encrypt(key, message))


if __name__ == "__main__":
    typer.run(main)
