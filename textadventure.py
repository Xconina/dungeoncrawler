import random
import time
#inventory dictiinary. values change throught game
inventory = {
	"shovel": False,
	"flashlight" :False,
	"key" : False,
#	"treasure": False,
	"knife": 1,
	"health" : 5,
	"gold" : 0,
	"runaway": True,
	"map": False,
}
highscores ={
}

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
drops = ["meat", "ancient scroll", "artifact", "bag of silver"]
finds = ["gemstone", "torn stuffed animal", "notebook", "compass", "water bottle"]
score = inventory["gold"] + len(mementos) + inventory["health"]

###defining what happens in rooms
#this is the room where the exit is located. can go south or east
def exitroom():
	global mementos
	global inventory
	print("You enter the room and see an exit. Finally!")
	monstercheck()
	if inventory["runaway"]==True:
		saferoom()
	else:
		directions = ["south", "east", "exit"]
		options = ["south", "east", "search", "dig", "inventory", "map", "exit"]
		user_input =""
		while user_input not in directions:
			if user_input == "search":
				print("You find food over in the corner. You eat it and feel a little better.")
				if inventory["health"] <=4:
					print("You start feeling much better. Your health goes up 2")	
					inventory["health"] += 1
					strhealth = str(inventory["health"])
					print("Your health is " + strhealth + ".")
				else:
						print("You are in great health.")
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
				print("Congrats! You have made it out.\nI hope you had fun on our adventure, "+ name + ".")
				print("Here is your ending inventory: ")
				checkinv()
				time.sleep(3)
				print("Your score for this game is: " + score)
				highscores.update({name : score})
				print("The highscores are: " + highscores)
			else:
				notvalid()
#this is where treasure located. go south or west
def treasureroom():
	print("You walk into treasure room")
#room where keys are. go north or west
def keyroom():
	print("you walk into key room")
#shovel is located here, only go west
def shovelroom():
	print("you walk into shovelroom")
#safe,go north east south
def saferoom():
	global inventory
	global mementos
	numx = random.randint(1,8)
	print("Wooh! This is the only room in the catacombs that is always safe. Not sure why the monsters never come in here.")
	print("In the center of the room you see a big firepit. A nice place to relax. You may relax to gain health then immediately leave the room, or you may do other actions here but not relax.")
	userinput = ""
	directions = ["east", "north", "south", "relax"]
	options = ["east", "north", "south", "relax","dig", "search", "inventory", "map"]
	while userinput not in directions:
		userinput = input("You may input: search, dig, relax, north, south, east. \n")
		if userinput == "relax":
			print("You sit down by thr warm fire. You are suddenly very relaxed.")
			if inventory["health"] == 5:
				print("You manifest gold in front of you")
				inventory["gold"] += numx
				strgold = str(inventory["gold"])
				print("You have " + strgold + " gold.")
				time.sleep(2)
				keyroom()
			elif inventory["health"] < 3:
				print("You start feeling much better. Your health goes up 2")	
				inventory["health"] += 2
				strhealth = str(inventory["health"])
				print("Your health is " + strhealth + ".")
				time.sleep(2)
				keyroom()
			else:
				print("You start feeling a little better. Your health goes up one.")
				inventory["health"] += 1
				strhealth = str(inventory["health"])
				print("Your health is " + strhealth + ".")
				time.sleep(2)
				keyroom()
		if userinput == "search":
			found = random.choice(finds)
			print("Woah, you found a " + found +". \n You put it in your bag.")
			mementos.append((found))
		if userinput == "east":
			keyroom()
		if userinput == "south":
			monsterroom()
		if userinput == "north":
			exitroom()
		if userinput not in options:
			notvalid()

#room 4, west of monsterroom,go east or south, has food
def room4():
	global inventory
	global mementos
	monstercheck()	
	if inventory["runaway"] == True:
		flashlightroom()
	else:
		print()
#west bottom room, flaahlight. go north or east
def flashlightroom():
	global inventory
	global mementos
	monstercheck()	
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
					print("You walk towards the boc and pry it open. Inside you find a dog leash, and also a " +found + ".\nYou put both in your bag.")
					mementos.append("dog leash",(found))
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
	monsters = ["slime monster", "undead", "ghoul"]	
	currentmonster= monsters[0]
	print("There's a " + currentmonster + " in here!")
	fighting = ["fight", "flee"]
	userfight = ""
	while userfight not in fighting:
		userfight = input("fight or flee?  \n")
		if userfight == "fight":
			inventory["runaway"] = False
			print(inventory["knife"])
			if (inventory["knife"] > 0):
				print("You slash the" + currentmonster)
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
		print("This room is cold and eerie. You see writing on the walls and slime guts splatterred.")
		userinput = ""
		directions = ["west"]
		options = ["west", "search", "dig", "map", "inventory", "read"]
		while userinput not in directions:
			userinput = input("You may input: search, dig, read, west. \n")
			if userinput == "read":
				if inventory["flashlight"] == True:
					print("Some of the words have smeared, but you read what you can.")
					time.sleep(1)
					print("Hundreds of years ago there lived a king.\nThis king was known for his violent ...... and all \nthe world feared him. One day he met a woman, a goddess\n ....... and he finally realized how his mean ways were going to destroy ....\nTo this day, he is known as a hero.")
					time.sleep(3)
				else:
					print("It's too dark to read.")
			if userinput == "search":
				if inventory["flashlight"] == True:
					print("Woah, you found a " + random.choice(finds) +". \n You put it in your bag.")
				else:
					print("Nice! You found a knife. That should come in handy if we see more monsters.")
					inventory["knife"] += 1
			if userinput == "west":
					entryway()
			if userinput == "dig":
				if inventory["shovel"]==True:
					found = random.choice(finds)
					print("You dig and find a " + found +". You put it in your bag.")
					mementos.append((found))
				else:
					print("You can't dig in here without a shovel.")
			if userinput == "inventory":
				checkinv()
			if userinput == "map":
				if inventory["map"] == True:
					choice = input("Are you looking for treasure or exit?")
					if choice == "treasure":
						print("Head northwest")
					if choice == "exit":
						print("Head northwest")
					else:
						notvalid()
				else:
					print("You don't currently have a map")
			if userinput not in options:
				notvalid()
				rules()
					
		
