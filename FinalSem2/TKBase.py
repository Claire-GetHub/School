from tkinter import *

class TKBase:
    def __init__(self):
        self.root = Tk()

        self.main()

        self.root.mainloop()

    def main(self) -> None:
        pass

    @staticmethod
    def add(*args, side = TOP) -> None:
        for wid in args:
            wid.pack(side= side)