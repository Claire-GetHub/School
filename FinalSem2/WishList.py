import csv
from os.path import exists

class WishList:

    def __init__(self):
        self.__fileName = "wishList.csv"
        self.__wList = self.__create()


    def __create(self) -> dict:
        """
        creates a dictionary of all items in "wishList.csv". Will create "wishList.csv" if it does not exsit.

        :returns: a disctionary with all the information from wishlist. Stored in the format: "item: [quantity, price, favorite]"
        """
        if not exists(self.__fileName):
            return {}

        wList = {}
        with open(self.__fileName, "r") as csvfile:
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
                try:
                    writer.writerow({'Item': item, 'Quantity': self.__wList[item][0], 'Price': self.__wList[item][1], 'Favorite': self.__wList[item][2]})
                except UnicodeEncodeError:
                    writer.writerow({'Item': "NAME ERROR", 'Quantity': self.__wList[item][0], 'Price': self.__wList[item][1], 'Favorite': self.__wList[item][2]})
    
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
            self.__wList[item] = values
            return True
        #if it doesnt adds it with base values
        else:  
            return False
        
    def deleteItem(self, item: str) -> bool:
        """
        removes an item from the wishlist

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
        
    def sortFav(self) -> dict:
        """
        returns a dictionary with only contains favorites

        :returns: a dict that only contains favorites. In the format: "item: [quantity, price, favorite]"
        """
        fav = {}

        for item in self.__wList:
            #the 2nd value in each items list is a boolean. Whether its a favorite or not
            if self.__wList[item][2] == "True":
                #if it is a favorite add it to the fav list
                fav[item] = self.__wList[item]
        #return fav to be printed
        return fav
    
    def sortPrice(self, lowest: bool = True, fav: bool = False) -> dict:
        """
        returns a dictionary sorted by price

        :param lowest: sorts lowest to highest if True. Sorts highest to lowest if False.

        :returns: a dict that is sorted by price. In the format: "item: [quantity, price, favorite]"
        """

        l = self.sortFav() if fav else self.__wList

        listDict = [[item, l[item][0], float(l[item][1]), l[item][2]] for item in l]

        listDict.sort(key=self.__price)
        
        return {lst[0]: [lst[1],lst[2],lst[3]] for lst in listDict}

    @staticmethod
    def __price(lst):
        return lst[2]
        

    def __sortPrice(self, lowest: bool = True, fav: bool = False) -> dict:
        """
        returns a dictionary sorted by price

        :param lowest: sorts lowest to highest if True. Sorts highest to lowest if False.

        :returns: a dict that is sorted by price. In the format: "item: [quantity, price, favorite]"
        """
        l = self.sortFav() if fav else self.__wList

        #new dictionary
        #price: item name
        keys = l.keys()
        prices = {float(l[item][1]): item for item in keys}
        #list of prices
        keys = list(prices.keys())
        #sorts prices
        keys.sort()
        #creates sorted dictionary
            #item name: price
        sd = {prices[i]: i for i in keys}

        #list of items
        keys = sd.keys()
        if not lowest:
            keys.reverse()
        #creates new dictionary
            #item name: [item values from wList]
        nd = {i:l[i] for i in keys}

        
        return nd
        

        
    @property  
    def view(self) -> dict:
        return self.__wList



    
            
