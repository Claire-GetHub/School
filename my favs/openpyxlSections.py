def sections(sheet, start = "A1", end = "C3", color1 = "E7E6E6", color2 = "C9C9C9"):
    flag = True
    colored = False
    for row in sheet[start:end]:
        color = color1 if flag else color2
        for cell in row:
            if cell.fill.start_color.index == "00000000":
                if colored:
                    flag = not flag
                    colored = False
                break
            else:
                sheet[cell.coordinate].fill = PatternFill(patternType='solid', fgColor=color)
                colored = True
