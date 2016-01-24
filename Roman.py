def main():
    get_change()


def get_change():
    x = 0
    wrong = 0
    while x <= 1000:
        attempt = str(algorithm(x))
        good_attempt = str(good_test(x))
        if len(attempt) > len(good_attempt):
            print(str(x) + " " + str(good_attempt))
            wrong += 1
        x += 1
    print("Total wrong " + str(wrong))


def good_test(x):
    y = x
    a = algorithm(x)
    b = breakdown_1(y)
    c = breakdown_2(y)
    d = breakdown_3(y)
    if len(a) < (len(b) or len(c) or len(d)):
        return a
    if len(b) < (len(a) or len(c) or len(d)):
        return b
    if len(c) < (len(a) or len(b) or len(d)):
        return c
    if len(d) < (len(a) or len(b) or len(c)):
        return d
    if len(a) == (len(b) or len(c) or len(d)):
        return a


def algorithm(x):
    numbers = [1, 4, 5, 9]
    change = []
    y = x
    while y >= numbers[3]:
        z = y
        z -= numbers[3]
        if z >= 0:
            y -= numbers[3]
            change.append(numbers[3])
    while y >= numbers[2]:
        z = y
        z -= numbers[2]
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


def breakdown_1(x):
    numbers = [1, 4, 5]
    change = []
    y = x
    while y >= numbers[2]:
        z = y
        z -= numbers[2]
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


def breakdown_2(x):
    numbers = [1, 4]
    change = []
    y = x
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


def breakdown_3(x):
    numbers = [1]
    change = []
    y = x
    while y >= numbers[0]:
        z = y
        z -= numbers[0]
        if z >= 0:
            y -= numbers[0]
            change.append(numbers[0])
    return change


main()
