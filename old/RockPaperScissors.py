
import random

def main():
    print('Rock','paper','scissors', 'SHOOT!', sep= '\n')
    choices = ['rock', 'paper', 'scissors']

    user = input('').lower().strip()
    computer = random.choice(choices)

    print(f'{user} vs {computer}')

    if user == computer:
        print('You tied!')
    elif (user == 'rock' and computer == 'paper') or (user == 'paper' and computer == 'scissors') or (user == 'scissors' and computer == 'rock') :
        print('computer wins!')
    else:
        print('user wins!')

    

if __name__ == "__main__":
    main()

    

