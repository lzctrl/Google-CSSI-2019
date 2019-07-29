import random

# seed = raw_input("What word'(s) to start: ")
phraseLength = int(raw_input("How many words in a phrase: "))
numberWords = int(raw_input("How many words to generate: "))

def grabText(filename):
    with open(filename) as f:
        content = ' '.join([line.replace('\n', '') for line in f.readlines()])
        return content

moby = grabText("mobydick.txt").split(' ')
gaga = grabText("ladygaga.txt").split(' ')
file = moby + gaga
# print(file)\

if phraseLength == 1:
    seed = file[random.randint(0, len(file) - 1)]
else:
    r = random.randint(0, len(file) - 1)
    if r == len(file) - 1:
        r = 0
    seed = file[r] + " " + file[r + 1]


newText = ""
newText = seed

dict = {}

def randomWord(array):
    return array[random.randint(0, len(array) - 1)]

def randomPhrase(array):
    r = random.randint(0, len(array) - 1)
    if r == len(array) - 1 or r == len(array) - 2 or r == len(array) - 3:
        return array[0] + " " + array[1]
    return array[r] + " " + array[r + 1]

def findWord(seed):
    words = []
    for i in range(0, len(file) - 1):
        if seed == file[i]:
            words.append(file[i + 1])

    if len(words) == 0:
        return

    while True:
        rWord = randomWord(words)
        if rWord != " " or rWord != "  " or rWord != "\n" or rWord != "   " or rWord != "    " or rWord.isSpace() == True:
            newSeed = (seed, rWord)
            dict[newSeed] = words
            return rWord

def findMultipleSeedLengths(seed):
    words = []

    for i in range(0, len(file) - 1):
        if i == len(file) - 1 or i == len(file) - 2 or i == len(file) - 3:
            words.append(file[0] + " " + file[1])
        elif seed == file[i] + " " + file[i+1]:
            words.append(file[i+2] + " " + file[i + 3])

    if len(words) == 0:
        return ""

    while True:
        rWord = randomPhrase(words)
        newSeed = (seed, rWord)
        dict[newSeed] = words
        return rWord

onError = False


for i in range(0, numberWords):
    if phraseLength == 1:
        word = findWord(seed)
        seed = word
        if word is None:
            print("That word could not be found")
            onError = True
            break
        newText = newText + " " + word
    elif phraseLength == 2:
        word = findMultipleSeedLengths(seed)
        seed = word
        if word is None:
            print("That word could not be found")
            onError = True
            break
        newText = newText + " " + word

if onError == False:
    print("\n\ndict: " + str(dict))

    print("\n\nCurrent Seed: " + seed)

    print("\n\nNew text: " + newText)
