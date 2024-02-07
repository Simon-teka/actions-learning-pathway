# Text-based MileStone Adventure Game

print("Welcome to the Adventure Game!")
print("You find yourself standing at a crossroad. Which direction do you want to go?")

direction = input("Do you want to go LEFT or RIGHT? ")
                        
if direction.upper() == "LEFT":
    print("You chose to go left. As you walk, you find a small house in the woods.")
    next_step = input("Do you want to KNOCK on the door or WALK around the house? ")
    if next_step.upper() == "KNOCK":
        print("You knock on the door and it creeks open. A friendly old man greets you.")
        final_choice = input("Do you want to ASK for help or LEAVE? ")
        if final_choice.upper() == "ASK":
            print("The old man welcomes you in and offers you food. You've found help and are safe.")
        elif final_choice.upper() == "LEAVE":
            print("You decide to leave and continue on your adventure.")
        else:
            print("Invalid choice.")
    elif next_step.upper() == "WALK":
        print("You walk around the house and find a hidden treasure. Congratulations!")
    else:
        print("Invalid choice.")
elif direction.upper() == "RIGHT":
    print("You chose to go to the right. As you walk, you encounter a bridge.")
    next_step = input("Do you want to CROSS the bridge or FOLLOW the river? ")
    if next_step.upper() == "CROSS":
        print("You cross the bridge and find a pot of gold at the end. Congratulations!")
    elif next_step.upper() == "FOLLOW":
        print("You follow the river and discover a beautiful waterfall. What a sight!")
    else:
        print("Invalid choice.")
else:
    print("Invalid choice.")