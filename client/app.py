import tkinter as tk
from client.components import (
    ConfigFrame,
    ScrollableTextArea,
    CIPHER_CAESAR,
    CIPHER_VIGNERE,
)

from caesar.core import encrypt, decrypt, vignere_encrypt, vignere_decrypt, ALPHABET

FRAME_PLAINTEXT = "plaintext"
FRAME_CIPHERTEXT = "ciphertext"
has_focus = None
source = None
target = None

frame_targets = {}
frame_sources = {}


def change_tracker(id, is_focused):
    global has_focus, target, source
    if is_focused:
        has_focus = id
        source = frame_sources[id]
        target = frame_targets[id]
    elif has_focus == id:
        has_focus = None
        source = None
        target = None


def on_change(id, value):
    global config_frame, has_focus, source, target, CIPHER_VIGNERE, CIPHER_CAESAR

    if id != has_focus:
        print(f"{id} does not have focus: {has_focus} does")
        return

    cipher_type = config_frame.cipher_type.get()
    if len(cipher_type) == 0:
        return

    key = config_frame.key.get()
    if len(key) == 0:
        return

    if cipher_type == CIPHER_CAESAR:
        key = ALPHABET.find(key[0]) + 1

    if source is frame_sources[FRAME_PLAINTEXT]:
        if cipher_type == CIPHER_CAESAR:
            result = encrypt(key=key, plaintext=value)
            target.set(result)
        elif cipher_type == CIPHER_VIGNERE:
            result = vignere_encrypt(key=key, plaintext=value)
            target.set(result)
    elif source is frame_sources[FRAME_CIPHERTEXT]:
        if cipher_type == CIPHER_CAESAR:
            result = decrypt(key=key, ciphertext=value)
            target.set(result)
        elif cipher_type == CIPHER_VIGNERE:
            result = vignere_decrypt(key=key, ciphertext=value)
            target.set(result)


DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

root = tk.Tk()
root.title("Vignere")
root.geometry(f"{DEFAULT_WIDTH}x{DEFAULT_HEIGHT}")
root.config(padx=10, pady=10)
config_frame = ConfigFrame(root, column=0, row=0, colspan=2)
plaintext_frame = ScrollableTextArea(
    root,
    title="Plaintext",
    id=FRAME_PLAINTEXT,
    row=1,
    column=0,
    change_tracker=change_tracker,
    on_change=on_change,
)
ciphertext_frame = ScrollableTextArea(
    root,
    title="Ciphertext",
    id=FRAME_CIPHERTEXT,
    row=1,
    column=1,
    change_tracker=change_tracker,
    on_change=on_change,
)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

frame_targets = {FRAME_PLAINTEXT: ciphertext_frame, FRAME_CIPHERTEXT: plaintext_frame}
frame_sources = {FRAME_PLAINTEXT: plaintext_frame, FRAME_CIPHERTEXT: ciphertext_frame}

root.mainloop()
