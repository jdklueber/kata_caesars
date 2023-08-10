import pytest
from caesar.core import (
    _encrypt_letter,
    _decrypt_letter,
    encrypt,
    decrypt,
    get_vignere_key,
    vignere_encrypt,
    vignere_decrypt,
)


PLAINTEXT = "plain"
CIPHERTEXT = "cipher"
KEY = "key"

test_data_strings = [
    {"key": 0, "plain": "ABCDEFGZ", "cipher": "ABCDEFGZ"},
    {"key": 1, "plain": "ABCDEFGZ", "cipher": "BCDEFGHA"},
    {"key": 2, "plain": "ABCDEFGZ", "cipher": "CDEFGHIB"},
    {"key": 3, "plain": "ABCDEFGZ", "cipher": "DEFGHIJC"},
]

test_data_letters = [
    {"key": 0, "plain": "A", "cipher": "A"},
    {"key": 1, "plain": "A", "cipher": "B"},
    {"key": 2, "plain": "A", "cipher": "C"},
    {"key": 1, "plain": "Z", "cipher": "A"},
    {"key": 2, "plain": "Z", "cipher": "B"},
]


@pytest.mark.parametrize("test_letters", test_data_letters)
def test_encrypt_letter(test_letters: dict):
    assert (
        _encrypt_letter(test_letters[KEY], test_letters[PLAINTEXT])
        == test_letters[CIPHERTEXT]
    )


@pytest.mark.parametrize("test_letters", test_data_letters)
def test_decrypt_letter(test_letters: dict):
    assert (
        _decrypt_letter(test_letters[KEY], test_letters[CIPHERTEXT])
        == test_letters[PLAINTEXT]
    )


@pytest.mark.parametrize("test_data", test_data_strings)
def test_encryption(test_data: dict):
    expected = test_data[CIPHERTEXT]
    actual = encrypt(test_data[KEY], test_data[PLAINTEXT])
    assert actual == expected


@pytest.mark.parametrize("test_data", test_data_strings)
def test_decryption(test_data: dict):
    expected = test_data[PLAINTEXT]
    actual = decrypt(test_data[KEY], test_data[CIPHERTEXT])
    assert actual == expected


def test_get_vignere_key():
    assert get_vignere_key("a") == 1
    assert get_vignere_key("A") == 1
    assert get_vignere_key("Z") == 26


def test_vignere_encrypt():
    key = "AABB"
    plain = "ABCDEFG"
    expected = "BCEFFGI"
    assert vignere_encrypt(key, plain) == expected


def test_vignere_decrypt():
    key = "AABB"
    expected = "ABCDEFG"
    cipher = "BCEFFGI"
    assert vignere_decrypt(key, cipher) == expected
