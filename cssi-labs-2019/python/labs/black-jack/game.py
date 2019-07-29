import random

def getRandomCard():
    return random.randint(2, 11)

def getUserInput():
    return raw_input("Would you like to draw? (y/n) ")

currentScore = 0
highestNum = 21
possibleLastCard = 0

gamesWon = 0
gamesLost = 0
totalScore = 0
highestScore = 0

print(" ")
roundsToPlay = raw_input("How many rounds to play? ")
roundsToPlay = int(roundsToPlay)

highestScore = 21 * roundsToPlay

for i in range(0, roundsToPlay):
    while currentScore <= highestNum:
        currentScore += getRandomCard()
        print(" ")
        print("Card picked: " + str(currentScore))
        print(" ")

        if currentScore == highestNum:
            break
        elif currentScore > highestNum:
            break

        userChoice = getUserInput()

        if userChoice == "n":
            possibleLastCard = getRandomCard()
            break

    totalScore += currentScore

    if currentScore == highestNum:
        print("You Win!")
        gamesWon += 1
    elif currentScore < highestNum:
        print(" ")
        print("You were so close! Your final score is " + str(currentScore) + ". The next card would have been a " + str(possibleLastCard))
    else:
        print("You lost...")
        gamesLost += 1

    currentScore = 0

print(" ")
print("You won a total of " + str(gamesWon) + " games.")
print("You lost a total of " + str(gamesLost) + " games.")
print(" ")
print("Your total score was " + str(totalScore))
print("Your total best score could have been " + str(highestScore))
print(" ")
