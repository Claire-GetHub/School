
#opens 2 files
def openFiles():
    while True:
        try:
            return open(input("file name 1: "), "r"), open(input("file name 2: "), "r")
        except FileNotFoundError:
            pass
            
#turn the file into a set. Each word being a value
def fileToSet(file):
    list = []
    for line in file:
        list += line.split()
    return set(list)

def main():
    #get both files
    file1, file2 = openFiles()
    #turn themm both to sets
    set1, set2 = fileToSet(file1), fileToSet(file2)

    #all unique words
    print(set1 ^ set2)
    #all words in both files
    print(set1 & set2)
    #all words in file1 and not file2
    print(set1 - set2)
    #all words in file2 and not file1
    print(set2 - set1)
    #all words not in both files
    print(set1 ^ set2)
  
    

if __name__ == "__main__":
    main()
