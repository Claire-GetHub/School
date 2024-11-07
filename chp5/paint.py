import math

def main():
    #get user input
    sFeet = float(input("how many square feet? "))
    paintPrice = float(input("price of paint per gallon? "))

    #Get all the values
    paint = paintAmount(sFeet)
    paintC = paintCost(paint, paintPrice)
    hours = time(paint)
    hoursC = laborCost(hours)
    total = hoursC + paintC

    #print everything
    print(f"gallons of paint: {paint:,.0f}\nlabor hours: {hours:,.0f}\ncost of paint: {paintC:,.2f}\nlabor charges: {hoursC:,.2f}\ntotal cost: {total:,.2f}")

def paintCost(amount, price):
    #gallons of paint times thier price
    return amount * price

def paintAmount(sFeet):
    #amount of paint divided by how much a gallon would cover. Uses ceil because you cant buy part of a gallon of paint
    return math.ceil(sFeet/112)

def laborCost(hours):
    #the amount of hours times what each hour costs
    return hours * 35

def time(paint):
    #using the amount of paint to calcutate the hours. ceiling because im not working for free even if it is 10 minutes.
    return math.ceil(paint * 8) #Others ways I tried -> sFeet/14 #(sFeet/112) * 8 


main()