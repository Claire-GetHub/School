import sys
import csv

#global. It is used throughout each function
wList = {}

#checks if there is a already made file
def check():
    try:
       file = open("wishList.csv", "r")
    except FileNotFoundError:
        #returns false so create list doesnt run
        return False
    else:
        #returns the file so createList can create the list from the function
        return file

#add everything from a csv file to wList
def createList(file):
    #parameters
        #file: is either the wishList file or False
    #checks if file is actual the file
    if file:
        with file as csvfile:
            #makes it readable
            reader = csv.DictReader(csvfile)
            #the headers of the csv file
            headers = ['Item','Quantity','Price','Favorite']
            #turns into the format I want
            for row in reader:
                #create a new key in the dict named the items name then create a list with the rest of the items values
                wList[row[headers[0]]] = [row[headers[1]],row[headers[2]], row[headers[3]]]

#view wList in format
def view():
    #checks if the dict is empty
    if len(wList) > 0:
        #returns the formated dict to be printed
        return tabulate(wList)
    else:
        #returns the error message to be printed
        return "Your wish list is empty."

#add a user specified            
def addItem():
    #the name of the item they want to add
    item = input("Enter the name of the item to add: ")

    #check if it exists
    if item in wList.keys():
        return f"{item} already exists in your wish list."
    #if it doesnt adds it with base values
    else: 
        wList[item] = [0,0.0,False]
        #returns false so nothing is printed
        return False

#update a user specified
def updateItem():
    #the name of the item to be updated
    item = input("Enter the name of the item to update: ")
    #checks if it exists
    if item in wList.keys():
        #current values
        print(f"Current values for {item}: qty={wList[item][0]}, price={wList[item][1]}, favorite={wList[item][2]}")
        #new values
        quan = checkFloat("Enter the new quantity: ")
        price = checkFloat("Enter the new price: ")
        fav = checkYesNo()
        #adds values
        wList[item] = [quan, price, fav]
        #returns the success
        return f"{item} updated successfully."
    else:
        #returns error to be printed
        return f"{item} is not in your wish list."

#returns a float   
def checkFloat(str):
    #parameters
        #str: the user prompt
    while True:
        try:
            return float(input(str))
        except ValueError:
            pass

#returns true or false
def checkYesNo():
    while True:
        anw = input("Is it a favorite? (yes/no):  ")
        if anw.lower() == "yes":
            return True
        elif anw.lower() == "no":
            return False

#delete a user specified
def deleteItem():
    #the name of the item to be deleted
    item = input("Enter the name of the item to delete: ")
    #checks if item exists
    if item in wList.keys():
        #deletes item
        del wList[item]
        #returns sucess
        return f"{item} has been removed from your wish list"
    else:
        #returns error
        return f"{item} is not in your wish list"

#new dict that is sorted from lowest price to highest price
def sortPrice():
    #creates dict
        # price: item name
    prices = {}
    for item in wList:
        prices[float(wList[item][1])] = item
        
    #list of prices
    keys = list(prices.keys())
    #sorts prices
    keys.sort()
    #creates sorted dictionary
        #item name: price
    sd = {prices[i]: i for i in keys}

    #list of items
    keys = sd.keys()
    #creates new dictionary
        #item name: [item values from wList]
    nd = {i:wList[i] for i in keys}

    #code to turn wList into the sorted list
    #clear()
    #for item in nd:
    #    wList[item] = nd[item]

    #returns new dict to be printed
    return tabulate(nd)

#creates new dict with only favorites
def sortFav():
    fav = {}

    for item in wList:
        #the 2nd value in each items list is a boolean. Whether its a favorite or not
        if wList[item][2] == "True":
            #if it is a favorite add it to the fav list
            fav[item] = wList[item]
    #return fav to be printed
    return tabulate(fav)

#clear wList
def clear():
    #for each item in a copy of wList
    for item in wList.copy():
        #delete the item
        del wList[item]

#saves wList to a csv file and exits program
def exitSave():
    with open("wishList.csv", "w") as after:
        #makes it dict writable
        writer = csv.DictWriter(after, fieldnames=['Item','Quantity','Price','Favorite'])
        #writes the heading
        writer.writeheader()
        for item in wList:
            #writes down each row
            writer.writerow({'Item': item, 'Quantity': wList[item][0], 'Price': wList[item][1], 'Favorite': wList[item][2]})

    sys.exit()

#turns a special type of dictionary into a string with specific formate
def tabulate(list):
    #parameters
        #list: a dictionary that has a list for each key
    
    headers = ["Item","Quantity","Price","Favorite"]

    #heading. uses spaces() so its not so long
    text = f"{headers[0]}\
            {spaces(20)}\
            {headers[1]}\
            {spaces(11)}\
            {headers[2]}\
            {spaces(19)}\
            {headers[3]}"

    #adds a line for each item in list
    for item in list:
        #so spacing is correct
        itemSpaces = 24 - len(item)
        quantitySpaces = 19 - len(str(list[item][0]))
        priceSpaces = 24 - len(str(list[item][1]))

        #adds item, the items quatity, the items price, and if its a favorite. 
        #adds the correct spacing in between each
        text += f"\n{item}\
            {spaces(itemSpaces)}\
            {list[item][0]}\
            {spaces(quantitySpaces)}\
            {list[item][1]}\
            {spaces(priceSpaces)}\
            {list[item][2]}"
    return text

#returns an amount of spaces decided by num
def spaces (num):
    text = ""
    for i in range(num):
        text += " "
    return text


#name of each funtion so we can run them
choices = ["index 0", view, addItem, updateItem, deleteItem, sortPrice, sortFav, clear, exitSave]

def menu():
    #the printed menu
    print(f"\nWelcome to the Shopping Wish List!\n\n\
    1. View Wish List\n\
    2. Add an Item\n\
    3. Update an Item\n\
    4. Delete an item\n\
    5. Sort Wish List by Price\n\
    6. Sort Wish List by Favorites\n\
    7. Clear Wish List\n\
    8. Exit & Save\n")

    #your choice
    choice = input("Enter your choice: ")
    #spacing because it loos nice
    print("")
    #if its a value in the choices list
    if choice.isdigit() and 9 > int(choice) > 0:
        #runs the choosen function and returns what the funtion returns
        return choices[int(choice)]()
