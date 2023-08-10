import typer
from caesar.core import decrypt


def main(message: str):
    for key in range(27):
        print(f"{key}: {decrypt(key, message)}")


if __name__ == "__main__":
    typer.run(main)
