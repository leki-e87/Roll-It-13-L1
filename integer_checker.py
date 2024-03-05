
# checks that users enter an integer
# that is more than 13
while True:

    error = "Please enter an integer that is close or more than 13."

    try:
        my_num = int(input("Enter an Integer"))

        # checks that the number is more than or equal to 13
        if my_num < 13:
            print(error)
        else:
            print("Your number is", my_num)

    except ValueError:
        print(error)
