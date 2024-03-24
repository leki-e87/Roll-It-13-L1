# checks that users enter an integer
# that is more than 13

def num_check():

    while True:
        error = "Please enter an integer that is close or more than 13."
        try:
            response = int(input("Enter an Integer"))

            # checks that the number is more than or equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# main routine
target_score = num_check()
print(target_score)
