from functions import *

# lets user create a savable wish list, including item name, quantity, 

def main ():
    #initialize wList
    createList(check())
    #keeps opening menu
    while True:
        #if the value of output is False dont print
        if (output := menu()):
            #otherwise print the output
            print(f"\n{output}")



if __name__ == "__main__":
    main()