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


# **** Main routine ******

print("🎲🎲 Roll It 13 🎲🎲")

want_instructions = yes_no("Would you like instructions? ")

if want_instructions == "yes":
    instructions()
