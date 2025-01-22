

def dicts():
    abc = "abcdefghijklmnopqrstuvwxyz"
    code = r"@#$%^&*()_-+=/.,<>`~[]{}59"
    en = {abc[i]:code[i] for i in range(len(abc))}
    de = {code[i]:abc[i] for i in range(len(abc))}
    return en, de

def openFile():
    while True:
        try:
            return open(input("file name: "), "r")
        except FileNotFoundError:
            pass
    

def enOrde():
    while True:
        anw = input("encrypt or decrypt: ").lower()
        if anw == "encrypt" or anw == "en":
            return True
        elif anw == "decrypt" or anw == "de":
            return False

def main ():
    en, de = dicts()
    text = ""
    with openFile() as file:
        list = en if enOrde() else de
    
        for line in file:
            for char in line:
                if char in list:
                    text += list[char.lower()]
                else:
                    text += char
    
    with open(f"{input('new file name: ')}.txt", "w") as file:
        file.write(text)

    




if __name__ == "__main__":
    main()
