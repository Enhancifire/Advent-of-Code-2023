def getLines():
    with open("test_case.txt", "r") as file:
        lines = file.read().splitlines()
        return lines


def main():
    digits = []
    lines = getLines()
    for line in lines:
        first = findFirstDigit(line)
        last = findLastDigit(line)

        digits.append(int(f"{line[first]}{line[last]}"))

    print(sum(digits))


def findFirstDigit(line):
    for i in range(len(line)):
        if line[i].isdigit():
            return i


def findLastDigit(line):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return i


if __name__ == "__main__":
    main()
