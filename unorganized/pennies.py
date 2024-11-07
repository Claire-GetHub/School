
days = int(input('amount of days: '))
fAmount = 0
allDays = []
add = .01

for n in range(days):
    dayAmount = (add := add * 2)
    fAmount += dayAmount
    allDays.append(dayAmount)

for i in range(len(allDays)):

    print(f'day {(i + 1)}: {allDays[i]:,.2f}')

print(f'{fAmount:,.2f}')