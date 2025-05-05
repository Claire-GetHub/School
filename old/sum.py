
amount = 0
num = int(input('input number, input a negative number to stop '))

while num > 0:
    amount += num
    num = int(input('input number, input a negative number to stop '))

print(amount)