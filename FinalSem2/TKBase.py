from tkinter import *

class TKBase:
    def __init__(self):
        self.root = Tk()

        self.main()

        self.root.mainloop()

    def main(self) -> None:
        pass

    @staticmethod
    def add(self, wids: list, side = TOP) -> None:
        for wid in wids:
            wid.pack(side= side)