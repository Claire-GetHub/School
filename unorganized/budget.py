import re

budget = int(re.sub("[^0-9]", "", input('Your budget for this month ')))


sAmount = 0
exFlag = True
askFlag = True
exNum = 1

while exFlag:
    amount = int(re.sub("[^0-9]", "", input('How many expenses do you have? ')))

    for n in range(1, amount + 1):
        num = int(re.sub("[^0-9]", "", input(f'expense {exNum} ')))
        sAmount += num
        exNum += 1

    while askFlag:
        more = input('Do you have more expenses? y/n ').lower()
        if more == 'y':
            askFlag = False
        elif more == 'n':
            exFlag = False
            askFlag = False

fAmount = budget - sAmount

print(f'you are {fAmount} over/under your budget')