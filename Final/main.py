from functions import *


def main ():
    #initialize wList
    createList(check())
    #keeps opening menu
    while True:
        #if the value of output is False dont print
        if (output := menu()):
            #otherwise print the output
            print(output)
    


if __name__ == "__main__":
    main()
