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
        self.addItem = Button(self.mainFrame, text= "addItem", command= lambda : self.multiFunc([lambda : self.switchFrames(self.changeFrame), lambda : self.editFunc(True), self.clearInfo, lambda: self.outputChange.set("")]))
        self.exit = Button(self.mainFrame, text= "save", command= self.save)
        

        #VIEW FRAME
        self.nameFrame = Frame(self.viewFrame)
        self.quaFrame = Frame(self.viewFrame)
        self.priceFrame = Frame(self.viewFrame)
        self.favFrame = Frame(self.viewFrame)
        self.rightFrame = Frame(self.viewFrame)

        #Item, Quantity, Price, Favorite
        self.nameLLabel = Label(self.nameFrame, text= "Name")
        self.nameList = Listbox(self.nameFrame, height= 20, width= 10)

        self.quaLLabel = Label(self.quaFrame, text= "Quantity")
        self.quaList = Listbox(self.quaFrame, height= 20, width= 10)

        self.priceLLabel = Label(self.priceFrame, text= "Price")
        self.priceList = Listbox(self.priceFrame, height= 20, width= 10)

        self.favLLabel = Label(self.favFrame, text= "Favorite")
        self.favList = Listbox(self.favFrame, height= 20, width= 10)

        self.delItem = Button(self.rightFrame, text= "Delete Item", command= self.delFunc)
        self.updateItem = Button(self.rightFrame, text= "Update Item", command= self.updateFunc)

        self.sortFavVar = IntVar()
        self.fav = Checkbutton(self.rightFrame, variable= self.sortFavVar, text= "Favorite", command= self.sortFunc)
        self.sortPriceVar = IntVar()
        self.price = Checkbutton(self.rightFrame, variable= self.sortPriceVar, text= "Price", command= self.sortFunc)

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
        self.add([self.nameFrame,
        self.quaFrame,
        self.priceFrame,
        self.favFrame,
        self.rightFrame], side= LEFT)

        self.add([self.nameLLabel,
        self.quaLLabel,
        self.priceLLabel,
        self.favLLabel], side= TOP)

        
        self.add([self.nameList,
        self.quaList,
        self.priceList,
        self.favList], side= LEFT)

        self.rightFrame.pack(side="right")
        self.add([ self.delItem,
        self.updateItem,
        self.fav,
        self.price,
        self.exitView])

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
        self.nameList.delete(0, END)
        self.quaList.delete(0, END)
        self.priceList.delete(0, END)
        self.favList.delete(0, END)

        i = 0
        for item in wList:
            self.nameList.insert(i, item)
            self.quaList.insert(i, wList[item][0]) 
            self.priceList.insert(i, wList[item][1])
            self.favList.insert(i, wList[item][2])
            i += 1


    def multiFunc(self, funcs: list):
        for func in funcs:
            func()

    def editFunc(self, b: bool):
        self.editType = b

    def checkVar(self, var):
        if var.get() == 1:
            return True
        else:
            return False
        
    def clearInfo(self):
        self.nameVar.set("")
        self.quaVar.set("")
        self.priceVar.set("")
        self.favVar.set(0)

    def findclicked(self):
        num = None

        for i in self.nameList.curselection():
            num = i

        for i in self.quaList.curselection():
            num = i

        for i in self.priceList.curselection():
            num = i

        for i in self.favList.curselection():
            num = i

        if num != None:
            return self.nameList.get(num)
        return False

    def checkEntries(self) -> bool:
        if self.nameVar.get() == "" or self.quaVar.get() == "" or self.priceVar.get() == "":
            self.outputChange.set("Missing information!")
        elif not self.quaVar.get().strip().isdigit():
            self.outputChange.set("Quantity must be an integer!")
        elif not match(r"^\$?\d*(\.\d+)?$", self.priceVar.get().strip()):
            self.outputChange.set("Price must be a positive float!")
        else:
            return False
        return True
    
    def changeFunc (self):

        if self.checkEntries():
            return

        #Item, Quantity, Price, Favorite
        itemName = self.nameVar.get().strip()
        val = [self.quaVar.get().strip(),
        self.priceVar.get().strip(),
        str(self.checkVar(self.favVar))]

        if self.editType:
            if self.wList.addItem(itemName, val):
                self.outputChange.set("Item added")
                self.clearInfo()
            else:
                self.outputChange.set("Item already exists!")            
        else:
            if self.wList.updateItem(itemName, val):
                self.outputChange.set("Item updated!")
            else:
                self.outputChange.set("Item Doesn't exist")

    def sortFunc (self):
        shownList = None
        if self.checkVar(self.sortFavVar) and self.checkVar(self.sortPriceVar):
            shownList = self.wList.sortPrice(fav= True)
        elif self.checkVar(self.sortFavVar):
            shownList = self.wList.sortFav()
        elif self.checkVar(self.sortPriceVar):
            shownList = self.wList.sortPrice()
        else:
            shownList = self.wList.view

        self.showWList(shownList)

    def updateFunc(self):
        if (item := self.findclicked()) == False:
            return
        
        self.switchFrames(self.changeFrame)
        self.editType = False
        self.clearInfo()

        self.nameVar.set(item)
        self.nameInput["state"] = "disabled"
        self.outputChange.set("")

    def delFunc(self):
        if (item := self.findclicked()) == False:
            return

        self.wList.deleteItem(item)
        self.showWList(self.wList.view)

    def save(self):
        self.wList.save()
        self.root.destroy()
        




    

    


        

if __name__ == "__main__":
    tk = Gui()