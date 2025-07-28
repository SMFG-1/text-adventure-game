# Write your adventure here!

def location_1():
    print("You're in a mansion that has intricite objects.")
    print("ACTION MENU:")
    print("- walk east")
    print("- walk west")
    action = input("INPUT ACTION: ")
    if action == "walk east":
        print("You walk east towards the greatest treasure of all.")
        location_2()
    elif action == "walk west":
        print("You fall into a hole.")
        game_over()
    else:
        print(f"Invalid action: {action}")
        location_1()

def location_2():
    print("You see a haunted house.")
    print("ACTION MENU:")
    print("- walk west")
    print("- walk east") # Added walk east option
    action = input("INPUT ACTION: ")
    if action == "walk west":
        print("Be careful!!")
        location_1()
    elif action == "walk east": # Added condition for walk east
        print("You walk east towards a safe house.")
        location_3()
    else:
        print(f"Invalid action: {action}")
        location_2(has_sword)

def location_3():
    print("You enter the safe house!")
    print("ACTION MENU:")
    print("- open door")
    print("- leave")
    action = input("INPUT ACTION: ")
    if action == "open door":
        print("You open the door and find a dragon.")
        location_4()
    elif action == "leave":
        print("You leave the house.")
        location_4() # Assuming leaving also leads to the dragon encounter
    else:
        print(f"Invalid action: {action}")
        location_3()

def location_4():
    print("O NO, A dragon is blocking your way.")
    print("ACTION MENU:")
    print("- attack")
    print("- run")
    print("- frantically dash")
    action = input("INPUT ACTION: ")
    if action == "attack":
            print("You attack the dragon and defeat it.")
            location_6()
    elif action == "run":
        print("You run away from the dragon.")
        location_4()
    elif action == "frantically dash":
        print("Run for your life before the dragon eats ya!")
        game_over()
    else:
        print(f"Invalid action: {action}")
        location_4()


def location_6():
    print("You enter the final room. You won!")

def game_over():
    print("GAME OVER")

# Start the game
location_1()
