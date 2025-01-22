
def main():
    string, list = check(input("your answers: "))
    print(string)
    print(list)



def check(anwsers):
    correct = 0
    incorrect = []
    corAnwsers = "ACAADBCACBADCADCBBDA"
    for i in range(len(corAnwsers)):
        if anwsers[i].upper() == corAnwsers[i]:
            correct += 1
        else:
            incorrect.append(i)
    return f"Correct: {correct}\nIncorrect: {len(incorrect)}", incorrect

main()