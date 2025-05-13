from tkinter import *
from TKBase import TKBase
from WishList import WishList
from re import match

class Gui (TKBase):
    def main(self) -> None:
        self.wList = WishList()

        #scenes
        self.mainFrame = Frame(self.root)
        self.viewFrame = Frame(self.root)
        self.changeFrame = Frame(self.root)

        #variables
        self.currentFrame = self.mainFrame
        self.editType = None


        #MAIN FRAME
        self.view = Button(self.mainFrame, text= "view", command= lambda : self.multiFunc([lambda : self.switchFrames(self.viewFrame), lambda : self.showWList(self.wList.view)]))
        self.addItem = Button(self.mainFrame, text= "addItem", command= lambda : self.multiFunc([lambda : self.switchFrames(self.changeFrame), lambda : self.editFunc(True)]))
        self.exit = Button(self.mainFrame, text= "exit", command= self.root.destroy)
        

        #VIEW FRAME
        self.leftFrame = Frame(self.viewFrame)
        self.rightFrame = Frame(self.viewFrame)

        #Item, Quantity, Price, Favorite
        self.namelist = Listbox(self.leftFrame, height= 20, width= 10)
        self.qualist = Listbox(self.leftFrame, height= 20, width= 10)
        self.pricelist = Listbox(self.leftFrame, height= 20, width= 10)
        self.favlist = Listbox(self.leftFrame, height= 20, width= 10)

        self.delItem = Button(self.rightFrame, text= "Delete Item", command= lambda : print(self.wList.view))
        self.updateItem = Button(self.rightFrame, text= "Update Item", command= lambda : self.multiFunc([lambda : self.switchFrames(self.changeFrame), lambda : self.editFunc(False)]))

        self.fav = Radiobutton(self.rightFrame, text= "favorite")
        self.price = Radiobutton(self.rightFrame, text= "price")

        self.exitView = Button(self.rightFrame, text= "mainMenu", command= lambda : self.switchFrames(self.mainFrame))

        #ADD FRAME
        self.nameLabel = Label(self.changeFrame, text= "Name")  
        self.nameVar = StringVar() 
        self.nameInput = Entry(self.changeFrame, textvariable= self.nameVar)

        self.quantityLabel = Label(self.changeFrame, text= "Quantity")   
        self.quaVar = StringVar()
        self.quantityInput = Entry(self.changeFrame, textvariable= self.quaVar)  

        self.priceLabel = Label(self.changeFrame, text= "Price")  
        self.priceVar = StringVar()
        self.priceInput = Entry(self.changeFrame, textvariable= self.priceVar)  

        self.favoriteLabel = Label(self.changeFrame, text= "Favorite")   
        self.favVar = IntVar()
        self.favoriteInput = Checkbutton(self.changeFrame, variable= self.favVar) 

        self.changeButton = Button(self.changeFrame, text= "add/update", command= self.changeFunc)

        self.outputChange = StringVar()
        self.outputLabel = Label(self.changeFrame, textvariable= self.outputChange) 

        self.exitChange = Button(self.changeFrame, text= "mainMenu", command= lambda : self.switchFrames(self.mainFrame))


        self.mainFrame.pack()
        
        #main frame packing
        self.add([self.view,
        self.addItem,
        self.updateItem,
        self.exit])

        #view frame packing
        self.leftFrame.pack(side="left")
        self.add([self.namelist,
        self.qualist,
        self.pricelist,
        self.favlist], side= LEFT)
        self.rightFrame.pack(side="right")
        self.add([ self.delItem,
        self.updateItem,
        self.fav,
        self.price])

        #add frame packing
                                                         
        self.add([self.nameLabel,
        self.nameInput,
        self.quantityLabel,
        self.quantityInput,
        self.priceLabel,
        self.priceInput,
        self.favoriteLabel,
        self.favoriteInput,
        self.changeButton,
        self.outputLabel,
        self.exitChange])

    def switchFrames(self, newFrame):
        self.currentFrame.pack_forget()
        self.currentFrame = newFrame
        self.currentFrame.pack()
    
    def showWList(self, wList: dict):
        self.list.delete(1, END)
        i = 1
        for item in wList:
            self.list.insert(i, f"{item}: {wList[item][0]}, {wList[item][1]}, {wList[item][2]}")
            i += 1


    def multiFunc(self, funcs: list):
        for func in funcs:
            func()

    def editFunc(self, b: bool):
        self.editType = b

    def changeFunc (self):
        self.checkEntries()

        #Item, Quantity, Price, Favorite
        itemName = self.nameVar.get().strip()
        val = [self.quaVar.get().strip(),
        self.priceVar.get().strip(),
        self.checkFav()]

        if self.editType:
            if self.wList.addItem(itemName, val):
                self.outputChange.set("Item added")
            else:
                self.outputChange.set("Item already exists!")            
        else:
            if self.wList.updateItem(itemName, val):
                self.outputChange.set("Item updated!")
            else:
                self.outputChange.set("Item Doesn't exist")


    def checkFav(self):
        if self.favVar.get() == 1:
            return True
        else:
            return False

    def checkEntries(self):
        if self.nameVar.get() == "" or self.quaVar.get() == "" or self.priceVar.get() == "":
            self.outputChange.set("Missing information!")
        elif not self.quaVar.get().strip().isdigit():
            self.outputChange.set("Quantity must be an integer!")
        elif not match(r"^\$?\d+\.?\d*$", self.priceVar.get().strip()):
            self.outputChange.set("Price must be a positive float!")
        

if __name__ == "__main__":
    tk = Gui()