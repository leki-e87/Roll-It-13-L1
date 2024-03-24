# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()
        # should repeat if users don't enter yes or no
        if response == "yes" or response == "y" or response == "yea":
            return "yes"
        elif response == "no" or response == "n" or response == "nah":
            return "no"
        else:
            print("Please try again.")


# outputs instructions
def instructions():
    print('''
    
                  🎲 *~*~*~* Instructions *~*~*~* 🎲
    
                          win the game innit
    
                              🎲 🎲 🎲
    ''')


# checks that users enter an integer
# that is more than 13

def num_check():
    while True:
        error = "Please enter an integer that is close or more than 13."
        try:
            response = int(input("Enter an Integer: "))

            # checks that the number is more than or equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# **** Main routine ****

print("🎲🎲 Roll It 13 🎲🎲")

want_instructions = yes_no("Would you like instructions? ")

if want_instructions == "yes":
    instructions()

print()
target_score = num_check()
