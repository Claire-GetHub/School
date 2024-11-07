n1 = int(input('whole number 1: '))
n2 = int(input('whole number 2: '))

greater = n1 if n1 > n2 else n2

for n in range(greater, 1, -1):
    if n1 % n == 0 and n2 % n == 0:
        print(f'Greatest Common Divisor: {n}')
        break
else:
    print('No greatest common divisor')