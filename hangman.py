import random

def printWord():
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")

def checkWord():
    ok = True
    for char in word:
        if char in guesses:
            continue
        else:
            ok = False
    return ok

words = ["banana", "apple", "water", "beer"]
word = random.choice(words) 
tries = int(input("How many chances do you want? "))
print("Guess the word!")
guesses = ""
while tries > 0:
    printWord()
    guess = input("Guess a character: ")
    if guess in word:
        guesses+=guess
    else:
        tries-=1
        print(guess+" is not in the word!")
    if checkWord() == True:
        print("The word was "+word)
        print("You win!")
        tries = 0
if tries == 0 and checkWord() == False:
    print("The word was "+word)
    print("You lose!")