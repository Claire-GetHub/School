
def main():
    #get amount from user
    replaceAmount = float(input("Cost to replace: "))
    #calls function then prints return
    print(f"Minimum Insurance: {minInsurance(replaceAmount):,.2f}")

def minInsurance(amount):
    # amount * 80% to get how much they should insure the building for
    return amount * .8

main()