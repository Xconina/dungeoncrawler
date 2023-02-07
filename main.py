#A text adventure dungeon crawler
#There are many different choices to be made that affect the game
#Try to get a high score
import random
import time
#inventory dictiinary. values change throught game
inventory = {
	"shovel": False,
	"flashlight" :False,
	"key" : False,
	"treasure": False,
	"knife": 0,
	"health" : 5,
	"gold" : 0,
	"runaway": False,
	"map": False,
    "small": False,
    "keyx": False,
}
monsters = ["slime monster", "undead", "ghoul", "eyebat", "spikeworm", "abomination," "hobgoblin", "vermin soldier", "elemental"]
boss = ["Shadow Dragon", "Gelatinous Cube", "Chimera", "Elder Brain", "Banshee" ]
highscores ={
}
def help():
	print("The available options for most rooms are: search, dig, map, inventory, help")
	print("Some commands won't work without an item in your inventory. You may check your inventory at any time")
	print("You may type north, south, east, or west depending on where the doors are located in that room")
	print("My tech only understands lowercase input")
	print("The program will pause to let you read occasionally. Press Enter to continue")
	print("Type help at any time to read these rules again")
#function to check current inventory
def checkinv():
	for key in sorted(inventory):
		print(key, "=" , inventory[key])
	for i in mementos:
		print(i)
#where items picked up along the way are stored
mementos=[]
#printwhenn not valid
def notvalid(): 
	print("Please enter a valid response.")
def rules():
	print("Remember, my tech only understands lowercase input. ")
drops = ["meat", "ancient scroll", "artifact", "bag of silver", "vial of angelic blood", "gauntlet", "teeth", "tattered leather", "claws", "vial of ectoplasm"]
finds = ["gemstone", "torn stuffed animal", "notebook", "compass", "water bottle", "brooch", "enchanted book", "wizard's robe", "talisman", "wand"]
score = inventory["gold"] + len(mementos) + inventory["health"]

###defining what happens in rooms
#this is the room where the exit is located. can go south or east
def exitroom():
	global mementos
	global inventory
	print("You enter the room and see an exit. Finally!")
    checkm = random.randind(1,3)
    if checkm == 2:
	    fight()
	if inventory["runaway"]==True:
		saferoom()
	else:
        print("You look around and the room is free of monsters")
        print("You see doors on the south and east, and you see an exit to the outside")
		directions = ["south", "east", "exit"]
		options = ["south", "east", "search", "dig", "inventory", "map", "exit"]
		user_input =""
		while user_input not in directions:
            user_input = input("What would you like to do? You may type exit to leave the catacombs and end the game")
			if user_input == "search":
				print("You find food over in the corner. You eat it and feel a little better.")
				if inventory["health"] <=4:
					print("You start feeling much better. Your health goes up 1")	
					inventory["health"] += 1
					strhealth = str(inventory["health"])
					print("Your health is " + strhealth + ".")
				else:
						print("You are already in great health.")
			if user_input == "dig":
				print("")
			if user_input == "map":
				print("")
			if user_input == "inventory":
				checkinv()
			if user_input == "south":
				saferoom()
			if user_input == "east":
				treasureroom()
			if user_input == "exit":
				print("You walk to the exit and open the door. There is fresh air!")
                input()
                print("Congrats! You have made it out.\nAnd you have so much treasure to bring home.\nI hope you had fun on our adventure, "+ name + ".")
				print("Here is your ending inventory: ")
				checkinv()
				input()
				print("Your score for this game is: " + score)
				highscores.update({name : score})
				print("The highscores are: " + highscores)
                again = input("Would you like to play again? yes or no")
                    if again == "no":
                        print("See you later!")
                        quit()
                    if again == "yes":
                        mementos.clear()
                        inventory.update({
                        "shovel": False,
                        "flashlight" :False,
                        "key" : False,
                        "treasure": False,
                        "knife": 0,
                        "health" : 5,
                        "gold" : 0,
                        "runaway": False,
                        "map": False,
                        "small": False,
                        "keyx": False, 
                        })
                        entryway()
                    else:
                        notvalid()
			else:
				notvalid()
                                
                                
