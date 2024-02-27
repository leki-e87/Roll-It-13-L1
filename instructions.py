print("🎲🎲 Roll It 13 🎲🎲")


# loop for testing purposes
while True:
    want_instructions = input(" Would you like to see instructions? ").lower()

    if want_instructions == "yes" or want_instructions == "y":
        print(" You answered yes to this question. ")
    elif want_instructions == "no" or want_instructions == "n":
        print("You chose no.")
    else:
        print("Please try again.")
