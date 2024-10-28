# Functions Practice, Roy Smith iv, V0.0

import random 

def helloWorldMulti(): # FUNCTION SIGNATURE
    """This function will output Hello, World! in a language the user choose""" # DOCSTRING
    # print a list of languages to the screen, at least three but no more than five.
    print("""
        Welcome to the Hello World Translator
        The available language choice are:
        [E]nghlish
        [S]panish
        [J]apanese
        [K]orean
        [T]hai
        """) 

    # allow the user to select (input) a choice for the language
    language = input("What language do you want?\n Please type the first letter of the language you want.\n").lower()

    # print "Hello, World" to the screen in the language
    
helloWorldMulti()
 

