from tkinter import *
from TKBase import TKBase
from WishList import WishList
from re import match

# noinspection PyAttributeOutsideInit
class Gui (TKBase):
    def main(self) -> None:
        self.wList = WishList()

        #scenes
        self.mainScene = Frame(self.root)
        self.viewScene = Frame(self.root)
        self.changeScene = Frame(self.root)

        #variables
        self.currentFrame = self.mainScene
        self.editType = None


    #MAIN SCENE
        
        self.view = Button(self.mainScene, text= "View", command= lambda : self.multiFunc(lambda : self.switchFrames(self.viewScene), lambda : self.showWList(self.wList.view), lambda : self.outputView.set("")))
        self.addItem = Button(self.mainScene, text= "Add Item", command= lambda : self.multiFunc(lambda : self.switchFrames(self.changeScene), lambda : self.editFunc(True), self.clearInfo, lambda: self.outputChange.set(""), lambda : self.nameState(True)))
        self.exit = Button(self.mainScene, text= "Exit", command= lambda : self.multiFunc(self.wList.save, self.root.destroy))
        

    #VIEW SCENE

        #listboxes frames
        self.nameFrame = Frame(self.viewScene)
        self.quaFrame = Frame(self.viewScene)
        self.priceFrame = Frame(self.viewScene)
        self.favFrame = Frame(self.viewScene)

        #view's buttons frame
        self.rightFrame = Frame(self.viewScene)
        

        #Listboxes and labels
            #Order: Item, Quantity, Price, Favorite
        self.nameListLabel = Label(self.nameFrame, text= "Name")
        self.nameList = Listbox(self.nameFrame, height= 20, width= 10)

        self.quaListLabel = Label(self.quaFrame, text= "Quantity")
        self.quaList = Listbox(self.quaFrame, height= 20, width= 10)

        self.priceListLabel = Label(self.priceFrame, text= "Price")
        self.priceList = Listbox(self.priceFrame, height= 20, width= 10)

        self.favListLabel = Label(self.favFrame, text= "Favorite")
        self.favList = Listbox(self.favFrame, height= 20, width= 10)
        
        #view's buttons
        self.delItem = Button(self.rightFrame, text= "Delete Item", command= self.delFunc)
        self.updateItem = Button(self.rightFrame, text= "Update Item", command= self.updateFunc)

        self.sortLabel = Label(self.rightFrame, text= "Sort")
        self.sortFavVar = IntVar()
        self.fav = Checkbutton(self.rightFrame, variable= self.sortFavVar, text= "Favorite", command= self.sortFunc)
        self.sortPriceVar = IntVar()
        self.price = Checkbutton(self.rightFrame, variable= self.sortPriceVar, text= "Price", command= self.sortFunc)

        self.clear = Button(self.rightFrame, text= "Clear List", command= lambda : self.multiFunc(self.wList.clear, lambda : self.showWList(self.wList.view), self.wList.save))

        self.outputView = StringVar()
        self.outputLView = Label(self.rightFrame, textvariable= self.outputView) 

        self.exitView = Button(self.rightFrame, text= "Main Menu", command= lambda : self.switchFrames(self.mainScene))


    #ADD SCENE
        
        #entry boxes, labels, and variables
        self.nameLabel = Label(self.changeScene, text= "Name")  
        self.nameVar = StringVar() 
        self.nameInput = Entry(self.changeScene, textvariable= self.nameVar)

        self.quantityLabel = Label(self.changeScene, text= "Quantity")   
        self.quaVar = StringVar()
        self.quantityInput = Entry(self.changeScene, textvariable= self.quaVar)  

        self.priceLabel = Label(self.changeScene, text= "Price")  
        self.priceVar = StringVar()
        self.priceInput = Entry(self.changeScene, textvariable= self.priceVar)  

        self.favoriteLabel = Label(self.changeScene, text= "Favorite")   
        self.favVar = IntVar()
        self.favoriteInput = Checkbutton(self.changeScene, variable= self.favVar) 

        #buttons and output label
        self.changeButton = Button(self.changeScene, text= "Add/Update", command= self.changeFunc)


        self.outputChange = StringVar()
        self.outputLabel = Label(self.changeScene, textvariable= self.outputChange) 

        self.exitChange = Button(self.changeScene, text= "Main Menu", command= lambda : self.switchFrames(self.mainScene))

    #initial scene pack
        self.mainScene.pack()
        
    #main scene packing
        self.add(self.view,
        self.addItem,
        self.updateItem,
        self.exit)

    #view scene packing
        #frame packing
        self.add(self.nameFrame,
        self.quaFrame,
        self.priceFrame,
        self.favFrame, side= LEFT)
        self.rightFrame.pack(side= RIGHT)

        #listbox label packing
        self.add(self.nameListLabel,
        self.quaListLabel,
        self.priceListLabel,
        self.favListLabel, side= TOP)

        #listbox packing
        self.add(self.nameList,
        self.quaList,
        self.priceList,
        self.favList, side= LEFT)

        #view buttons packing
        self.add(self.delItem,
        self.updateItem,
        self.clear,
        self.sortLabel,
        self.fav,
        self.price,
        self.outputLView,
        self.exitView)

    #add scene packing
                                                         
        self.add(self.nameLabel,
        self.nameInput,
        self.quantityLabel,
        self.quantityInput,
        self.priceLabel,
        self.priceInput,
        self.favoriteLabel,
        self.favoriteInput,
        self.changeButton,
        self.outputLabel,
        self.exitChange)



