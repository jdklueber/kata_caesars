from tkinter import ttk
import tkinter as tk
from tkinter import scrolledtext

STICKY_FULL = [tk.N, tk.S, tk.E, tk.W]
STICKY_X = [tk.E, tk.W]
CIPHER_CAESAR = "caesar"
CIPHER_VIGNERE = "vignere"


class ConfigFrame:
    def __init__(
        self, parent: tk.Widget, column: int, row: int, colspan: int = None
    ) -> None:
        self.parent = parent
        self.column = column
        self.row = row
        self.frame = ttk.Frame(self.parent)
        self.frame.config(borderwidth=1, relief="groove", padding=(10))

        self.parent.columnconfigure(column, weight=1)

        self.frame.grid(
            column=column, row=row, sticky=STICKY_FULL, columnspan=colspan or 1
        )

        ttk.Label(self.frame, text="Cipher Type:").grid(row=0, column=0)
        self.cipher_type = tk.StringVar(value=CIPHER_VIGNERE)

        ttk.Radiobutton(
            self.frame, text="Caesar", variable=self.cipher_type, value=CIPHER_CAESAR
        ).grid(row=0, column=1, padx=10)

        ttk.Radiobutton(
            self.frame, text="Vignere", variable=self.cipher_type, value=CIPHER_VIGNERE
        ).grid(row=0, column=2, padx=10)

        ttk.Label(self.frame, text="Key:").grid(row=0, column=3)
        self.key = tk.StringVar()
        ttk.Entry(self.frame, textvariable=self.key).grid(
            row=0, column=4, sticky=STICKY_X
        )

        self.frame.columnconfigure(4, weight=1)


class ScrollableTextArea:
    def __init__(
        self, parent, title, id, change_tracker, on_change, row, column
    ) -> None:
        self.title = title
        self.id = id
        self.on_change = on_change
        self.change_tracker = change_tracker
        self.frame = ttk.Frame(parent)
        self.frame.config(borderwidth=1, relief="groove", padding=(10))
        ttk.Label(self.frame, text=title).grid(row=0, column=0)
        self.textbox = scrolledtext.ScrolledText(self.frame)
        self.textbox.grid(row=1, column=0, sticky=STICKY_FULL)
        self.frame.grid(row=row, column=column, sticky=STICKY_FULL)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)

        self.textbox.bind("<FocusIn>", lambda e: self.change_tracker(self.id, True))
        self.textbox.bind("<FocusOut>", lambda e: self.change_tracker(self.id, False))
        self.textbox.bind(
            "<KeyRelease>", lambda e: self.on_change(self.id, self.value())
        )

    def value(self):
        return self.textbox.get("1.0", "end")

    def set(self, text):
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", text)
