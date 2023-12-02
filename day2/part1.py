import common


def main():

    viableSolutions = []

    for gameNumber, maxRed, maxGreen, maxBlue in common.parser():
        if maxRed <= 12 and maxGreen <= 13 and maxBlue <= 14:
            print(gameNumber, maxRed, maxGreen, maxBlue)
            viableSolutions.append(gameNumber)

    print(sum(viableSolutions))


if __name__ == "__main__":
    main()
