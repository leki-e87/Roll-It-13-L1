import random


# checks that users enter an integer
# that is more than 13


# generates a number between 8 and 6
# to simulate the roll of a die
def roll_die():
    outcome = random.randint(a=1, b=6)
    return outcome


# rolls two dice and returns total
# and whether we had a double roll
def two_rolls():
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (atp)
    user_score = roll_1 + roll_2

    # show user the result
    print(f"Die 1: {roll_1} \t Die 2: {roll_2}")

    return user_score, double_score


def int_check(question):
    while True:
        error = "Please enter an integer that is close or more than 13."

        try:
            response = int(input(question))

            # checks that the number is more than or equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine

# begin user and computer scores
user_score = 0
comp_score = 0

num_rounds = 0

target_score = int_check("Enter a target score: ")
print(target_score)

while user_score < target_score and comp_score < target_score:
    # add one to the number of rounds (for our heading)
    num_rounds += 1
    print(f"🎲 Round {num_rounds} 🎲")

    print("Round heading goes here...")
    add_points = int(input("How many points have been won?"))
    user_score += add_points

print()
print(f"Your final score is {user_score}")
