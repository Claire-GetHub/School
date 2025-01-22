


def main():
    winners = {}
    with open("WorldSeriesWinners.txt", "r") as file:
        for line in file:
            line = line.strip("\n")
            if line in winners:
                winners[line] += 1
            else:
                winners[line] = 0

    print(winners)


if __name__ == "__main__":
    main()