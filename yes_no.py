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


# Main routine
while True:
    want_instructions = yes_no("Would you like instructions? ")
    print(f"Player chose {want_instructions}.")


