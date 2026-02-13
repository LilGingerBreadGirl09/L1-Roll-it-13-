#functions go here


def yes_no(question):




    while True:

        response = input(question).lower()

        #check the user says yes / no / y / n
        if response == "yes" or response == "y":
           return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please enter Yes or No >:[")


#Main routine


# testing loop...
while True:
    want_instructions = yes_no ("Do you want to see instructions? ")
    print(f"You choose {want_instructions}")



print (f"You chose {want_instructions} We are Done!")