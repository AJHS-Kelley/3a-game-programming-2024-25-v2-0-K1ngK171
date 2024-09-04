# Data Types and Operatives, Roy Smith IV, v0.0

#Fundamental Data Types
#String - str - sequence of letters numbers spaces or toher characters.
# String in python are insode ' ' or " "
# doesnt matter if you use ' ' or " " , just be consistent

# Boolean- Bool - True and False Values.

# Float - float - any number value wit a decimal value, +/-, including 0.0

#Integers - int - any whole number, +/-, including 0.

# Data Tpees are stored in VARIABLES
# A variable is basically a buckeet with a name put data into
# VAIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STARED IN IT!
# VARIABLE CANNOT START WITH A NUMBER
# CamelCaseVaribalNames
# snake_case_variable_names

# DECLARING VARIABLE AND ASSIGNING VALUES

#high_score = 946521 # int data type
#highscore = 231654 # int data type

#carSpeed = 10.35 # float data type, miles per hour
car_Speed = 5.9543215 # float data type, miles per hour

hasAxe = True # boolean data type
isPurple = False # boolean data tpye

#playerName = 'Roy Smith IV' # string data type
Armorcatalog = 'Iron Chest Plate' # string data type

# ASSIGN NEW VALUE
#playerName = 'King'
#carSpeed = 1.74

# DATA TYPES CAN CHANGE, BE CAREFUL
hasAxe = 3.1

# Printing Data Type
newInt = 4
NewFloat = 5.0
NewString = "Skibidi Toilet"
NewBool = False

#print(type(newInt))
#print(type(NewFloat))
#print(type(NewString))
#print(type(NewBool))

#printing Variable to Console / Screen
#print(playerName)
#print(carSpeed)
#print(highscore)
#print(isPurple)

#printing variables and and expressions to console / screen

# PRINTING VARIABLE INTO STRINGS
# print(f"Hello {playerName}. Your high score is {highscore}. Great Job. \n")

# ARITHMETIC OPERATERS
myInt = 7
myFloat = 6.71
myNum= 0

# addtition
myInt = 8 + 2
myFloat = 6.3 + 3.7

myInt = myInt + 10

myNum = myInt + myFloat
# when you add an int and a float together, the answer becomes a float

# subtraction
myNum = myInt - myFloat
myNum = myFloat - 1.5

 # multiplication
myNum = myInt * myFloat

# Division
myNumber = myInt / myFloat # first is numerater, second number is denominator

# MODULUS (MODULO) % -- Returns REMAINDER after dividing
# MOST COMMON USE FOR MODULUS IS DETERMINING EVEN / ODD NUMBERS.

numStudents = 10
numslicesPizza = 40

leftovers = numslicesPizza % numStudents
print(leftovers)

# EXPONENTS **
numsquared = 5 ** 2 # 5 is the base, 2 is the exponent.

# FLOOR-DIVISION // -- Divides, throws out any decimal.
myNum = myInt // myFloat

# ADddition- Assignment Operator - Mostly used for counters
myNum = 5
myNum = myNum + 1 # Old-School Method
myNum += 1 # New Hotness
myNum *= 1
myNum /= 1

# COMPARISON OPERATOR

# IS-EQUAL-TO == Are the two values equal to eachother?
# Returns True or False based on evaluation
x = 6
print(x == 5)

# NOT-EQUAL-TO  != Are the two values NOT equal
# Returns True or False based on evaluation
print(x != 12)

# GREATER THAN / GREATER-THAN-OR-EQUAL TO
print(5 > 3) # Greater Than
print(12 >= 2) # Greater Than or Equal To

# LESS THAN / LESS-THAN-OR-EQUAL TO
print(5 < 3) # LESS Than
print(12 <= 2) # Less Than or Equal To

# LOGICAL OPERATORS
# and -- ALL CONDITION MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
age = 43
height = 56.5
eyeColor = "Brown"
# In order to ride the teacup, you must be atleast 18 years old and at least 60" tall
print (age >= 18 and height >= 60)
print (age >= 18 and height >= 60 and eyeColor == "purple")
#ALWAYS CHECK FOR THE LEAST-LIKELY TO BE TRUE CONDITION FIRST!!!!!
#print(defeatedBoss == True and level > and hasBlueKey == True)

# or -- ATLEAST ONE CONDITION MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
print (age >= 18 or height >= 60)
print (age >= 18 or height >= 60 and eyeColor == "purple")
# ALWAYS CHECK FOR THE MOST-LIKELY TO BE TRUE CONDITION FIRST!!!!!
#print(defeatedBoss == True and level > and hasBlueKey == True)

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT.
a = 5
print(a == 5)
print(not (not (a == 5)))

# COMBINING LOGICAL OPERTATORS
#print(a == 5 and haskey == True or isCloud == True)
#TRUE and

# IDENTITY OPERATORS
g = 1.0
h = 1.0
i = g
print(g is h)
print(i is h)
print(i is not 1.0)
print(i is not g)

# MEMBERSHIP OPERATORS
fruits = ["apple", "banana", "tomato"]
print("banana" in fruits)
print("potato" in fruits)
































































