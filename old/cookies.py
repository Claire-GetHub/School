
SUGAR = 0.03125
BUTTER = 0.02083333333
FLOUR = 0.05729166666

amount = float(input('How many cookies do you want? '))



def cookieAmount (amount):

    sugarAmount = SUGAR * amount
    butterAmount = BUTTER * amount
    flourAmount = FLOUR * amount

    if sugarAmount > 1 :
        sugarCup = 'cups'
    else:
        sugarCup = 'cup'

    if butterAmount > 1 :
        butterCup = 'cups'
    else:
        butterCup = 'cup'

    if flourAmount > 1 :
        flourCup = 'cups'
    else:
        flourCup = 'cup'


    ingredients = f'sugar: {sugarAmount:,.2f} {sugarCup} \nbutter: {butterAmount:,.2f} {butterCup} \nflour: {flourAmount:,.2f} {flourCup}'

    return ingredients



print(cookieAmount(amount))