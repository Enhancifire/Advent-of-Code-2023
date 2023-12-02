def parser():
    lines = openFile()
    for line in lines:

        splitIndex = line.index(":")
        gameNumber = int(line[5: splitIndex])

        line = line[splitIndex + 1:]

        rounds = line.split(";")

        maxRed = 0
        maxGreen = 0
        maxBlue = 0
        for r in rounds:
            for i in r.split(","):
                indShow = i.split(" ")
                if indShow[-1] == "red":
                    maxRed = max(maxRed, int(indShow[-2]))

                if indShow[-1] == "green":
                    maxGreen = max(maxGreen, int(indShow[-2]))

                if indShow[-1] == "blue":
                    maxBlue = max(maxBlue, int(indShow[-2]))

        yield gameNumber, maxRed, maxGreen, maxBlue


def openFile():
    with open("cases.txt", "r") as f:
        lines = f.read().splitlines()
        return lines
