
#returns 2 dicts
    #letter: code
    #code: letter
def dicts():
    #letters
    abc = "abcdefghijklmnopqrstuvwxyz"
    #the coode for each letter
    code = r"@#$%^&*()_-+=/.,<>`~[]{}59"
    en = {abc[i]:code[i] for i in range(len(abc))}
    de = {code[i]:abc[i] for i in range(len(abc))}
    #returns encrypt dict and decrypt dict
    return en, de

#returns an opened file
def openFile():
    #makes sure file exists
    while True:
        try:
            return open(input("file name: "), "r")
        except FileNotFoundError:
            pass
    
#returns bool depending on if user inputs encrypt or decrypt
    #encrypt > True
    #decrypt > False
def enOrde():
    while True:
        anw = input("encrypt or decrypt: ").lower()
        if anw == "encrypt" or anw == "en":
            return True
        elif anw == "decrypt" or anw == "de":
            return False

def main ():
    #encrypt and dycrpt dicts
    en, de = dicts()
    #blank text
    text = ""
    with openFile() as file:
        #use encrypt or decrypt list, depending on user
        list = en if enOrde() else de
    
        for line in file:
            for char in line:
                if char in list:
                    #adds coded or decoded character
                    text += list[char.lower()]
                else:
                    #adds character if not in list
                    text += char

    #saves to user specified file
    with open(f"{input('new file name: ')}.txt", "w") as file:
        file.write(text)

    
if __name__ == "__main__":
    main()