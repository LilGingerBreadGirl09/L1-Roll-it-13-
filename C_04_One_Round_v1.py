# import random

# Intialise rounds points
user_points = 0
comp_points = 0
double_user = "no"

# Roll the dice for the user and not if they got a double
user_one = random.randint( 1, 6 )
user_two = random.randint( 1, 6 )

if user_one == user_two:
   double_user = "yes"


# Roll the dice for the computer
comp_one = random.randint( 1, 6 )
comp_two = random.randint( 1, 6 )


#Update the use / Computer points
user_points += user_one + user_two
comp_points += comp_one + comp_two

# Output results
print("\nInitial Points")
print(f"User - Roll 1 : {user_one} \t| Roll 2: {user_two} \t| Total: {user_points} ")
print(f"Computer - Roll 1 : {comp_one} \t| Roll 2: {comp_two} \t| Total: {user_points} ")

# Let the user know if they qualify for double points
if double_user == "yes":
    print("Beautiful, wonderful news! - if you win I shall grant you double your points! ^^")