def Counting_bits(number: int):
    binary = str(bin(number))
    length = len(binary)
    splitted = binary[2:length]
    new_array = []
    for i, char in enumerate(splitted):
        if char == "1":
            new_array.append(int(i + 1))


    new_array.insert(0, len(new_array))
    return new_array


def main():
    count = Counting_bits(161)
    count

main()