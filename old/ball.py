
height = float(input('inital height in meter: '))
sHeight = height
COR = float(input('The coefficient of restitution of a ball: '))
bounces = 0
distance = 0

#test cases
#12 .9 = 46 226.11
#100 .7 = 20 566.13

while height >= .10:
    bounces += 1
    tempHeight = height * COR
    if tempHeight >= .10:        
        distance += height * 2
        height *= COR
    else:
        break

distance -= sHeight
distance += height + height

print(f'{bounces:,.2f}')
print(f'{distance:,.2f}')   