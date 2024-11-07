
def main():
    #get seating for each class
    classA = int(input("Class A Seats: "))
    classB = int(input("Class B Seats: "))
    classC = int(input("Class C Seats: "))
    #call function and print return
    print(f"Income: {income(classA, classB, classC)}")

def income(a, b, c):
    #multiplies amount of tickets by thier price
    return (a*20) + (b*15) + (c*10)

main()