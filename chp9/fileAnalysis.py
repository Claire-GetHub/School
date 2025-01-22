

def openFiles():
    while True:
        try:
            return open(input("file name 1: "), "r"), open(input("file name 2: "), "r")
        except FileNotFoundError:
            pass

def fileToSet(file):
    list = []
    for line in file:
        list += line.split()
    return set(list)

def main():
    file1, file2 = openFiles()
    set1, set2 = fileToSet(file1), fileToSet(file2)
    
    print(set1 ^ set2)
    print(set1 | set2)
    print(set1 - set2)
    print(set2 - set1)
    print(set1 ^ set2)
  
    

if __name__ == "__main__":
    main()