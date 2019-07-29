import random

randomNum = random.randint(1, 10)

guess = raw_input("Guess a number between 1 and 10 ")
guess = int(guess)

while guess != randomNum:
    print("Sorry " + str(guess) + " is not the number...")
    if guess > randomNum:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    guess = raw_input("Guess a number between 1 and 10 ")
    guess = int(guess)

print("\nWooooo you got the answer!")
