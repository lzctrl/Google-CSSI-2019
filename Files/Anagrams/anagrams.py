import random

# phraseScramble = raw_input("Phrase to scramble (or Enter to quit)? ")
# maxNum = int(raw_input("Max words to include (Enter for none)? "))

def grabText(filename):
    with open(filename) as f:
        content = ' '.join([line.replace('\n', '') for line in f.readlines()])
        return content

file = grabText("dict1.txt").split('\r ')

# phraseScramble.strip(' ')
phraseSorted = []
phraseScramble = "barbara bush"

for i in phraseScramble:
    if i != " ":
        phraseSorted.append(i)

phraseSorted.sort()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def letterInventory(s):
    count = []
    letters = alphabet
    for i in range(0, len(letters)):
        count.append(0)

    for i in range(0, len(s)):
        character = s[i]
        print(character)
        if character >= 'a' and character <= 'z':
            print(ord(character) - ord('a'))
            count[ord(character) - ord('a')] += 1
            # count[25] += 1

    for i in range(len(count) - 1, 0, -1):
        if count[i] == 0:
            letters.pop(i)
            count.pop(i)


    for i in range(0, len(count) - 1):
        print(str(letters[i]) + ": " + str(count[i]))

    newString = ""

    for i in letters:
        newString += i

    print(newString)

def removeChar(suffix, char):
    return suffix.replace(char, "")

def isPrefix2(prefix, dictionary, start, end):
    while start <= end:
        mid = (start+end) / 2

        if prefix == dictionary[mid]:
            print(prefix)
            return True
        elif prefix < dictionary[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False

def isPrefix(prefix, dictionary):
    return isPrefix2(prefix, dictionary, 0, len(file) - 1)

def findAnagram(commit, prefix, suffix):
    if not prefix and not suffix:
        big_list.append(commit)

        for char in suffix:
            findAnagram(commit, suffix+char, removeChar(suffix, char))

        return
    elif isPrefix(prefix, file) == False:
        return

word = file[random.randint(0, len(file) - 1)]

# findAnagram([], "bru", "sh")
letterInventory("bro")
