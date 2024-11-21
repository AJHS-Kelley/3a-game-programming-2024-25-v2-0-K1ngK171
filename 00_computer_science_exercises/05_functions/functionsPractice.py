# Functions Practice, Roy Smith iv, V0.3

import random 

def helloWorldMulti(): # FUNCTION SIGNATURE
    """This function will output Hello, World! in a language the user choose""" # DOCSTRING
    # print a list of languages to the screen, at least three but no more than five.
    print("""
        Welcome to the Hello World Translator
        The available language choice are:
        [E]nglish
        [S]panish
        [J]apanese
        [K]orean
        [F]ilipino
        """) 

    # allow the user to select (input) a choice for the language
    language = input("What language do you want?\n Please type the first letter of the language you want.\n").upper()

    # print "Hello, World" to the screen in the language
    
    if language == "E":
        print("In English:\nHello world.\n")
    elif language == "S":
        print("In Spanish:\nHola mundo!\n")
    elif language == "J":
        print("In Japanese:\nKonichiwa sekai!\n")
    elif language == "K":
        print("In Korean:\njeon squash yoravoon annyeonghaseyo!\n")
    else:
        print("In Filipino:\nhello world!\n ")

helloWorldMulti() # Function Call

# Function to determine Even / Odd Numbers
argument1 = random.randint(-1000, 1000)

def isEven(argument1 : int) -> bool: # Requires one (Arguemnt1) and RETURNS a boolean value.
    """Determine if an integer value is even or odd"""
    if argument1 % 2 == 0:
        return True
    else:
        return False
    
print(isEven(argument1))

# Function with Multiple Arguments
def canRideRollerCoaster(age: int, height: int) -> bool:
    if age >10 and height > 4:
        print("You can ride.\n")
        return True
    else:
        print("You cannot ride.\n")
        return False
    
canRideRollerCoaster (4,10) # Argument must be passed in the same order as the function signature indicates.