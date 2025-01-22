
def main():
    accNums = fileToList("charAcc.txt")
    accNum = input("account number: ")
    
    if accNum in accNums:
        print("num is valid")
    else:
        print("num is invalid")



def fileToList(file):
    list = []
    with open(file, "r") as file:
        for line in file:
            list.append(line.strip("\n"))
    return list


main()