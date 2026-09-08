# Shared Arabic values and matching Roman symbols, largest first so
# subtractive pairs (CM, CD, XC, XL, IX, IV) are applied before single letters.
ARABIC = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
ROMAN = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]


def to_roman(number: int) -> str:
    blob = number
    final = []

    for value, symbol in zip(ARABIC, ROMAN):
        while blob >= value:
            final.append(symbol)
            blob = blob - value
            print(symbol)
    return("".join(final))



def romanizer(numbers):
    return [to_roman(n) for n in numbers]


def main():
    numbers = [1, 49, 23]
    converted = romanizer(numbers)
    print(converted)  # ["I", "XLIX", "XXIII"]

    # print(arabic_to_roman(49))  # XLIX


if __name__ == "__main__":
    main()
