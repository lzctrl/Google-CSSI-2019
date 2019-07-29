import random

def longest_word(a, b, c):
    if len(a) > len(b) and len(a) > len(b):
        return a
    elif len(b) > len(a) and len(b) > len(c):
        return b
    else:
        return c

print(longest_word("first", "second", "third"))


def reverse_string(word):
    newWord = ""
    for i in word:
        newWord = i + newWord
    return newWord

print(reverse_string("chicken dinner"))


def sum_to_n(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    return sum

print(sum_to_n(4))


def is_triangle(s1, s2, s3):
    if s1 + s2 > s3 or s2 + s3 > s1 or s3 + s1 > s2:
        return True
    else:
        return False

print(is_triangle(3, 4, 2))
print(is_triangle(0, 0, 0))


def roll_dice(numRolls):
    iterations = 1
    perfectRoll = numRolls * 6
    totalSum = roll(numRolls, perfectRoll)

    while totalSum != perfectRoll:
        totalSum = roll(numRolls, perfectRoll)
        iterations += 1

    return "That took " + str(iterations) + " iterations to get a perfect roll of " + str(perfectRoll)

def roll(numRolls, perfectScore):
    sum = 0
    for i in range(0, numRolls):
        numRolled = random.randint(1, 6)
        sum += numRolled
    print(sum)
    return sum


print(roll_dice(5))