#UTILITY METHODS
    
    #for all
    @staticmethod
    def multiFunc(*args):
        """
        Runs all arguments.
        :param args: All the functions you want to run.
        """
        for func in args:
            func()

    def switchFrames(self, newFrame: Frame):
        """
        Unpacks the self.currentFrame. Packs newFrame. Sets self.currentFrame to the newFrame.
        :param newFrame: The frame that is being switched with self.currentFrame.
        """
        self.currentFrame.pack_forget()
        self.currentFrame = newFrame
        self.currentFrame.pack()


    #for view scene
    def showWList(self, wList: dict):
        """
        Shows the current info from the given dictionary on the lightboxes.
        :param wList: The dictionary to be shown. In the format "item: [quantity, price, favorite]".
        """
        self.nameList.delete(0, END)
        self.quaList.delete(0, END)
        self.priceList.delete(0, END)
        self.favList.delete(0, END)

        i = 0
        for item in wList:
            self.nameList.insert(i, item)
            self.quaList.insert(i, wList[item][0]) 
            self.priceList.insert(i, f"${float(wList[item][1]):,.2f}")
            self.favList.insert(i, wList[item][2])
            i += 1

    def findClicked(self):
        """
        Finds the current item clicked on the lightboxes.
        :return: returns the name of the clicked item.
        """
        num = None

        for i in self.nameList.curselection():
            num = i

        for i in self.quaList.curselection():
            num = i

        for i in self.priceList.curselection():
            num = i

        for i in self.favList.curselection():
            num = i

        if num is not None:
            return self.nameList.get(num)
        return False


    #for add scene

    def clearInfo(self):
        """
        Resets all values in the entry boxes.
        """
        self.nameVar.set("")
        self.quaVar.set("")
        self.priceVar.set("")
        self.favVar.set(0)

    def editFunc(self, b: bool):
        """
        Changes the value of self.editType to b.
        :param b: self.editType new value.
        """
        self.editType = b

    def nameState(self, b: bool):
        """
        Disables or enables the name entry box.
        :param b: True, the box is enabled. False, the box is disabled.
        """
        if b:
            self.nameInput["state"] = "normal"
        else:
            self.nameInput["state"] = "disabled"
        
    def checkEntries(self) -> bool:
        """
        Checks for and sets output text to error. If any.
        :return: True, if there are no errors. False, if there is an error.
        """
        if self.nameVar.get() == "" or self.quaVar.get() == "" or self.priceVar.get() == "":
            self.outputChange.set("Missing information!")
        elif not self.quaVar.get().strip().isdigit():
            self.outputChange.set("Quantity must be an integer!")
        elif not match(r"^\$?\d*(\.\d+)?$", self.priceVar.get().strip()):
            self.outputChange.set("Price must be a positive float!")
        else:
            return False
        return True
    

#BUTTON METHODS
    
    def changeFunc (self):
        """
        Runs when the add/update button is clicked. Adds the information to self.wList.
        """
        if self.checkEntries():
            return

        #Item, Quantity, Price, Favorite
        itemName = self.nameVar.get().strip()
        val = [self.quaVar.get().strip(),
        self.priceVar.get().strip(),
        "True" if self.favVar.get() else "False"]

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

        self.wList.save()

    def sortFunc (self):
        """
        Runs when a sorting button is clicked. Chooses which type of sorted list will be shown.
        """
        if self.sortFavVar.get() and self.sortPriceVar.get():
            shownList = self.wList.sortPrice(fav= True)
        elif self.sortFavVar.get():
            shownList = self.wList.sortFav()
        elif self.sortPriceVar.get():
            shownList = self.wList.sortPrice()
        else:
            shownList = self.wList.view

        self.showWList(shownList)

    def updateFunc(self):
        """
        Runs when the update button is clicked. Switches to the change screen and puts it into the update mode.
        """
        if not (item := self.findClicked()):
            self.outputView.set("Click an item to update")
            return
        
        
        self.switchFrames(self.changeScene)
        self.editType = False
        self.clearInfo()

        self.nameVar.set(item)
        self.nameInput["state"] = "disabled"
        self.quaVar.set(self.wList.view[item][0])
        self.priceVar.set(self.wList.view[item][1])
        self.favVar.set(1 if self.wList.view[item][2] == "True" else 0)

        self.outputChange.set("")
        self.outputView.set("")


    def delFunc(self):
        """
        Runs when the delete button is clicked. Deletes the selected item and then shows the new list.
        """
        if not (item := self.findClicked()):
            self.outputView.set("Click an item to delete")
            return

        
        self.wList.deleteItem(item)
        self.showWList(self.wList.view)

        self.outputView.set("")

        self.wList.save()
        




    

    


        

if __name__ == "__main__":
    tk = Gui()