#north of entryway,  go any way
def monsterroom():
	global inventory
	global mementos
	print("You come into a very large room.\nThe walls are covered in spider webs and there are skeletons in the corner.")
	time.sleep(2)
	monstercheck()
	if inventory["runaway"] == True:
		room4()
	else:
		directions = ["north", "south", "east", "west"]
		options = ["north", "east", "west", "south", "search", "dig", "map", "inventory"]
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
						print("Type 'map' at any time for a directional hint.")
					elif choice == "webs":
						found = random.choice(finds)
						print("You reach into the spiderwebs and see something hiding.\nYou find a " + found + " and put it in your bag")
						mementos.append((found))
					else:
						notvalid()
				else:
					print("It's too dark in here to be searching.\nYou could run into the spider webs.")
			if user_input == "dig":
				if inventory["shovel"] == True:
					print("After a lot of effort you dig up...bones.\nAre these human?\nYou put them in your bag, cautiosly.")
					mementos.append("mysterious bones")
				else:
					print("You need a shovel.")
			if user_input == "inventory":
				checkinv()
			if user_input == "map":
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
			if user_input == "north":
				saferoom()
			if user_input == "east":
				shovelroom()
			if user_input == "south":
				entryway()
			if user_input == "west":
				room4()
			if user_input not in options:
				notvalid()
			
			
			
#room 1, entryway. n e or west
def entryway():
	global inventory
	global mementos
	directions = ["north","east", "west"]
	options = ["north", "east", "west", "search", "dig", "map", "inventory"]
	userInput = ""
	print("It's so dark and dusty in here.\nAll I can see are doors on the east, north, and west walls.")
	while userInput not in directions:
		userInput = input("What next? You may search, dig. Or continue east, north, or west.")
		if userInput == "search":
			if inventory["flashlight"] == True:
				print("You found a skeleton in the corner. You looked through the pockets and found five gold.")
				inventory["gold"] += 1
				time.sleep(1)
				print(inventory["gold"])
			else:
				print("It's way too dark in here to search.\nYou'll need to find a flashlight. I think I saw one west of here before.")
		if userInput == "dig":
			if inventory["shovel"] == True:
			     print("Spiders jump out of the hole! When they're out of the way you find a photo album. It says 'Adamos'. Their family name. You see pictures of a couple and their baby. You put this in your bag.")
			     mementos.append("photo album")
			else:
			     print("You need a shovel to dig.")
		if userInput == "inventory":
			checkinv()
		if userInput == "map":
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
		
		if userInput == "east":
			slimeroom()
		if userInput == "north":
			monsterroom()
		if userInput == "west":
			flashlightroom()
		if userInput not in options:
			notvalid()

#monstercheck/fight rules
def monstercheck():
	global inventory
	global mementos
	checkm = random.randint(1,3)
	if checkm == 2:
		monsters = ["slime monster", "undead", "ghoul"]	
		currentmonster= random.choice(monsters)
		print("You take a quick look to see of the room is safe.")
		print("There's a " + currentmonster + " in here!")
		fighting = ["fight", "flee"]
		userfight = ""
		while userfight not in fighting:
			userfight = input("fight or flee?")
			if userfight == "fight":
				inventory["runaway"] = False
				if inventory["knife"] > 0:
					print("You slash the" + currentmonster)
					choice = random.choice(drops)
					print("The " + currentmonster + " drops a " + choice + ".\nYou put it in your bag.")
					mementos.append((choice))
					print(mementos)
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
	else:
		print("You look around and the room is free of monsters.")	
		
		

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
	check = input("Do you want to go find the treaaure? yes or no?\n")
	if check == "yes":
		print("Cool! Let's start looking.")
		print("Before we go, lets cover the rules. My tech only understands lowercase, \nso be aware when typing onmy interface.")
		time.sleep(1)
		print("If you ever want to check yiur inventory, just type 'inventory'.\nSame goes for a map if you ever find one.")
		print("So obviously the door shut behind you when you came in.")
		print("We will have to look for another 	direction to go.\nLet's see what we can find in this room first.")
		time.sleep(1)
		entryway()
	elif check == "no":
		print("Okay, maybe another time.\nI'll be right here if you change your mind.")
		quit()
	else:
		notvalid()
		rules()
		
		
		
