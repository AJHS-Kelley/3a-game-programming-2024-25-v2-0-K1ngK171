# Rock_paper_scissors by roy smith IV v0.1

# Module Imports
import random, time


# DATA STRUCTURES -- PLAYERS
playerScore = 0
playerChoice= None
numBraws = 0

#DATA STRUCTURE -- CPU
cpuScore = 0
cpuChoice = None

# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:

# STARTING FROM THIS LINE, EVERY LINE NEEDS TO MOVE RIGHT BY ONE TAB. 
    # let cpu select at random
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
    # print(f"CPU Choice: {cpuChoice}")

    #   let PLAYER select choice at random
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
    
# compare player choice to cpu choice
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
    elif playerChoice ==  "paper" and cpuChoice == "paper":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        playerChoice += 1
        # cpu wins
    elif playerChoice ==  "paper" and cpuChoice == "rock":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        playerChoice += 1
        # player wins
    elif playerChoice ==  "paper" and cpuChoice == "scissors":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        playerChoice += 1
        # draw