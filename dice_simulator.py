import random


# generates a number between 8 and 6
# to simulate the roll of a die
def roll_die():
    result = random.randint(a=1, b=6)
    return result


# MR goes here (main routine)

for item in range(0, 10):
    user_score = 0
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (atp)
    user_points = roll_1 + roll_2

    # show user the result
    print(f"Die 1: {roll_1} \t Die 2: {roll_2} \t Points: {user_points}")
    print(f"Double Score opportunity: {double_score}")

