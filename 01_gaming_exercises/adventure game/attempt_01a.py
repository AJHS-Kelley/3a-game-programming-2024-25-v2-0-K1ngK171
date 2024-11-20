# Adventure attempt 1, Roy Smith IV, V0.3
# You have a lot of code to add.   You need to finish by Friday. 
 
import random
import time
import datetime

# SAVING DATA TO A FILE
# STeP 1 -- Create the file name
logFileName = "dragonrealmlog" # add .txt to the file name.  
# Example: dragonrealmlog1132AM.txt

# STEP 2 -- Create / Open the file to save the data

saveData = open(logFileName, "a")
# FILE MODES
# "X" CREATES FILE, IF FILE EXIST, EXIST WITH ERROR MESSSAGE
# "W" CREATES FILE, IF FILE EXIST, ERASE AND OVERWRITE CONTENTS
# "a" CREATES FILE, IF FILE EXIST, APPEND DATA TO THE FILE

#ITEM LIST
hasSpear = False
hasSword = False
hasBow = False
hasGreatSword = False


saveData.write("GAME STARTED" + " " + str(datetime.datetime.now()) + "\n")


def displayIntro():

    print('You are in a land full of wonder. In front of you,')
    print('you see a cave on your left and a city on your right')
    print('which path would you like to start off with?')
    print()

def chooseCave():
    cave = '1'
    city = '2'
    while cave != '1' and city != '2':
        print('what direction will you go? (1 or 2)')
        cave = input()
    return cave


def check(chosenArea):
    print('You headed to the city to grab some gear...')
    time.sleep(1)
    print('The City is lively and vivid...')
    time.sleep(1)
    print('You head to the blacksmith to choose your weapon...')
    time.sleep(1)
    print("The blacksmith asks you which weapon would you like him to craft")
    time.sleep(1)
    
    friendlyCave = random.randint(1, 2)

    if chosenArea == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    check(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()




# ClOSE THE FILE
saveData.write("END OF GAME LOG\n\n")
saveData.close()