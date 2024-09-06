# loops, Roy Smith IV, v0.0

# TWO TYPES OF LOOPS
# for <-- Used when you know how many loops you'll need.
# While <-- Used when you do not know how many loops you'll need.

# for loops is like Go Fish, you search each card for what the player asked.
# while loop is like musical chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN iteration.
# "iterate through the list" means use for loop

# for loops example -- Iterating a List
fruits = ["apple", "banana", "pineapple", "strawberry"]
for eachfruit in fruits: 
    print(eachfruit)

# continue keyword -- Skips the current iteratiohn and then finishes the loop.
fruits = ["apple", "banana", "pineapple", "strawberry"]
for eachfruit in fruits: 
    if eachfruit == "banana":
        continue
    print(eachfruit)

    # break keyword -- immediately exit the loop
fruits = ["apple", "banana", "pineapple", "strawberry"]
for eachfruit in fruits: 
    if eachfruit == "banana":
        break
    print(eachfruit)

# for loops using range().  range(x) is EXCLUSIVE, it starts at 0 and ends at x - 1
    for i in range (10): # range is 0 - 9
        print(i)