#this is where treasure located. go south or west
def treasureroom():
    global inventory
    global mementos
    print("You look around the room. The walls sparkle gold. Could this be where the treasure is?")
    randmon = random.choice(monsters)
    randboss = random.choice(boss)
    print("Before you can investigate, two monsters pop out.")
    input()
    print("First you fight the sidekick, the " + randmon)
    print("You are unable to flee, you must fight")
    if inventory["knife"] >= 1:
        print("Good thing you have a knife. You take it out of your pocket and charge at the " + randmon)
        print("It fights back. You take one damage. Then you surprise it, shoving your knife through it's chest\nThe "+ randmon + " collapses.")
        inventory["health"] -= 1
        input()
    elif inventory ["knife"] < 1 and inventory["shovel"]== True:
        print("You have no knife, but you have a shovel. You take it out and wack the " + randmon + " on his head. He collapses.")
        print("As he stumbles and falls, he uses all his might to punch you in the face. You suffer one damage")
        inventory["health"] -= 1
        loot = random.choice(drops)
        print("He drops a "+ loot + " and you put it in your bag.")
        print("It is time to fight the boss, but you have no knife. You must have at least one to fight him, or you will die.")
        input()
        print("You retreat to the safe room")
        saferoom()
    else:
        print("Without a knife, you are defenseless. You punch the " + randmon + " as hard as you can.\nIt attacks you, and forces you out of the room.")
        print("You must have at least one knife when you return, or you will be unable to fight.")
        inventory["health"] -= 1
        saferoom()
    print("You fought well, but now it's time for the hardest fight. An angry " + randboss + " approaches you")
    if inventory["knife"] >= 2:
        print("He is strong. He has a greatsword, and is so quick that he slashes you before you notice")
        inventory["health"]-= 1
        strhealth = str(inventory["health"])
        print("Your current health is " + strhealth)
        if inventory["health"]<3:
            choiceinput = input("Would you like to flee, yes or no?")
            if choiceinput == "yes":
                print("You run fast, and flee all the way to the safe room")
                saferoom()
        else:
            print("You stumble, but then you take both your knives out and attack!\nYou hit him on the left, then the right")
            print("He takes damage, but he is strong. He hits you again.")
            inventory["health"]-=1
            nowhealth = str.inventory["health"]
            print("Your health is now " + nowhealth)
            if inventory["health"]<= 2:
                choose = input("Would you like to flee to the saferoom, yes or no?")
                if choose == "yes":
                    saferoom()
            else:
                print("You give the fight all you have! You back up, and throw one of your knives at the monster.\n\
                      Instantly, he shrieks and flees. Your knife goes with him.")
                bossloot = random.choice(drops)
                print("On his way out, he dropped a " + bossloot + " which you put in your bag.")
                mementos.ammend((bossloot))
    if inventory["knife"] == 1:
        print("This fight will be hard, but you will try your best. It may have been more helpful to have two knives.")
        print("Before you know it, the " + randboss + " attacks with a giant axe. You dodge, but he cuts your arm")
        inventory["health"]-= 1
        if inventory["health"] <3:
            strhealth = str(inventory["health"])
            print("Your health is "+ strhealth )
            choice = input("Would you like to flee to the closest room, yes or no?")
            if choice == "yes":
                keyroom()
        else:
            print("You fight long and hard. The monster bites your arm, and you slash his head.\nAfter a long fight, you catch him by surprise and shove your knife through his heart")
            bossloot = random.choice(drops)
            print("The " + randboss + " falls to the floor. He drops " + bossloot + " and you put it in your bag" )
            mementos.ammend((bossloot))
    else:
        print("You need at least one knife to fight the boss. I am sending you back towards the entryway to find one.")
        input()
        entryway()
    directions = ["south", "east"]
    user_input = ""
    print("You see a small chest, a big pile of dirt, and walls of speckled gold.\nThere are doors on the west and south walls")
    while user_input not in directions:
        user_input = input("What would you like to do?")
        if user_input == "inventory":
            inventory()
        elif user_input == "help":
            help()
        elif user_input == "south":
            keyroom()
        elif user_input == "west":
            exitroom()
        elif user_input == "search":
            print("You walk over to the small chest.")
            if inventory["small"]== False:
                if inventory["keyx"] == True:
                    print("You open the small chest and find gold! There are gold doubloons and a golden crown.")
                    print("You put them in your bag, but wonder if there is more treasure here.")
                    inventory["gold"] += 25
                    mementos.ammend("golden crown")
                    inventory["small"]= True
                else:
                    print("You do not have the right key to open this treasure")   
            else:
                print("You have already opened this treasure chest.")    
        elif user_input == "dig":
            if inventory["treasure"] == False:
                if inventory["shovel"] == True:
                    print("You walk over to the big pile of sand and dig for what feels like hours.")
                    print("You pull out the biggest chest you have ever seen. It is heavy.")
                    input()
                    yesno = input("Would you like to try to open it?")
                    if yesno == "yes":
                        if inventory["key"]== True:
                            print("You shove the key into the hole. It gets a little stuck, but then it works.")
                            print("When you open it, you are mesmorized. There are stacks of gold bars, and a golden wand")
                            input()
                            print("This was the treasure that people have talked about for hundreds of years")
                            print("It is now yours. You put it in your bag")
                            inventory["gold"] += 100
                            mementos.ammend("golden wand")
                            inventory["treasure"]= True
                        else:
                            print("You put the key in but it doesn't work. You must need a different key")
                    else:
                        print("You leave the treasure for another time.")
                        input()
                else:
                    print("You need a shovel to dig through that big pile of sand")
            else:
                print("You have already found the treasure in this hole.")
        else:
            notvalid()
            
