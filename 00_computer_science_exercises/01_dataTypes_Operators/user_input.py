# User Input Practice, Roy Smith iv, v0.0

# input() is the built-in to get information from the KEYBOARD
# BASIC EXAMPLE
#variableName = input("please type a variable name and press enter.\n") 
#print(variableName)

# input() saves ALL INPUT TO STRING DATA TYPES DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES DEFAULT!!!
# input() saves ALL INPUT TO STRING DATA TYPES DEFAULT!!!

# INCORRECT, CAUSES A CONCENTRACTION ERROR.
#myNumber = unput("Please tpye an INTEGER number and press enter.\n")
#print(myNumber + 5)

#CORRECT -- USE a wrapper
myNumber = int (input("Please tpye an INTEGER number and press enter.\n"))
print(myNumber + 5)

# Wrapper Functions
# int() will convert the data to an INTERGER if possible.
newNumber = input("Please typer a value and press enter.\n")
print(int(newNumber)) # can convert STRING to INTEGER.
print(float(newNumber)) # can convert STRING to FLOAT.
print(str(newNumber)) # con convert INTEGER to STRING.

# float() will convert the data to a FLOAT if possible.
newNumber = input("Please type a value and press enter.\n")
#print(int(newNumber)) <-- cannot convert FLOAT to INTEGER.
print(float(newNumber)) # can convert STRING to INTEGER.
print(str(newNumber)) # can convert Float to INTEGER

# str() will convert the data to a STRING id possible.