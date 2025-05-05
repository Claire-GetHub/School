import math

number = int(input('num > 1: '))
flag = True
num = number


primeFactors = []


def prime(num):
    for n in range(2, int(math.sqrt(num)) + 1):
        if num % n == 0:
            return False
    return True
    
def factor(number):
    for n1 in range(2, number + 1):
        for n2 in range(2, number + 1):
            if n1 * n2 == number:
                return [n1, n2]
    return [1, number]

        
while flag:
    factors = factor(num)
    primes = 0
    for n in factors:
        if prime(n):
            primes += 1
            if not(n == 1):
                primeFactors.append(n)

            if primes == 2:
                flag = False
                break
        elif not(n == 1):
            num = n

print(primeFactors)
        