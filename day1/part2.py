validDigits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def getLines():
    with open("cases.txt", "r") as file:
        lines = file.read().splitlines()
        return lines


def convert(digit: str):
    if digit == "one":
        return 1
    if digit == "two":
        return 2
    if digit == "three":
        return 3
    if digit == "four":
        return 4
    if digit == "five":
        return 5
    if digit == "six":
        return 6
    if digit == "seven":
        return 7
    if digit == "eight":
        return 8
    if digit == "nine":
        return 9

    if digit == "1":
        return 1
    if digit == "2":
        return 2
    if digit == "3":
        return 3
    if digit == "4":
        return 4
    if digit == "5":
        return 5
    if digit == "6":
        return 6
    if digit == "7":
        return 7
    if digit == "8":
        return 8
    if digit == "9":
        return 9


def main():
    lines = getLines()
    digits = []

    for line in lines:
        digit = getDigitFromLine(line)
        digits.append(digit)

    print(sum(digits))


def getDigitFromLine(line: str):
    first = getFirstDigit(line)
    last = getLastDigit(line)
    try:
        ans = int("{}{}".format(convert(first), convert(last)))
        return ans

    except Exception as e:
        print(e)
        print(line)
        print(f"First: {first}; Last: {last}")
        return 0


def getFirstDigit(line: str):
    for i in range(len(line)):
        if line[i].isdigit():
            return line[i]

        if line[i: i+3] in validDigits:
            return line[i: i+3]

        if line[i: i+4] in validDigits:
            return line[i: i+4]

        if line[i: i+5] in validDigits:
            return line[i: i+5]


def getLastDigit(line: str):
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return line[i]

        if line[i - 2: i + 1] in validDigits:
            return line[i - 2: i + 1]

        if line[i - 3: i + 1] in validDigits:
            return line[i - 3: i + 1]

        if line[i - 4: i + 1] in validDigits:
            return line[i - 4: i + 1]


if __name__ == "__main__":
    main()
