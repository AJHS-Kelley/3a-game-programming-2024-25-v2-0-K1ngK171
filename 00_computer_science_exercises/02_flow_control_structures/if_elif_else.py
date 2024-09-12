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

# AMUSEMENT PARK HEIGHT CHECKER EXAMPLE
# Must be > min. height and < max. height for ride.
    
# When writing if-elif-else blocks check for the HIGHEST Value first when usuing > or >=
if height >= 6:
    print("You're too tall enough to ride the tea cups!\n")
elif height >= 3:
    print("You're too tall to ride the tea cups!\n")
else: # "oh no, something's wrong!"
    print("Error, weight not detected. Do not ride\n")


# When writing if-elif-else blocks check for the LOWEST VALUE first when using < or <=
if height <= 3:
    print("You're not tall enough to ride.\n")
elif height < 6:
    print("You're tall enough to ride.\n")
else: # "oh no, something's wrong!"
    print("Error, height not deteted. Do not ride.\n")

# Create an if-elif-else block that checks for temperature.
# If the temperature is atlest 100, print that it's too hot outside.
# If the temperature is atlest 50 degrees but less than 100, print that recess is allowed.
# If the temperature is less than 50 degrees but greater than 0, print that recess is in the gym
# If no temperature is detected, print an error message
    
temperature = 99

if temperature >= 100:
    print("It's too hot, students cannot go to recess.\n")
elif temperature >= 50:
    print("Recess is allowed today.\n")
elif temperature > 0:
    print("Recess will be in the gym.\n")
else:
    print("Error detectiong temperature.\n")

