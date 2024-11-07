
def main ():
    valid = False
    while not(valid):
        guess = int(input('Number between 1 & 10 '))
        if guess > 0 and guess <= 10:
            print(guess)
            valid = True
        else:
            print('Enter a valid number')

main()