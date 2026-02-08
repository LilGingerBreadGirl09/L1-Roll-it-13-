want_instructions =input ("Do you want to see instructions?").lower()

#check the user syays yes / no
if want_instructions =="Yes" or want_instructions == "y":
    print("You said Yes!")
elif want_instructions == ("No") or want_instructions == "n":
    print("You said No!")
else:
    print("Please enter Yes or No >:[")
