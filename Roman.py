def main():
    get_change()


def get_change():
    x = 0
    wrong = 0
    while x <= 1000:
        attempt = str(roman_algorithm(x))
        good_attempt = str(algorithm(x))
        if len(attempt) > len(good_attempt):
            print(str(x) + " " + str(good_attempt))
            wrong += 1
        x += 1
    print("Total wrong " + str(wrong))


def algorithm(x):
    numbers = [1, 4, 5, 9]
    change = []
    y = x
    while y >= numbers[3]:
        z = y
        if z == 12:
            change.extend([4, 4, 4])
            return change
        elif z == 8:
            change.extend([4, 4])
            return change
        else:
            if z >= 0:
                y -= numbers[3]
                change.append(numbers[3])
    while y >= numbers[2]:
        z = y
        if z == 12:
            change.extend([4, 4, 4])
            return change
        elif z == 8:
            change.extend([4, 4])
            return change
        else:
            if z >= 0:
                y -= numbers[2]
                change.append(numbers[2])
    while y >= numbers[1]:
        z = y
        z -= numbers[1]
        if z >= 0:
            y -= numbers[1]
            change.append(numbers[1])
    while y >= numbers[0]:
        z = y
        z -= numbers[0]
        if z >= 0:
            y -= numbers[0]
            change.append(numbers[0])
    return change


def roman_algorithm(x):
    numbers = [1, 4, 5, 9]
    change = []
    y = x
    while y >= numbers[3]:
        z = y-numbers[3]
        if z >= 0:
            y -= numbers[3]
            change.append(numbers[3])
    while y >= numbers[2]:
        z = y-numbers[2]
        if z >= 0:
            y -= numbers[2]
            change.append(numbers[2])
    while y >= numbers[1]:
        z = y - numbers[1]
        if z >= 0:
            y -= numbers[1]
            change.append(numbers[1])
    while y >= numbers[0]:
        z = y - numbers[0]
        if z >= 0:
            y -= numbers[0]
            change.append(numbers[0])
    return change


main()
