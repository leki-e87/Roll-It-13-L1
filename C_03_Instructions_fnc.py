# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y" or response == "yea":
            return "yes"
        elif response == "no" or response == "n" or response == "nah":
            return "no"
        else:
            print("Please try again.")

# outputs intstructions
def instructions():
    print('''
    
    **** Instructions ****
    
    Roll the dice.  Keep rolling until you get 
    to 13 (or slightly less).
    If you go over you lose!
    
    If the computer goes over you win :)
    
    etc
        
    ''')


# Main routine

want_instructions = yes_no("Would you like instructions? ")

if want_instructions == "yes":
    instructions()


