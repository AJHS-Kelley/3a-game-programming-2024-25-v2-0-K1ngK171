# Rock_paper_scissors by roy smith IV v3.0

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
playerNmae = input("Please type your name and press enter.\n")
print(f"Hello {playerName}!\n")
isCorrect = input("Is that correct?  Type yes or no and press enter.\n ").lower()

# .lower() can turn ALL input into lowercase.
# .upper() can turn ALL input into uppercase.

if isCorrect == "yes":
    print(f"Ok {playerName}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Please type your name and press enter.\n")

# THE RULES using MULTI LINE STRINGS
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

# MULTI-LINE STRING CAN BE USED AS BIG COMMENTS
"""
anything in between the set of double- is just ignored.
If you need to write large comments, it's easier to use multi-line strings
putting an # in fron of 15 different lines.
"""

# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\n The CPU has {cpuScore} points.\n")
    playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
    if playerChoice != "rock" or playerChoice != "Paper" or playerChoice != "Scissors":
        playerChoice = input("please enter rock, paper, or scissors and press enter.\n").lower()
        if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
            print("You are not following directions. Please try again.\n")
            exit()
        print(f"You have chosen {playerChoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n")
# STARTING FROM THIS LINE, EVERY LINE NEEDS TO MOVE RIGHT BY ONE TAB. 
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
    print(f"CPU Choice: {cpuChoice}")

# compare player choice to cpou choice
    if playerChoice ==  "rock" and cpuChoice == "paper":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        cpuChoice += 1
        # cpu wins
    elif playerChoice ==  "rock" and cpuChoice == "scissors":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        cpuChoice += 1
        # player wins
    elif playerChoice ==  "rock" and cpuChoice == "rock":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        # DRAW
    elif playerChoice ==  "scissors" and cpuChoice == "rock":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        cpuChoice += 1
        # cpu wins
    elif playerChoice ==  "scissors" and cpuChoice == "paper":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        playerChoice += 1
        # player wins
    elif playerChoice ==  "scissors" and cpuChoice == "scissors":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        cpuChoice += 1
        # draw
    elif playerChoice ==  "paper" and cpuChoice == "rock":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        playerChoice += 1
        # draw
    elif playerChoice ==  "paper" and cpuChoice == "scissors":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        playerChoice += 1
        # cpu wins
    elif playerChoice ==  "paper" and cpuChoice == "paper":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        playerChoice += 1
        # draw

