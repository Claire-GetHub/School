word = input("Enter a word: ")
amount = int(input('Enter a number: '))


left = amount - 1
right = 0

for n in range(amount):
    
    for n in range(left):
        print("-", end= " ")

    print(f'{word}' ,end="")

    for n in range(right):
        print(" -", end= "")

    print("\n", end= "")
    left -= 1
    right += 1