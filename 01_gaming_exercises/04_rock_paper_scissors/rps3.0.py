# Rock_paper_scissors by roy smith IV v3.3

# Module Imports
import random, time

# DATA STRUCTURES -- PLAYERS
playerScore = 0
playerName = "Test Player"
playerChoice = None

#DATA STRUCTURE -- CPU
cpuScore = 0
cpuChoice= None

# PLAYER NAME INPUT 
def playerName(): # Function Signature -- name of function, (arguments if any)
    """Gets the name form the palyer and returnss it."""
    # The line above is a DOCSTRING, it gives a brief examplbe of what the function does.
    playerName = input("Please type your name and press enter.\n")
    print(f"Hello {playerName}!\n")
    isCorrect = input("Is that correct?  Type yes or no and press enter.\n ").lower()
    if isCorrect == "yes":
        print(f"Ok {playerName}, let's play Rock, Paper, Scissors!\n")
    else:
        playerName = input("Please type your name and press enter.\n")
    return playerName

# CALLING THE FUNCTION
playerName = playerName()

# THE RULES using MULTI LINE STRINGS
def rules():
    print (f"""
    Welcome, {playerName} to the game of rock paper scissors!
    its time to play
       
    you will play against a cpu. The first player to score 5 points wins.
    you will select from rock paper or scissors.
    the cpu will select rock papaer scissors at random.
       
    1) ROCK BEATS SCISSORS
    2) SCISSORS BEATS PAPER
    3) PAPER BEATS ROCKS
    """)
    #Does another part of this program need to access this information?
    # IF YES, YOU MUST HAVE A return FUNCTION
    # IF NO, A return STATEMENT IS NOT NEEDED

def playerChoice():
    playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("please enter rock, paper, or scissors and press enter.\n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print("You are not following directions. Please try again.\n")
            exit()
        print(f"You have chosen {playerChoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n")
    return playerChoice

def cpuChoice():
    cpuChoice = random. randint(0,2 ) # randomly slect 0, 1, 2
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice = "paper" 
    elif cpuChoice == 2:
        cpuChoice = "scissors"
    else:
        print("Unable to determine CPU choice,\n Please restart.\n")
        exit()
    return cpuChoice

def pickWinner(playerChoice: str, cpuChoice: str) -> str:
    """Determines the winner using player and CPU choices."""
    if playerChoice == "rock" and cpuChoice == "paper":
        # CPU WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        return "CPU Wins"
    elif playerChoice == "rock" and cpuChoice == "scissors":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
        return "Player Wins"
    elif playerChoice == "rock" and cpuChoice == "rock":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        return "Draw"
    elif playerChoice == "scissors" and cpuChoice == "rock":
        # CPU WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        return "CPU Wins"
    elif playerChoice == "scissors" and cpuChoice == "paper":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
        return "Player Wins"
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "rock":
        # PLAYER WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
        return "Player Wins"
    elif playerChoice == "paper" and cpuChoice == "paper":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "scissors":
        # CPU WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        return "CPU Wins"
    else:
        print("Unable to determine a winner. Please restart.\n")
        exit()

def score(winner: str) -> int:
    """This function uses the winner to update the score for CPU, Num. DRAWS, and player score."""
    if winner == "Player Wins":
        score = 1
    elif winner == "CPU Wins":
        score = 1
    else: # This is a DRAW.
        score = 0
    return score

def matchWinner(playerScore: int, cpuScore: int) -> bool:
    """This function determines if a player has won the game or not by scoring 5 points."""
    if playerScore >=5:
        print("Congratulations! You are the winner.\n")
        return True
    elif cpuScore >= 5:
        print("Sadly, you have been defeated by the CPU.\n")
        return True
    else: # No winner yet
        return False

def playGame(playerScore: int, cpuScore: int) -> None:
    """This function will use all other functions to play Rock, Paper, Scissors. """
    while True:
        cpuPick = cpuChoice()
        playerPick = playerChoice()
        roundWinner = pickWinner(playerPick, cpuPick)
        if roundWinner == "Player Wins":
            playerScore += score(roundWinner)
        if roundWinner == "CPU Wins":
            cpuScore += score(roundWinner)

        print(f"Player Score: {playerScore}\n")
        print(f"CPU Score: {cpuScore}\n")

        if matchWinner(playerScore, cpuScore) == True:
            break

playGame(playerScore, cpuScore)