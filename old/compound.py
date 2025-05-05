P = float(input('amount in account '))
r = float(input('intrest '))
n = float(input('copound frequency '))
t = float(input('time in years '))


A = P*(1+((r/100)/n))**(n*t)
print(round(A,2))