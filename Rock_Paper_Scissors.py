import random

# Variable Declarations, options for compluter list and then strings for answers
options = ["Rock", "Paper", "Scissors"]
paperAnswer = "Paper Covers Rock"
rockAnswer = "Rock Crushes Scissors"
scissorAnswer = "Scissors Cuts Paper"
drawAnswer = "Guess this one is a draw"

print("Thank you for using Ian's Rock Paper Scissors")

while True:
    #computer selects option and then player inputs
    compAnswer = random.choice(options)
    playAnswer = input("I have selected my option, now please select yours: ")
    print("I selected " + compAnswer)

    # Depending on what player selected determines hte answer
    if playAnswer == compAnswer:
        print(drawAnswer)
    elif playAnswer == "Rock" or playAnswer == "rock":
        if compAnswer == "Paper":
            print("I win " + paperAnswer)
        else:
            print("You win " + rockAnswer)
    elif playAnswer == "Paper" or playAnswer == "paper":
        if compAnswer == "Scissors":
            print("I win " + scissorAnswer)
        else:
            print("You win " + paperAnswer)
    elif playAnswer == "Scissors" or playAnswer == "scissors":
        if compAnswer == "Rock":
            print("I win " + rockAnswer)
        else:
            print("You win " + scissorAnswer)
    else:
        print("Hey!  That's not an answer!")

    #Game asks player to continue loop
    again = input("Would you like to try again? (y/n): ")
    if again == "n":
        break
    else:
        print(" ")
