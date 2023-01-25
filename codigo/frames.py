import tkinter as tk


class Frames_base():
    def __init__(self, root) -> None:
        self.root = root

    def cria_frame(self):
        self.tela_1 = tk.Frame(
            self.root,
            background='lightgrey'
        )

        self.tela_1.place(
            relx=0.02,
            rely=0.02,
            relwidth=0.96,
            relheight=0.96
        )
