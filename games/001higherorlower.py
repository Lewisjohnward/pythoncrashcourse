# Simple number guessing game

import sys
import random
import os
import time

# The number to guess
rand = random.randint(1, 100)
# The number of attempts at guessing
i = 0
# Array containing previous guesses
prevguesses = []
# Number of guesses permitted
numberofguesses = 10

# Print previous guesses
def printprevious():
    print("Previous guesses")
    for x in prevguesses:
        # Print each prevguess with newline at end
        print(x)

# Clear terminal screen
def clearscrn():
    os.system('clear')

# Handle if guess is higher than number
def handlehigher():
    prevguesses.insert(0, f'Lower than {guess}')

# Handle if guess is lower than number
def handlelower():
    prevguesses.insert(0, f'Higher than {guess}')

# Handle endgame
def endgame():
    clearscrn()
    exit()

# Handle correct guess
def handlecorrectguess():
    clearscrn()
    print(f'You guessed the correct number: {rand}')
    time.sleep(1)
    endgame()

# While attempts is less than number of guesses permitted
while i < numberofguesses:
    clearscrn()
    # Print previous guesses
    printprevious()
    # Print number of guesses remaining 
    print(f'guesses left: {numberofguesses - i}')
    while True:
        try:
            guess = input("Enter number: ")
            guess = int(guess)
            prevguesses.append(guess)
            break
        except:
            clearscrn()

    # Check guess against number
    if guess == rand:
        handlecorrectguess()
    elif guess > rand:
        handlehigher()
    elif guess < rand:
        handlelower()
    # Increment number of guesses
    i = i + 1
