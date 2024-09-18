# Rock_paper_scissors by roy smith IV v0.1

# Module Imports
import random

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
    print(Ok {palyerNmae})




# THE RULES using MULTI LINE STRINGS
print (f"""
welcome, {playerName} to the game of rock paper scissors!
its time to play
       
you will play against a cpu. the first player to score 5 points wins.
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
while playerscore < 5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\n The CPU has {cpuScore} points.\n")
    playerChoice = input 
    # print the current score for cpu and player.
    # let player rock, paper, scissor.
    # compare player choice to cpu choice
    # print the results to the screen
    # award point to winner and output results.