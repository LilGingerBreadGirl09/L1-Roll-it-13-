#functions go here
def yes_no(question):
    """ Checks if user enters yes / no """
    while True:

        response = input(question).lower()

        #check the user says yes / no / y / n
        if response == "yes" or response == "y":
           return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter Yes or No >:[")

def instructions():
    """ prints instructions """

    print("""
*** Instructions ***

Roll the Dice and try again!
""")

def int_check():
    """Checks users enter an integer more than / equal to 13"""

    error = "Please enter an integer more than / equal to 13. >:["

    while True:
        try:
            response = int(input("What is the game goal?"))

            if response < 13:
                print(error)

            else:
               return response

        except ValueError:
            print(error)


#Main routine

# ask the user if they want instructions (check is they say yes / no)
want_instructions = yes_no ("Do you want to see instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

print()
game_goal = int_check()
print(game_goal)