#room where keys are. go north or west
def keyroom():
	print("you walk into key room")
#shovel is located here, only go west
def shovelroom():
	print("you walk into shovelroom")
    print("This room is dark and dusty. The floors are coated in sand and dirt.")
#safe,go north east south
def saferoom():
    global inventory
    global mementos
    numx = random.randint(1,8)
    print("Wooh! This is the only room in the catacombs that is always safe. Not sure why the monsters never come in here.")
    print("In the center of the room you see a big firepit. A nice place to relax. You may relax to gain health then immediately leave the room, or you may do other actions here but not relax.")
    userinput = ""
    directions = ["east", "north", "south", "relax"]
#options = ["east", "north", "south", "relax","dig", "search", "inventory", "map"]
    while userinput not in directions:
        userinput = input("You may input: search, dig, relax, north, south, east. \n")
        if userinput == "relax":
            print("You sit down by thr warm fire. You are suddenly very relaxed.")
            if inventory["health"] == 5:
                print("You manifest gold in front of you")
                inventory["gold"] += numx
                strgold = str(inventory["gold"])
                print("You have " + strgold + " gold.")
                input()
                keyroom()
            elif inventory["health"] < 3:
                print("You start feeling much better. Your health goes up 2")	
                inventory["health"] += 2
                strhealth = str(inventory["health"])
                print("Your health is " + strhealth + ".")
                input()
                keyroom()
            else:
                print("You start feeling a little better. Your health goes up one.")
                inventory["health"] += 1
                strhealth = str(inventory["health"])
                print("Your health is " + strhealth + ".")
                input()
                keyroom()
        elif userinput == "search":
            found = random.choice(finds)
            print("Woah, you found a " + found +". \n You put it in your bag.")
            mementos.append((found))
        elif userinput == "east":
            keyroom()
        elif userinput == "south":
            monsterroom()
        elif userinput == "north":
            exitroom()
        elif userinput == "dig":
            if inventory["shovel"]== True:
                found = random.choice(finds)
                print("You dig and find a" + found + ". You put it in your bag")
                mementos.append((found))
            else:
                print("You cannot dig without a shovel")
        elif userinput == "map":
            print()
        elif userinput == "help":
            help()
        elif userinput == "inventory":
            inventory()
        else:
            notvalid()

