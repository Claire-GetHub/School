from openpyxl import *

def main():
    wb = load_workbook("testing.xlsx")


    sheet = wb["Sheet1"]

    for row in sheet["AF1":"BF1"]:
        for cell in row:
            print(utils.column_index_from_string(alpha(cell.coordinate)))


    wb.save("testing.xlsx")


def alpha(s):
    letters = ""
    for char in s:
        if char.isalpha():
            letters += char
    return letters

if __name__ == "__main__":
    main()