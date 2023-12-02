import common


def main():

    viableSolutions = []
    powerOfSet = []

    for gameNumber, maxRed, maxGreen, maxBlue in common.parser():
        # if maxRed <= 12 and maxGreen <= 13 and maxBlue <= 14:
        #     # print(gameNumber, maxRed, maxGreen, maxBlue)
        #     viableSolutions.append(gameNumber)

        print(maxGreen * maxBlue * maxRed)
        powerOfSet.append(maxRed * maxBlue * maxGreen)

    # print(sum(viableSolutions))
    print(sum(powerOfSet))


if __name__ == "__main__":
    main()