#room 4, west of monsterroom,go east or south, has food
def room4():
    global inventory
    global mementos
    checkm = random.randint(1,3)
    print("You enter a room. It looks small and cozy")
    if checkm == "2":
        fight()
    else:
        print("You look around and the room is free of monsters.")
    if inventory["runaway"] == True:
        flashlightroom()
    else:
        print("This room looks like someone lived here for a while.\nThere are sleeping bags and a backpack")
        directions = ["east", "south"]
        user_input = ""
        while user_input not in directions:
            user_input = input("There are doors on the east and south. What would you like to do?")
            if user_input == "search":
                if inventory["health"] < 5:
                    print("You open the backpack and find food. Yum")
                    inventory["health"] += 1
                    strhealth = str(inventory["health"])
                    print("Your health is now at "+ strhealth)
                    input()
                else:
                    randchoice = random.choice(finds)
                    print("You open the backpack and find " + randchoice + ". You put it in your bag.")
                    mementos.ammend((randchoice))
                    input()
            elif user_input == "dig":
                if inventory["shovel"] == True:
                    print("You move the sleeping bag and dig underneath. You find a stash of journals and canned goods.\nYou put it in your bag.")
                    mementos.ammend("stash of journals and food")
                else:
                    print("You can't dig without a shovel. But you move the sleeping bag and find a skeleton. You put a finger bone in your bag.")
                    mementos.ammend("human finger bone")
                    input()
            elif user_input == "inventory":
                inventory()
            elif user_input == "help":
                help()
            elif user_input == "map":
                if inventory["map"] == True:
                    print("The treasure and exit are both northeast from here")
                else:
                    print("You don't currently have a map")
            elif user_input == "south":
                flashlightroom()
            elif user_input == "east":
                monsterroom()
            else:
                notvalid()



	#if inventory["runaway"] == True:
	#	flashlightroom()
	#else:
	#	print()
                

#west bottom room, flaahlight. go north or east


def flashlightroom():
    global inventory
    global mementos
    checkm = random.randint(1,3)
    print("You enter a new room. The walls are blue and painted with stars.")
    if checkm == "2":
        fight()
    else:
        print("You look around and the room is free of monsters.")
    if inventory["runaway"] == True:
        entryway()
    else:
        print("This room looks promising. I see a box in the far corner and a huge pile of sand.")
        directions = ["north", "east"]
	    options = ["north", "east", "search", "dig", "map", "inventory"]
		user_input = ""
		while user_input not in directions:
			user_input = input("You can search, dig, go north, or east.\n")
			if user_input == "search":
				if inventory["flashlight"] ==True:
					found = random.choice(finds)
					print("You walk towards the box and pry it open. Inside you find a dog leash, and also a " +found + ".\nYou put both in your bag.")
					mementos.append("dog leash")
					mementos.append((found))
				else:
					print("You walk towards the box and find a flashlight sitting behind it.")
					inventory["flashlight"] = True
			if user_input == "dig":
				if inventory["shovel"] == True:
					found = random.choice(finds)
					print("You dig until you find something interesting. You pick it up to see that it is a "+ found + ".\nYou put it in your bag.")
					mementos.append((found))
				else:
					print("You try digging with your hands but it doesn't work. You need a shovel.")
			if user_input == "east":
				entryway()
			if user_input == "inventory":
				checkinv()
			if user_input == "map":
				if inventory["map"]== True:
					choice =input("Do Youwant directions to treasure or exit?")
					if choice == "treasure":
						print("Head northeast")
					elif choice == "exit":
						print("Head north")
					else:
						notvalid()
			if user_input == "north":
				room4()
			if user_input not in options:
				notvalid()
			
#east bottom, enemy and knife. west only
def slimeroom():
    global inventory
    global mementos
