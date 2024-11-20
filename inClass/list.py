import random

def winner():
    names = ["h","j","c"]
    #can be multiple
    winner = random.choices(names, k=2)
    #one value
    winner = random.choice(names)
    print(winner)

def write():
    with open("cities.txt", "w") as file:
        for city in ["New York", "Dallas", "Tokyo"]:
            file.write(city + "\n")

def read():
    with open("cities.txt", "w") as file:
        cities = file.readlines
        for i in range(cities):
            cities[i] = cities[i].strip("\n")
