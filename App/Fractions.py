import random


def level1():
    fractions = ["1/2", "1/3", "1/4", "1/5", "2/3", "3/4"]
    num = random.randint(0, 5)
    return fractions[num]


def level2():
    fractions = ["2/5", "3/5", "5/6", "4/5", "3/7", "2/7"]
    num = random.randint(0, 6)
    return fractions[num]


def level3():
    fractions = ["3/7", "4/7", "4/9", "5/6",
                 "5/8", "7/8", "3/8", "2/9", "1/8", "4/9"]
    num = random.randint(0, 9)
    return fractions[num]