#global runaway
    print("You are now in the slime room.")
    print("There's a slime monster in here!")
    input()
    fighting = ["fight", "flee"]
    userfight = ""
    while userfight not in fighting:
        userfight = input("fight or flee?  \n")
        if userfight == "fight":
            inventory["runaway"] = False
            if (inventory["knife"] > 0):
                print("You slash the slime monster! It bursts into goops of slime.")
                print("It drops a " + random.choice(drops))
            else:
                print("You punch the slime monster and it flees. But first, it sprays you with toxic slime.")
                inventory["health"] -= 1
                strhealth = str(inventory["health"])
                print("Your health is now " + strhealth + ". Don't drop below 0.")
        elif userfight == "flee":
            print("You turn around and flee to the closest door.")
            inventory["runaway"] = True
        else:
            notvalid()	
    if inventory["runaway"] == True:
        entryway()
    else:
        print("This room is cold and eerie. You see writing on the walls and slime guts splattered.")
        input()
        userinput = ""
        directions = ["west"]
        options = ["west", "search", "dig", "map", "inventory", "read"]
        while userinput not in directions:
            userinput = input("You may go back west, use regular inputs, or type read to read the wall \n")
            if userinput == "read":
                if inventory["flashlight"] == True:
                    print("Some of the words have smeared, but you read what you can.")
                    time.sleep(1)
                    print("Hundreds of years ago there lived a king.\nThis king was known for his violent ...... and all \nthe world feared him. One day he met a woman, a goddess\n ....... and he finally realized how his mean ways were going to destroy ....\nTo this day, he is known as a hero.")
                    input()
                else:
                    print("It's too dark to read.")
            elif userinput == "search":
                if inventory["flashlight"] == True:
                    print("Woah, you found a " + random.choice(finds) +". \n You put it in your bag.")
                    print("You also found another knife!")
                    inventory["knife"] += 1
                else:
                    print("Nice! You found a knife. That should come in handy if we see more monsters.")
                    inventory["knife"] += 1
            elif userinput == "west":
                entryway()
            elif userinput == "dig":
                if inventory["shovel"]==True:
                    found = random.choice(finds)
                    print("You dig and find a " + found +". You put it in your bag.")
                    mementos.append((found))
                else:
                    print("You can't dig in here without a shovel.")
            elif userinput == "inventory":
                checkinv()
            elif userinput == "map":
                if inventory["map"] == True:
                    choice = input("Are you looking for treasure or exit?")
                    if choice == "treasure":
                        print("Head north")
                    if choice == "exit":
                        print("Head northwest")
                    else:
                        notvalid()
                else:
                    print("You don't currently have a map")
            elif userinput == "help":
                help()
            else:
                notvalid()
                rules()

		
#north of entryway,  go any way
def monsterroom():
    global inventory
    global mementos
    checkm = random.randint(1,3)
    print("You come into a very large room.\nThe walls are covered in spider webs and there are skeletons in the corner.")
    input()
    print(checkm)
    if checkm == "two":
        fight()
    else:
        print("You look around and the room is free of monsters.")	
    if inventory["runaway"] == True:
        room4()
    else:
        directions = ["north", "south", "east", "west"]
        #options = ["north", "east", "west", "south", "search", "dig", "map", "inventory"]
        print("You aren't sure what to do next.")
        user_input = ""
        while user_input not in directions:
            user_input = input("You can search, dig, or go any direction.")
            if user_input == "search":
                if inventory["flashlight"] == True:
                    choice = input("Where do you want to search? Skeletons or webs?")
                    if choice == "skeletons":
                        print("You see three skeletons.\nTwo adults and a child.\nThey are sitting next to something.\nYou pick it up.")
                        print("You found a treasure map.\nThey must have been searching for treasure.\nYou put the map in your bag.")
                        inventory[map] = True
                        print("Type 'map' at any time for a directional hint.")
                    elif choice == "webs":
                        found = random.choice(finds)
                        print("You reach into the spiderwebs and see something hiding.\nYou find a " + found + " and put it in your bag")
                        mementos.append((found))
                    else:
                        notvalid()
                else:
                    print("It's too dark in here to be searching.\nYou could run into the spider webs.")
            elif user_input == "dig":
                if inventory["shovel"] == True:
                    print("After a lot of effort you dig up...bones.\nAre these human?\nYou put them in your bag, cautiously.")
                    mementos.append("mysterious bones")
                else:
                    print("You need a shovel.")
            elif user_input == "inventory":
                checkinv()
            elif user_input == "map":
                if inventory["map"] == True:
                    choice = input("Are you looking for treasure or exit?")
                    if choice == "treasure":
                        print("Head north")
                    elif choice == "exit":
                        print("Head north")
                    else:
                        notvalid()
                else:
                    print("You don't currently have a map")
            elif user_input == "north":
                saferoom()
            elif user_input == "east":
                shovelroom()
            elif user_input == "south":
                entryway()
            elif user_input == "west":
                room4()
            else:
                notvalid()


			
