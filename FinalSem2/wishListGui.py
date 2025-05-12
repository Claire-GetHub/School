from tkinter import *
from TKBase import TKBase
from WishList import WishList

class Gui (TKBase):
    def main(self) -> None:
        self.wList = WishList()


        self.mainFrame = Frame(self.root)
        self.viewFrame = Frame(self.root)
        self.changeFrame = Frame(self.root)

        self.currentFrame = self.mainFrame

        #MAIN FRAME
        self.view = Button(self.mainFrame, text= "view", command= lambda : self.switchFrames(self.viewFrame))
        self.addItem = Button(self.mainFrame, text= "addItem", command= lambda : self.switchFrames(self.changeFrame))
        self.exit = Button(self.mainFrame, text= "exit", command= self.root.destroy)

        #VIEW FRAME
        self.leftFrame = Frame(self.viewFrame)
        self.rightFrame = Frame(self.viewFrame)

        self.list = Listbox(self.leftFrame)

        self.delItem = Button(self.rightFrame, text= "Delete Item", command= lambda : print("test"))
        self.updateItem = Button(self.rightFrame, text= "Update Item", command= lambda : print("test"))

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

        self.changeButton = Button(self.changeFrame, text= "add/update", command= lambda : print("add"))

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
        self.rightFrame.pack(side="right")
        self.add([self.list, 
        self.delItem,
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

    def changeFunc (self, add: bool = True):
        pass
        #Finish funtion
        if add:
            self.wList.addItem()
        else:
            self.wList.updateItem()
        

if __name__ == "__main__":
    tk = Gui()