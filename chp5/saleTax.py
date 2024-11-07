
def main ():

    #get price from user
    amount = float(input("Price: "))
    #find amount needed to tax
    state = stateTax(amount)
    county = countyTax(amount)

    #print all the information
    print(f"\nBefore Tax: {amount}\nState Tax: {state:.2f}\nCounty Tax: {county:.2f}\nTotal Tax: {(total := state + county):.2f}\nTotal: {total + amount}")

def stateTax (price):
    #state tax is 5%
    return price * 0.05

def countyTax(price):
    #county tax is 2.5%
    return price * 0.025

main()