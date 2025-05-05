
years = int(input('Period of years '))
fRain = 0
fAmount = 0

for n in range(years):
    for n in range(12):
        month = int(input(f'rainn for month {n} '))
        fRain += month
        fAmount += 1

average = fRain/fAmount

print(f'the average rainfall is {average}')