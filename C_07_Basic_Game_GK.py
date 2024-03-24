import random


# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
    else:
        print("You did not choose a valid response")


# outputs instructions
def instructions():
    print('''

                  🎲 *~*~*~* Instructions *~*~*~* 🎲

                          win the game innit

                              🎲 🎲 🎲
    ''')


# Checks that users enter an integer
# that is more than 13
def int_check(question):
    while True:
        error = "Please enter an integer that is 13 or more."

        try:
            response = int(input(question))

            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# generates an integer between 0 and 6
# to simulate a roll of a die
def roll_die():
    roll_result = random.randint(1, 6)
    return roll_result


# rolls two dice and returns total and whether we
# had a double roll
def two_rolls(who):
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have a double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (so far)
    first_points = roll_1 + roll_2

    # Show the user the result
    print(f"{who}: {roll_1} & {roll_2} - Total: {first_points}")

    return first_points, double_score


# main routine goes here

# initialise user score and computer score
user_score = 0
comp_score = 0

num_rounds = 0

# Asks users if they want to read the instructions and displays them

print("🎲🎲 Roll It 13 🎲🎲")

want_instructions = yes_no("Would you like instructions? ")

if want_instructions == "yes":
    instructions()


# asks for target score
target_score = int_check("Enter a target score: ")
print(target_score)

# Loop for game, goes until target score is reached
while user_score < target_score and comp_score < target_score:

    # Add one to the number of rounds (for our heading)
    num_rounds += 1
    print(f"💿💿💿 Round {num_rounds} 💿💿💿")

    # Start of a single round

    # initialise 'pass' variables
    user_pass = "no"
    computer_pass = "no"

    # Start Round...
    print("Press <enter> to begin this round: ")
    input()

    # Get initial dice rolls for user
    user_first = two_rolls("User")
    user_points = user_first[0]
    double_points = user_first[1]

    # Tell the user if they are eligible for double points
    if double_points == "yes":
        print("If you win this round, you gain double points!")

    # Get initial dice rolls for computer
    computer_first = two_rolls("Computer")
    computer_points = computer_first[0]

    # print(f"The computer rolled a total of {computer_points}.")

    # Loop (while both user / computer have <= 13 points)...
    while computer_points <= 13 and user_points <= 13:

        # ask user if they want to roll again, update
        # points / status
        print()

        # If user has 13 points, we can assume they don't want to roll again!
        if user_points == 13:
            user_pass = "yes"

        if user_pass == "no":
            roll_again = yes_no("Do you want to roll the dice (type 'no' to pass): ")
        else:
            roll_again = "no"

        if roll_again == "yes":
            user_move = roll_die()
            user_points += user_move

            # If user goes over 13 points, tell them that they lose and set points to 0
            if user_points > 13:
                print(f"Oh no. You rolled a {user_move} so your total is {user_points}...  "
                      f"You've gone over 13 which means that you lost this round.")

                # reset user points to zero so that when we update their
                # score at the end of round it is correct.
                user_points = 0

                break

            else:
                print(f"You rolled a {user_move} and have a total score of {user_points}.")

        else:
            # If user passes, we don't want to let them roll again!
            user_pass = "yes"

        # if computer has 10 points or more (and is winning), it should pass!
        if computer_points >= 10 and computer_points >= user_points:
            computer_pass = "yes"

        # Don't let the computer roll again if the pass condition
        # has been met in a previous iteration through the loop.
        elif computer_pass == "yes":
            pass

        else:

            # Roll die for computer and update computer points
            computer_move = roll_die()
            computer_points += computer_move

            # check computer has not gone over...
            if computer_points > 13:
                print(f"💥💥💥The computer rolled a {computer_move}, taking their points"
                      f" to {computer_points}.  This is over 13 points so the computer loses!💥💥💥")
                computer_points = 0
                break

            else:
                print(f"The computer rolled a {computer_move}.  The computer"
                      f" now has {computer_points}.")

        print()
        # Tell user if they are winning, losing or if it's a tie.
        if user_points > computer_points:
            result = "You are ahead."
        elif user_points < computer_points:
            result = "The computer is ahead!"
        else:
            result = "It's currently a tie!"

        print(f"{result} \tUser: {user_points} \t | \t Computer: {computer_points}")

        # if both the user and the computer have passed,
        # we need to exit the loop.
        if computer_pass == "yes" and user_pass == "yes":
            break

    # Outside rounds loop - double user points if they won and are eligible

    # Show rounds result
    print()

    if user_points < computer_points:
        print("Damn. You lost this round which means no points "
              "have been added to your total score.  The computer's score has "
              f"increased by {computer_points} points.")

        add_points = computer_points

    # currently does not include double points!
    elif user_points > computer_points:
        # Double user points if they are eligible
        if double_points == "yes":
            user_points *= 2

        print(f"Nice! You won the round and {user_points} points have "
              f"been added to your score.")

        add_points = user_points

    else:
        print(f"The result for this round is a TIE.  You and the computer "
              f"both have {user_points} points.")

        add_points = user_points

    # end of a single round

    # If the computer wins, add its points to its score
    if user_points < computer_points:
        comp_score += add_points

    # if the user wins, add their points to their score
    elif user_points > computer_points:
        user_score += add_points

    # if it's a tie, add the points to BOTH SCORES
    else:
        comp_score += add_points
        user_score += add_points

    print()
    print(f"🎲🎲🎲 User: {user_score} points | Computer: {comp_score} points 🎲🎲🎲 ")
    print()

print()
print(f"Your final score is {user_score}")
