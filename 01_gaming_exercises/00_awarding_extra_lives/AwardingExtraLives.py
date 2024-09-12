# Awarding Extra Lives, Roy Smith IV, v0.0


score = int(input("please input your score here.\n"))
lives = 3
name = "Roy"


# print(f"Hello {name}!  You scored {score} points.\n")


# CHARACTER REFERENCE
# CURLY BRACES {}
# BRAKETS[]
# ANGLE BRAKETS <>
# PARENTHESIS ()

# Allow the user to input the score AS AN INTEGER
# If score is 10000 or less
    # Lose a Life
# Else if score is > 10000 but less than 100001
    # Gives 1 Extra Life
# else score is > 100000 
    # Gain 2 Extra Lives

# Output the score and nuimber if lives on screen


if score <= 10000:
    lives -= 1
elif score < 100001:
    lives += 1
elif score > 100000:
    lives += 2

print(f" you have {lives} lives remaining.\n")
print(f"{name}, You scored {score} points.\n")