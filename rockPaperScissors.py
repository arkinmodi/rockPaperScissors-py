from random import randint

def score(finalScore):
    userScore = 0
    computerScore = 0
    options = ["ROCK", "PAPER", "SCISSORS"]

    while userScore != finalScore and computerScore != finalScore:
        computerChoice = options[randint(0,2)]
        userChoice = str(input("Rock, Paper, or Scissors? ")).upper()

        if userChoice == computerChoice:
            print("It's a tie!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
            continue
        
        elif userChoice == 'PAPER':
            if computerChoice == options[0]:
                userScore += 1
                print ("You win!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
                continue

            else:
                computerScore += 1
                print ("You lose!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
                continue
            continue        

        elif userChoice == 'SCISSORS':
            if computerChoice == options[1]:
                userScore += 1
                print ("You win!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
                continue

            else:
                computerScore += 1
                print ("You lose!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
                continue
            continue 
        
        elif userChoice == 'ROCK':
            if computerChoice == options[2]:
                userScore += 1
                print ("You win!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
                continue

            else:
                computerScore += 1
                print ("You lose!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
                continue
            continue

def infinte():
    userScore = 0
    computerScore = 0
    options = ["ROCK", "PAPER", "SCISSORS"]

    while True:
        computerChoice = options[randint(0,2)]
        userChoice = str(input("Rock, Paper, or Scissors (type break to stop)? ")).upper()

        if userChoice == 'BREAK':
            print("Final Scores:\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
            break
        
        elif userChoice == computerChoice:
            print("It's a tie!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
            continue
        
        elif userChoice == 'PAPER':
            if computerChoice == options[0]:
                userScore += 1
                print ("You win!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
                continue

            else:
                computerScore += 1
                print ("You lose!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
                continue
            continue        

        elif userChoice == 'SCISSORS':
            if computerChoice == options[1]:
                userScore += 1
                print ("You win!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
                continue

            else:
                computerScore += 1
                print ("You lose!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
                continue
            continue 
        
        elif userChoice == 'ROCK':
            if computerChoice == options[2]:
                userScore += 1
                print ("You win!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
                continue

            else:
                computerScore += 1
                print ("You lose!\n" + "Your Score = " + str(userScore) + "\n" + "Computer Score = " + str(computerScore))
                continue
            continue 

def main():
    gameType = input("Up to what score (type infinte for continuous game)? ").upper()

    if gameType != 'INFINTE':
        score(int(gameType))
    elif gameType == 'INFINTE':
        infinte()

main()