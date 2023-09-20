import random

print("Welcome to Rock, Paper and Scissor game")

UserPoints = 0
ComputerPoints = 0
TiePoints = 0
moves =["Rock", "Paper", "Scissor"]

def checkForWinner(playerChoice, computerChoice):
    if (playerChoice == "Rock" and computerChoice == "Paper"):
        print("Sorry! You lose")
        return "computer"
    elif (playerChoice == "Rock" and  computerChoice == "Scissor"):
        print("Congrats! You won")
        return "user"
    elif (playerChoice == "Paper" and computerChoice == "Rock"):
        print("Sorry ! You lose")
        return "computer"
    elif (playerChoice == "Paper" and computerChoice == "Scissor"):
        print("Congrats ! You won")
        return "user"
    elif (playerChoice == "Scissor" and computerChoice == "Rock"):
        print("Sorry ! You lose")
        return "computer"
    elif (playerChoice == "Scissor" and computerChoice== "Paper"):
        print("Congrats ! You won")
        return "user"
    else:
        print("It is tie, play again!")
        return "Tie"
num = int(input("How many points the game will end: "))
while (UserPoints != num and ComputerPoints != num):
    while True:
        playerChoice = input("Pick a move Rock, Paper, or Scissor:")
        if(playerChoice == "Rock" or playerChoice == "Paper" or playerChoice == "Scissor"):
            break
        else:
            print("Invalid input? Try again")

    computerChoice = random.choice(moves)

    print("Userchoice :", playerChoice)
    print("Computerchoice :",computerChoice)
    result = checkForWinner(playerChoice , computerChoice)
    if(result == "user"):
        UserPoints += 1
    elif(result == "computer"):
        ComputerPoints += 1
    else:
        TiePoints += 1
    print("Your Score:", UserPoints, "Computer Score:", ComputerPoints, "Tie:", TiePoints,"\n" )
if (UserPoints == num):
    print("User won the match")
elif(ComputerPoints == num):
    print("Computer won the match")
else:
    print("Tie between the User and Computer")
print("GameOver! Thanks for playing")


