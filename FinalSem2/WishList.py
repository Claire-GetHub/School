import csv

class WishList:

    def __init__(self):
        self.__fileName = "wishList.csv"
        self.__wList = self.__create()


    def __create(self) -> dict:
        """
        creates a dictionary of all items in "wishList.csv". Will create "wishList.csv" if it does not exsit.

        :returns: a disctionary with all the information from wishlist. Stored in the format: "item: [quantity, price, favorite]"
        """

        wList = {}
        with open(self.__fileName, "w+") as csvfile:
            #makes it readable
            reader = csv.DictReader(csvfile)
            #the headers of the csv file
            headers = ['Item','Quantity','Price','Favorite']
            #turns into the format I want
            for row in reader:
                #create a new key in the dict named the items name then create a list with the rest of the items values
                wList[row[headers[0]]] = [row[headers[1]],row[headers[2]], row[headers[3]]]

            return wList
        
    #saves wList to a csv file and exits program
    def save(self):
        """
        Writes the current wish list to "wishList.csv" 
        """
        with open(self.__fileName, "w") as after:
            #makes it dict writable
            writer = csv.DictWriter(after, fieldnames=['Item','Quantity','Price','Favorite'])
            #writes the heading
            writer.writeheader()
            for item in self.__wList:
                #writes down each row
                writer.writerow({'Item': item, 'Quantity': self.__wList[item][0], 'Price': self.__wList[item][1], 'Favorite': self.__wList[item][2]})
    
    def clear(self):
        """
        clears all items from the wishlist.
        """
        self.__wList = {}

    #add a user specified            
    def addItem(self, item: str, values: list) -> bool:
        """
        add an item to the wishlist

        :param item: the name of the item you want to create
        :param values: a list of the values. In the format: "[quantity, price, favorite]"

        :returns: a bool that shows whether the updating was successful or not
        """        

        #check if it exists
        if item in self.__wList.keys():
            return False
        #if it doesnt adds it with base values
        else: 
            self.__wList[item] = values
            #returns false so nothing is printed
            return True
        

    def updateItem(self, item: str, values: list):
        """
        update an item from the wishlist

        :param item: the name of the item you want to update
        :param values: a list of the new values. In the format: "[quantity, price, favorite]"

        :returns: a bool that shows whether the updating was successful or not
        """        
        #check if it exists
        if item in self.__wList.keys():
            return False
        #if it doesnt adds it with base values
        else: 
            self.__wList[item] = values
            #returns false so nothing is printed
            return True
        
    def deleteItem(self, item: str) -> bool:
        """
        removes an itemm from the wishlist

        :returns: a bool that shows whether the deleting was successful or not
        """

        if item in self.__wList.keys():
            #deletes item
            del self.__wList[item]
            #returns sucess
            return True
        else:
            #returns failed
            return False 
        
    @property  
    def view(self) -> dict:
        return self.__wList

        
    
            
