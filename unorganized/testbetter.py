
def main():
    x = getInt("What's x? ")
    print(f"x is {x}")


def getInt(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

    
main()