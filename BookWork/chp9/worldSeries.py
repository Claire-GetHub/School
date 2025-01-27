


def main():
    #uses functions to make each variable
    year = isInt()
    yearwin = years()
    amountwin = wins()

    if year in yearwin:
        print(yearwin[year])
        print(amountwin[yearwin[year]])
    else:
        print("none")


def isInt():
    #makes sure year is an int
    while True:
        try:
            return int(input("year: "))
        except ValueError:
            pass

# returns a dict
    #year: winner of that year
def years():

    winners = {}
    #the years not played
    notPlayed = [1904, 1994]
    #current year
    year = 1903
    with open("WorldSeriesWinners.txt", "r") as file:
        #file has a team on each line 
        for line in file:
            #if the year wasnt played go to the next year
            if year in notPlayed:
                year += 1
                continue
            else:
                #add the year and the winner of that year
                winners[year] = line.strip("\n")
            #increment years
            year += 1
        #return the dictionary
            #year: winner of that year
        return winners

# returns a dict
    #winner: amount of wins
def wins ():
    winners = {}
    with open("WorldSeriesWinners.txt", "r") as file:
        #file has a team on each line
        for line in file:
            #i dont want \n in my dict
            line = line.strip("\n")
            #if team is already in winners increment the wins
            if line in winners:
                winners[line] += 1
            #otherwise add them to the dict
            else:
                winners[line] = 0
    #return the dict
        #winner: amount of wins
    return winners


if __name__ == "__main__":
    main()
