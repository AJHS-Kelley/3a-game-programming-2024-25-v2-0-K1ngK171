# Flow Control Structures, Roy Smith IV, v0.0
# Making Computer Programs Make Decisions

temperature = 9.95
color = "Blue"
height = 7
DontLikesPineallpeOnPizza = True

# SINGLE DECISION POINT - if statement
# if CONDITIONAL_EXPRESSION:  <-- This will use a COMPARISON OPERATER 99% of the time. 
    # runThisCode IF the CONDITIONAL_EXPRESSIONAL is True

if temperature > 100:
    print("it is hot as the sun outside.\n")

if height >= 7:
    print("can i got home?\n")

# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS.
if DontLikesPineallpeOnPizza:
    print("Disgusting")

# What if we want something different to happen?
if color == "Red": # COMMON ERROR FOR STUDENTS IS USING = instead of ==. 
    print("Your shirt is the correct uniform shirt.\n")
else:
    print("Your shirt is not the correct uniform shirt.\n")

if height >= 6:
    print("I wear a shoe size of 8.\n")
else:
    print("I dont wear a shoe size of 8.\n")









