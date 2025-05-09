from tkinter import *
from TKBase import TKBase

class Gui (TKBase):
    def main(self) -> None:
        self.mainFrame = Frame(self.root)
        self.viewFrame = Frame(self.root)
        self.addFrame = Frame(self.root)
        self.delFrame = Frame(self.root)

        #MAIN FRAME
        self.view = Button(self.mainFrame, text= "", command= lambda : print("test"))
        self.addItem = Button(self.mainFrame, text= "", command= lambda : print("test"))
        self.updateItem = Button(self.mainFrame, text= "", command= lambda : print("test"))
        self.delItem = Button(self.mainFrame, text= "", command= lambda : print("test"))
        self.sortPrice = Button(self.mainFrame, text= "", command= lambda : print("test"))
        self.sortFav = Button(self.mainFrame, text= "", command= lambda : print("test"))
        self.exit = Button(self.mainFrame, text= "", command= lambda : print("test"))
        

if __name__ == "__main__":
    tk = Gui()