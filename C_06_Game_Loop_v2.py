# At the start of the game, the computer / user score are both zero
comp_score = 0
user_score = 0

game_goal = int(input("Game Goal"))      #Should be a function call!

# Play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    # Start of Round Loop
    # For testing purposes, ask the user what the points for the user / computer were
    comp_points = int(input("Enter the Computer points at the end of the round"))
    user_points = int(input("Enter the User points at the end of the round"))

    # Outside rounds loop - Update score with round points, only ad points to the score of the
    comp_score += comp_points
    user_score += user_points

    #Show overall scores (add this to rounds loop)
    print("*** Game Update ***") #replace with call to statement generator
    print(f"User Score: {user_score} | Comp Score: {comp_score}")

#end of entire game, output final results
print()
if user_score > comp_score:
    print("The User has Won the war of Greatness!")   # Replace this with statement generator call
else:
    print("The Computer has Won the war of Greatness!")