
def main ():
    #Gets input, sends it to function, then prints
    print(f'Miles = {convert(float(input("Kilos: "))):.2f}')

def convert(kilos):
    #to get from kilos to miles
    return kilos * 0.6214

main()