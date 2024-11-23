import random

def printstuff():
    x = int(input("Enter your choice! \n 1 - Rock \n 2 - Paper \n 3 - Scissors : "))
    return x
printstuff()

strings = ["Rock","Paper","Scissors"]

def gameLoop():
    choice = printstuff
    computer = random.randint(1,3)
    print("Now it's Computer's Turn...")
    print("The computer chooses "+strings[computer-1])
    if choice == computer:
        print("Its a tie!")
        gameLoop()
    elif choice == 1 and computer == 2:
        print("You lose!")
    elif choice == 1 and computer == 3:
        print("You win!")
    elif choice == 2 and computer == 1:
        print("You win!")
    elif choice == 2 and computer == 3:
        print("You lose!")
    elif choice == 3 and computer == 1:
        print("You lose!")
    else:
        print("You win!")
    if input("Do you want to play again? (Yes/No) ") == "Yes":
        gameLoop()


gameLoop()
