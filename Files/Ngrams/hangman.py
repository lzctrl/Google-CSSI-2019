import random

# Array to hold random words
words = ["monitor", "program", "application", "keyboard", "javascript", "gaming", "network", "programmer", "hello", "world", "random"];

# Random word stored here
randomWord = ""

# All the letters the user has guessed
lettersGuessed = []

# The current word which contains the correct guesses and empty spaces
currentWord = []

# Max mistakes and the user's current mistakes
MAX_MISTAKES_ALLOWED = 6
currentMistakes = 0

# Get the random word at the start of the game
def getRandomWord():
    return words[random.randint(0, len(words) - 1)]

# Add spaces to the user's current word
def populateCurrentWordSpaces():
    for i in randomWord:
        currentWord.append(" ")

# Prints the board with correct letters and spaces
def printBoard():
    board = ""

    for i in currentWord:
        if i == " ":
            board += "_ "
        else:
            board += i + " "

    print(board + "\n")

# Check if the letter has already been guessed, return true if yes, otherwise return false
def checkLetterGuessedAlready(letter):
    for i in lettersGuessed:
        if i == letter:
            return True

    return False

# Check if the letter is in the random word
def checkLetterInWord(letter):

    lettersGuessed.append(letter)

    countIndex = 0

    foundLetter = False

    for i in randomWord:
        if i == letter:
            currentWord[countIndex] = letter
            foundLetter = True
        countIndex += 1

    return foundLetter

# Convert the array containing the letters and spaces into one word
def wordArrayToString(letters):
    word = ""
    for i in letters:
        word += i
    print(word)
    return word

# Welcome user
print("\nWelcome to hangman, let's play!\n")

wonGame = False

# New word and correctly add values to user's current word
randomWord = getRandomWord()
populateCurrentWordSpaces()

# Print the board
printBoard()

# Play the game, while the user's mistakes are less than the max amount
while currentMistakes <= MAX_MISTAKES_ALLOWED or randomWord == wordArrayToString(currentWord):
    # Get guess from user
    guess = raw_input("Let's guess a letter: ")

    # Make sure the guess is not empty or not greater than 1 character
    while guess == " " or guess == "" or len(guess) > 1:
        guess = raw_input("Let's guess a letter: ")

    # Check if the letter has already been guessed
    if checkLetterGuessedAlready(guess) == True:
        print("\nLetter already guessed.\n")
    elif randomWord == wordArrayToString(currentWord):
        wonGame = True
        break
    # Check if the letter is in the word, letter found, update board and other arrays
    elif checkLetterInWord(guess) == True:
        print("\nCorrect guess!\n")

    else:
        print("\nIncorrect guess...\n")
        currentMistakes += 1
        print(str(currentMistakes) + " incorrect guesses.\n")

    printBoard()

if currentMistakes > MAX_MISTAKES_ALLOWED and wonGame == False:
    print("\nYou lost, the full word was: " + randomWord + "\n")
else:
    print("\nYay you won!\n")
