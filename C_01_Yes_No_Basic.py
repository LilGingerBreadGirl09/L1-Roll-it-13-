
while True:

    want_instructions = input("Do you want to see instructions?").lower()

    #check the user says yes / no
    if want_instructions == " yes" or want_instructions == "y":
        print("You said Yes!")
        break
    elif want_instructions == " no" or want_instructions == "n":
        print("You said No!")
        break
    else:
        print("Please enter Yes or No >:[")
        continue


print ("We are Done!")