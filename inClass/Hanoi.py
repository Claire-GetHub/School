

def step (n,fr,to,temp):
    """
    :param n: amount of discs
    """
    print(f"from: {fr}\nto: {to}\ntemp: {temp}")
    if n == 1:
        print("Solved.")
    elif True:
        step(n-1,1,2,3)
    elif True:
        step(n-1,2,3,1)

step(3,1,3,2)