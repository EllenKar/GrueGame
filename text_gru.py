apple_taken = False
knife_taken = False

#each scene is created by defining functions for them and then executing from function to function.

def introScene():
    directions = ["red room"]
    print("You are inside a green room.")
    if apple_taken == False:
        print("There is an apple on a small table. It smells of poison.")
        next_act_g = input("You can take the apple if you wish. Press Y to take it and N to leave it untouched.")
        if next_act_g == "Y":
            appleAct()
        else:
            print("You leave the apple on the table.")
    else:
        print("There is a small table in the corner. It's empty.")
    print("You can choose to go forward into the red room. A deep growl is coming from somewhere in the house.")
    userInput = ""
    while userInput not in directions:
        print("Press Y to move into the red room and N to stay.")
        userInput = input()
        if userInput == "Y":
            redRoom()
        else:
            print("You have stayed inside the green room.")

def appleAct():
    print("You have taken the apple!")
    # we define the below variable as global because it exists globally, and we want to change it from this function.
    # this is the only way to do it, by declaring it here as global and then changing it.
    global apple_taken
    apple_taken = True
    introScene()

def knifeAct():
    print("You have taken the knife!")
    global knife_taken
    knife_taken = True
    redRoom()
    
def redRoom():
    directions = ["green room", "black room"]
    print("You are inside a red room.")
    if knife_taken == False:
        print("There is a knife on a small table. It looks wickedly sharp.")
        next_act_r = input("Do you want to take the knife? Press Y to take it or N to leave.")
        if next_act_r == "Y":
            knifeAct()
        else:
            ("You leave the knife on the table.")
    else:
        print("There is a small table in the corner. It's empty.")
    print("You can choose to go back to the green room or forward to the black room. Press Y to go forward, T to go back or N to stay here.")
    userInput = ""
    while userInput not in directions:
        print("What will you do?")
        userInput = input()
        if userInput == "Y":
            blackRoom()
        elif userInput == "T":
            introScene()
        else:
            print("You have stayed here. You hear another threatening growl.")
            

def blackRoom():
    print("You are inside the black room.")
    print("You can see a door ahead that leads to a bright light, and you know that if you go through it, you will wake up back in your bed!")
    print("Suddenly, the grue appears! It's a bearish looking monster with pitch black fur. Its eyes are bright white and its mouth is open and dripping.")
    print("The grue takes a step towards you.")
    if knife_taken and apple_taken is True:
        appleknife_ending()
    elif knife_taken or apple_taken is True:
        if knife_taken is True:
            knifeEnding()
        elif apple_taken is True:
            appleEnding()
    else:
        bad_ending()

def knifeEnding():
    print("Emboldened by a burst of bravery, you run towards the grue and stab it!")
    print("If you thought it might be more resilient than usual, it was not. It quickly keels over and dies.")
    print("Quickly, you move over its body and run through the door. You made it!")
    quit()

def appleEnding():
    print("You decide to offer it the apple in hopes it will be distracted.")
    print("The grue quickly munches the apple, and the poison works just as quickly. The grue falls over and dies.")
    print("Quickly, you move over its body and run through the door. You made it!")
    quit()

def appleknife_ending():
    print("With a knife and an apple in your hands, you have plenty of weapons.")
    print("You offer the apple to the grue. As it munches it distractedly, you stab the monster quickly.")
    print("The grue dies with a surprised expression on its face.")
    print("Quickly, you move over its body and run through the door. You made it!")
    quit()

def bad_ending():
    print("You try to run fast, but the grue is quicker.")
    print("It grabs you and eats you in two bites!")
    print("You have failed!")
    quit()
    

if __name__ == "__main__":
    print("----------------------------")
    print("ESCAPE THE GRUE!")
    print("----------------------------")
    print("After waking from a dream you cannot remember, you find yourself within a small house you've never seen before.")
    print("There is a threatening growl in the distance. You instinctively know this is a monster that will threaten your very life. They call it the infamous....GRUE!")
    print("You must find the way out quickly, and make sure you survive the monster. Good luck!")
    introScene()




