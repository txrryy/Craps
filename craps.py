import random

def rollDice():
    return random.randint(1, 6)

def crapsGame():
    print()
    
    print("Welcome to the Craps game!\n")
    print(" INSTRUCTIONS")
    print("If you roll a 7 or 11 on your first roll, you win.\n\
If you roll a 2, 3, or a 12 on your first roll, you lose.\n\
If you roll any other number of your first roll,\n\
that is your point and you have to roll that point before\n\
you roll a seven, or else, you lose.")
    print()
    input("Press Enter to roll the dice...")

    firstRoll = rollDice() + rollDice()
    print(f"You rolled: {firstRoll}\n")

    if firstRoll in (2, 3, 12):
        print("You lost! You rolled Craps.")
    elif firstRoll in (7, 11):
        print("Congratulations! You won.")
    else:
        print("You established a point. Rolling again...\n")

        while True:
            input("Press Enter to roll the dice...")
            nextRoll = rollDice() + rollDice()
            print(f"Point: {firstRoll}")
            print(f"You rolled: {nextRoll}\n")

            if nextRoll == firstRoll:
                print("Congratulations! You matched your point. You won!")
                break
            elif nextRoll == 7:
                print("You rolled a 7. You lost.")
                break

    playAgain = input("Play again? (yes/no): ").lower()
    if playAgain == "yes":
        crapsGame()
    else:
        print("Thanks for playing! Goodbye!")
        
        
        
##################################################


crapsGame()
