import random


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


# main routine starts
print("Press <enter> to begin playing:")
input()

# initialise 'pass' variables
user_pass = "no"
computer_pass = "no"

# get initial dice rolls for user
user_first = two_rolls()
user_points = user_first[0]
double_points = user_first[1]

# tell the player if they can get double points
if double_points == "no":
    double_feedback = ""
else:
    double_feedback = "If you win this round, you get double points!"

# output initial move results
print(f"You rolled a total of {user_points}. {double_feedback}")
print()

# get initial dice rolls for computer
computer_first = two_rolls()
computer_points = computer_first[0]

print(f"The computer rolled a total of {computer_points}")

# loop while the player and computer both have less than 13 points
while computer_points < 13 and user_points < 13:

    # ask the player if they want to roll again, update
    # points and status
    print()
    roll_again = input(" Would you like to roll the dice? (type 'no' to pass): ")

    if roll_again == "yes":
        user_move = roll_die()
        user_points += user_move

        # if player goes over 13 points, tell them they lost the game and set their points to 0
        if user_points > 13:
            print(f"Oh no! You rolled a {user_move}. You now have {user_points} points"
                  f" which means your score is over 13, so you lose this round.")

            # reset user points to zero so that when we update their
            # score at the end of the round, it is correct
            user_points = 0

            break

    else:
        user_pass = "no"

    # roll die for computer and update computer points
    if computer_points <= 10:
        computer_move = roll_die()
        computer_points += computer_move

        if computer_points > 13:
            print("The computer has gone over and you win!")
            computer_points = 0
            break

        else:
            print(f"The computer rolled a {computer_move}. The computer now has"
                  f" {computer_points}.")

    print()
    if user_points > computer_points:
        result = "You are ahead."
    elif user_points < computer_points:
        result = "The computer is in the lead!"

        print(f"***Round Update***:  {result} ")
        print(f"User Score: {user_points} \t | \t Computer Score: {computer_points}")

# outside loop - double user points if they won and are eligible

# show rounds result

if user_points < computer_points:
    print("You lost. No points have been added to your overall score,"
          f"and the computer's score has been increased by {computer_points} points.")

# currently doesn't include double points
else:
    print(f"You won! {user_points} points has been added to your score.")
