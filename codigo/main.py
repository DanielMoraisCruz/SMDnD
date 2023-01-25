import tkinter as tk

from frames import Frames_base


class manager():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.configura_tela()
        self.frame_TI = Frames_base(self.root)
        self.frame_TI.cria_frame()

        self.root.mainloop()

    def configura_tela(self):
        self.root.title("SGMD")
        self.root.config(
            background='white'
        )
        self.root.geometry("675x685+0+0")

    def central_manager(self):
        pass


manager()
