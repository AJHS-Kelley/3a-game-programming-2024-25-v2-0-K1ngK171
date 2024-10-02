# Rock_paper_scissors by roy smith IV v0.1

# Module Imports
import random, time


# DATA STRUCTURES -- PLAYERS
playerScore = 0
playerChoice= None
numDraws = 0

#DATA STRUCTURE -- CPU
cpuScore = 0
cpuChoice = None

# MAIN GAME LOOP
loopCount = 0
loopsReq = int(input("How many loops do you want?\nEnter an intger, no commas, and press ENTER.\n"))
# req is the universal abbreviations in computer programming for REQUEST.  reqs = REQUESTS
rpsTimeStart = time.time() # returns the number of seconds since JAN. 01, 1970 @ 12.00AM 
# print ("life")
while loopCount < loopsReq:
        # print ("crash")
        # STARTING FROM THIS LINE, EVERY LINE NEEDS TO MOVE RIGHT BY ONE TAB. 
        # let cpu select at random
    cpuChoice = random. randint(0,2) # randomly slect 0, 1, 2
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
    cpuChoice = random. randint(0, 2) # randomly slect 0, 1, or 2
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice = "scissors" 
    elif cpuChoice == 2:
        cpuChoice = "paper"
    else:
        print("Unable to determine CPU choice,\nPlease restart.\n")
        exit()
        # print (f"CPU Choice: {cpuChoice}"")

        # compare player choice to cpu choice
    if playerChoice ==  "rock" and cpuChoice == "paper":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        cpuScore += 1
        # cpu wins
    elif playerChoice ==  "rock" and cpuChoice == "scissors":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        playerScore += 1
        # player wins
    elif playerChoice ==  "rock" and cpuChoice == "rock":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        numDraws +=1
        # DRAW 
    elif playerChoice ==  "scissors" and cpuChoice == "rock":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        cpuChoice += 1
        # cpu wins
    elif playerChoice ==  "scissors" and cpuChoice == "paper":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        playerScore += 1
        # player wins
    elif playerChoice ==  "scissors" and cpuChoice == "scissors":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        numDraws += 1
        # draw
    elif playerChoice ==  "paper" and cpuChoice == "paper":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        numDraws += 1
        # draw
    elif playerChoice ==  "paper" and cpuChoice == "rock":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        playerScore += 1
        # player wins
    elif playerChoice ==  "paper" and cpuChoice == "scissors":
        print(f"the CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("the cpu wins a point")
        cpuScore += 1
        # draw  
    

print(f"Your Final Score: {playerScore}\nCPU Final score  {cpuScore}\nDraws: {numDraws}\n")
if playerScore > cpuScore:
    print(f"Congratulations, you are the winner.\n ")
elif cpuScore > playerScore:
    print("the cpu wins, try again next time.\n")
else:
    print("unable to determine a winner.\nPlease restart.\n")

rpstimeStop = time.time()
rpsTime = rpstimeStop - rpsTimeStart
print(f"Number of Loops: {loopCount}\n")
print(f"Execution Time {rpsTime:.2F} seconds.\n")