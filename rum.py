def entrance():
    print("You have entered the entrance")
    print("What do you want to do?")
    answer = input("1) go to the living room \n2) stay here \n3) Exit")

    if answer == "1":
        print("You approach the door ahead and open it")
        livingroom()
    elif answer == "2":
        print("You have decided to stay")
        entrance()
    elif answer == "3":
        print("You exited the rooms")
        exit()

def livingroom():
    print("You have entered the livingroom")
    print("You see two doors, \nOne infront, \nOne to the left")
    print("Where do you want to go")
    ans = input("1) back to the previous room, \n2) To the Sunshine door, \n3) The door with the cold draft, \n4) Sleep, \n5) Exit")
    if(ans == "1"):
        print("You go back to the previous room")
        entrance()
    elif(ans == "2"):
        print("You went to the room with the sunshine room")
        Sunshine()
    elif(ans =="3"):
        print("You go to the drafty room") 
        Draftyroom()
    elif(ans == "4"):
        print("You took a quick nap")
    elif(ans == "5"):
        print("You exited the rooms")
        exit()

def Sunshine():
    print("You walked through the shining room")
    print("You don't see much more than sunshine")
    print("You can only go back")
    ans = input("1) Go back, \n2) Walk in the shiny room, \n3) Exit")
    if(ans == "1"):
        print("You walk back to the living room")
        livingroom()
    elif(ans == "2"):
        print("You walk around in the sunny room")
    elif(ans == "3"):
        print("You exited the rooms")
        exit()

def Draftyroom():
    print("You walked through the cold drafty door feeling chilled")
    print("It's nothing more than a cold dark room with a draft")
    ans = input("1) Go back to the previous room, \n2) Stay in the room, \n3) Exit")
    if(ans == "1"):
        livingroom()
    elif(ans == 2):
        print("You stay in the cold room")
    elif(ans == "3"):
        print("You exited the rooms")
        exit()

def Exit():
    print("You exited the rooms")

print("Welcome to my Labyrinth")
entrance()