#room 1, entryway. n e or west
def entryway():
    global inventory
    global mementos
    directions = ["north","east", "west"]
#options = ["north", "east", "west", "search", "dig", "map", "inventory"]
    userInput = ""
    print("It's so dark and dusty in here.\nAll I can see are doors on the east, north, and west walls.")
    input()
    while userInput not in directions:
        userInput = input("What next? You may search, dig. Or continue east, north, or west.")
        if userInput == "search":
            if inventory["flashlight"] == True:
                print("You found a skeleton in the corner. You looked through the pockets and found five gold.")
                inventory["gold"] += 1
                print(inventory["gold"])
                input()
            else:
                print("It's way too dark in here to search.\nYou'll need to find a flashlight. I think I saw one west of here before.")
                input()
        elif userInput == "dig":
            if inventory["shovel"] == True:
                print("Spiders jump out of the hole! When they're out of the way you find a photo album. It says 'Adamos'. Their family name. You see pictures of a couple and their baby. You put this in your bag.")
                mementos.append("photo album")
                input()
            else:
                print("You need a shovel to dig.")
        elif userInput == "inventory":
            checkinv()
        elif userInput == "map":
            if inventory["map"] == True:
                choice = input("Are you looking for treasure or exit?")
                if choice == "treasure":
                    print("Head north")
                if choice == "exit":
                    print("Head north")
                else:
                    notvalid()
            else:
                print("You don't currently have a map")		
        elif userInput == "east":
            slimeroom()
        elif userInput == "north":
            monsterroom()
        elif userInput == "west":
            flashlightroom()
        elif userInput == "help":
            help()
        else:
            notvalid()

#monstercheck/fight rules

	
def fight():
    global monsters	
    currentmonster= random.choice(monsters)
    print("You take a quick look to see of the room is safe.")
    input()
    print("There's a " + currentmonster + " in here!")
    fighting = ["fight", "flee"]
    userfight = ""
#while userfight not in fighting:
    userfight = input("fight or flee?")
    if userfight == "fight":
        if inventory["knife"] > 0:
            print("You slash the" + currentmonster)
            choice = random.choice(drops)
            print("The " + currentmonster + " drops a " + choice + ".\nYou put it in your bag.")
            mementos.append((choice))
            inventory["runaway"] = False
        else:
            print("You punch him but he is too strong. The " + currentmonster + " hits you back hard. You must flee.")
            inventory["health"] -= 1
            strhealth = str(inventory["health"])
            print(name + ", your health is now " + strhealth + ". Don't drop below 0.")
            inventory["runaway"] = True
    elif userfight == "flee":
        print("You turn around and flee to the closest door.")
        inventory["runaway"]= True
    else:
        notvalid()		

#intro scene
print("Oh, hello there traveller.\nI haven't seen you around here before.")
name = input("What is your name? \n")
print("Nice to meet you, " + name + ". I'm Giz.\nI'm the resident robot guide here, I'll show you around\n.")
time.sleep(3)
print("Did you mean to trap yourself here?\nIf not, it's kinda too late.\nThese are the Chrysus Catacombs.\nLegends say there is a treasure chest buried somewhere here.\n")
print(". ")
check = ""
yesno = ["yes", "no"]
while check not in yesno:
    check = input("Do you want to go find the treasure? yes or no?\n")
    if check == "yes":
        print("Cool! Let's start looking.")
        print("Before we go, lets cover the rules.")
        help()
        print("So obviously the door shut behind you when you came in.")
        input()
        print("We will have to look for another direction to go.\nLet's see what we can find in this room first.")
        input()
        entryway()
    elif check == "no":
        print("Okay, maybe another time.\nI'll be right here if you change your mind.")
        quit()
    else:
        notvalid()
        rules()