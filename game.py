import pickle
import sys
import time
import os
#to play the game all you have to do is run the file. 
#This is the loop I use for printing out text and making it look like it is being typed. 
def type_out_text(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.04)
    print()

#This is the intro of the game. The player gets asked the name and if they want to here the instructions. 
playerName = input("What is your name?")
play_intro = input(f"{playerName}, would you like to hear the intro and instructions?(input. 'yes'/'no')\n")
while play_intro.lower() not in ["yes", "no"]:
    play_intro = input("Invalid input. Please enter 'yes' or 'no':\n")
if play_intro == "yes":
    type_out_text(f"Welcome {playerName} to this adventure. You will have to face your fears on today's journey.")
    type_out_text("You are a knight in a castle searching for his king's lost treasure.\nExplore the castle to figure out how to win.")
    instructions = """\nINSTRUCTIONS
To navigate the castle, simply type the direction of one of the available exits.
(Ex. 'north, south, east, west')
To pick an item, input 'get' and the name of the item.
To use an item input 'use' and then the item name.
To save input 'save' to load input 'load'.
To quit input 'quit'.
Just so you know there are some hidden commands you have to discover ;)
To see this message again input 'i'"""
    type_out_text(instructions)
    #This is a useless input so whatever you put doesn't matter. I did this just to make sure the player has enough time to read the instructions before moving on. 
    input("Are you ready to begin this epic quest?\n")
    time.sleep(2)
    type_out_text("Honestly...you don't really have an option...Good luck!\n")
    time.sleep(1)

elif play_intro == "no":
    type_out_text("Good luck!")
#this os.system('clear') is something I figured out how to use in order to clear everything in the terminal. It makes the game look more clear. 
os.system('clear')
#This is the room class where I define all the aspects of the room
#The room has a name a description a series of possible exits and items.
class Room():
    #This method sets up the room and sets all of the NPC variables to their default values. 
    def __init__(self, name, description, exits, items = []):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items
        self.sorcerer_defeated = False
        self.dude_defeated = False
        self.cloaked = False
    
    #the following update methods are used when the player defeats one of the NPC's. if they do the description of the rooms they are in changes. 
    def update(self):
        if self.sorcerer_defeated:
            self.description = "The sorcerer lies defeated on the ground. The room is now quiet."
        else:
            self.description = "There is a powerful Sorcerer ready to kill you. You must defend yourself."
    
    def update1(self):
        if self.dude_defeated:
            self.description = "Full of cobwebs and unused storage space. There is a dead old man on the floor."
        else:
            self.description = "Full of cobwebs and unused storage space. It smells like moldy cheese.\nWait a second...An old man asks for some food."

    def update2(self):
        if self.cloaked:
            self.description = "The cloaked figure lies dead on the floor."
        else:
            self.description = "You are closed off by iron bars. But wait... It looks like somebody broke through.\nThere is a cloaked figure in the corner."
    #the display method displays all of the information of the current room you are in. 
    def display(self):
        print(self.name)
        type_out_text(self.description)
        print("\nExits: ")
        for direction in self.exits:
            print(direction)
        if self.items:
            print("Items: ")
            for item in self.items:
                print(item)
#Game class
class Game():
    #The initializer takes in the things we need to know about the player. 
    def __init__(self):
        self.rooms = []
        self.current_room = None
        self.inventory = []
        self.smart = False
        self.instructions = """\nINSTRUCTIONS
To navigate the castle, simply type the direction of one of the available exits.
(Ex. 'north, south, east, west')
To pick an item, input 'get' and the name of the item.
To use an item input 'use' and then the item name.
To save input 'save' to load input 'load'.
To quit input 'quit'.
To see this message again input 'i'"""
#There are very many methods which do their job, kind of hard to explain them all. 
    def add_room(self, room):
        self.rooms.append(room)
        
    def start(self):
        self.current_room = self.rooms[0]
        self.play()
    #This is the most important method that contains most of the game mechanics. 
    def play(self):
        while True:
            os.system('clear')
            self.current_room.display()
            #Here we get the players input and automaticallly check if it corrisponds with the exits of current room you are in.
            command = input(f"\nWhat would you like to do?\n(Inventory:{self.inventory})\n").lower()
            if command in self.current_room.exits:
                 for room in self.rooms:
                    if room.name == self.current_room.exits[command]:
                        self.current_room = room
                        break
            #this is a command that the player is not told about. It is essential to talk to the librarian in order to win. Unless that is you figure it out on your own. 
            elif command == "talk" and self.current_room.name == "Library":
                if self.smart:
                    type_out_text("I see you have discovered the clues...Now the treasure is yours. I am at peace.")
                    time.sleep(1)

                else:
                    type_out_text("You talk to a librarian who was hiding in the corner.")
                    type_out_text("""'Hello, I am Kurg. I have been a librarian here for many years.I am an expert on potions. 
I was a good friend to the the great King Magnus.\nI was devastated when he was found dead. 
So much so that I investigated his death.\nI found some clues but I was never able to piece them together.
If you do figure out the solution though, you will be rewarded.\nThe clues are found in the Storeroom.
There is a hidden trap door there.To go inside it simply input 'trap door' while in the storeroom.'""")
                    time.sleep(2)
                    
            #another random unmentioned command.
            elif command == "sleep" and self.current_room.name == "Bedroom":
                type_out_text("You take a short nap.")
            #another random unmentioned command.
            elif command == "dance battle" and self.current_room.name == "Dungeon Cell":
                type_out_text("You get schooled in a dance battle by a random guy in the corner. That must suck for you.")
           
            elif command == "quit":
                break
            
            elif command == "i":
                type_out_text(self.instructions)
            #secret command that you can only do in the store room. Pretty hard to guess without talking to the librarian.
            elif command == "trap door" and self.current_room.name == "Storeroom":
                #not sure why I added an achievment
                type_out_text("achievement: Detective")
                time.sleep(1)
                self.current_room = room20
            #yet another secret command
            elif command == "read" and self.current_room.name == "Graveyard":
                type_out_text("The sorcerer is the man who murdered the late king Magnus.\nThe only way to defeat him is to use one of his potions.\nBeware of enemies for they are disguised as friends and the will betray you.\nSometimes leaving somebody alive will cost you your life.\nYou will meet a cloaked figure that you must not trust.\nYou will have to take advantage of him in order to survive.\nAfter you purchase a potion, you must end him.")
                time.sleep(1)
                self.smart = True
            #These save and load the various things in the game. 
            elif command == "save":
                with open("save_game.pickle", "wb") as f:
                    pickle.dump((self.current_room, self.inventory, self.smart, room3.items, room5.items, room10.items, room19.description, room13.description, room15.description), f)
                type_out_text("Game saved.")
                    
            elif command == "load":
                try:
                    with open("save_game.pickle", "rb") as f:
                        self.current_room, self.inventory, self.smart, room3.items, room5.items, room10.items, room19.description, room13.description, room15.description = pickle.load(f)
                    type_out_text("Game loaded.")
                except FileNotFoundError:
                    type_out_text("No save file found.")
            #the way i decided to pick up items is to check if the players input starts with 'get'. If it does i seperate the get and the thing after it. Then if the thing after it exists, I check if I can use it based on what room I am in. In some cases it depends on other variables. 
            elif command.startswith("get "):
                item_name = command[4:]
                
                if item_name in self.current_room.items:
                    self.inventory.append(item_name)
                    self.current_room.items.remove(item_name)
                    type_out_text(f"You have picked up {item_name}.")
                    
                else:
                    type_out_text(f"{item_name} is not in this room.")
            #I did a similar thing i did with picking up items for the use items. I seperate the use and the word after and check if the word after exists. 
            elif command.startswith("use "):
                item_name = command[4:]
                #starting here i have a bunch of different possibilities of items and how you can use them. A lot of them make you die. 
                if item_name == "key" and "key" in self.inventory and self.current_room.name == "Treasure Room":
                    if self.smart:
                        type_out_text("You found the treasure with the help of the Librarian's clues...Congratulations!\nYou return to Kurg the Librarian and he gives you all of his gold. Cool! Now you get double the reasure... You win!")
                        break

                    else:
                        type_out_text("You were able to aquire the treasure with out the help of the Librarian's clues. Great Job!\nJust so you know, this means that you don't get the reward he promised but you still get the treasure!\nYou WIN!!!!")
                        break

                elif item_name == "book" and "book" in self.inventory and self.current_room.name == "Library":
                    type_out_text("You read a page of the book. It talks about an ancient potion of invisibility.")
                    self.inventory.remove("book")
                    
                elif item_name == "food" and "food" in self.inventory and self.current_room.name == "Cellar":
                    type_out_text("You give an old man some food. He thanks you by giving you a gold coin.")
                    self.inventory.append("coin")
                    self.inventory.remove("food")
                    
                elif item_name == "coin" and "coin" in self.inventory and self.current_room.name == "Dungeon Cell":
                    type_out_text("You pay a man and he gives you a potion in return")
                    self.inventory.remove("coin")
                    self.inventory.append("potion")
                #this is a stupid one
                elif item_name == 'deodorant' and self.current_room.name == 'Lavatories':
                    type_out_text("Its still stinky...")
                
                elif item_name == "sword" and "sword" in self.inventory and self.current_room.name == "Cellar":
                    type_out_text("You stab the dude...")
                    self.inventory.remove("sword")
                    room13.dude_defeated = True
                    room13.update1()

                elif item_name == "sword" and "sword" in self.inventory and self.current_room.name == "Dungeon Cell":
                    if "potion" in self.inventory:
                        type_out_text("You stab the cloaked figure. That was sad.")
                        self.inventory.remove("sword")
                        #here is where I update the desciption of the room if the person inside of it was defeated or killed. I set the variable to true then call the update function. This is the same with room19 and room13. 
                        room15.cloaked = True
                        room15.update2()
        
                    else:
                        type_out_text("You stab the cloaked figure. He was your only chance to win.")
                        self.inventory.remove("sword")
                        break
                
                elif item_name == "sword" and "sword" in self.inventory and self.current_room.name == "Sorcerers Room":
                    type_out_text("You attempt to stab the Sorcerer. He easily avoids it.\nHe uses a spell to kill you. You are dead.")
                    break
                
                elif item_name == "potion" and "potion" in self.inventory and self.current_room.name == "Sorcerers Room":
                    if "sword" in self.inventory:
                        type_out_text("The man who gave you the potion alerted the Sorcerer. The Sorcerer was expecting your arrival.\nHe kills you with a powerfull spell.\n")
                        break
                    else:
                        type_out_text("You use the potion. It gives you invisibility.\nThe Sorcerer is looking around for you.\nHe casts as spell that rebounds off a mirror.\nIt hits him right in the face...He is dead.\nYou pick up a key that falls out of his pocket.")
                        self.inventory.remove("potion")
                        room18.sorcerer_defeated = True
                        room18.update()
                        self.inventory.append("key")

                elif item_name == "potion" and "potion" in self.inventory and self.current_room.name == "Dungeon Cell":
                    type_out_text("You use the potion. It startles the cloaked figure.\nOut of fear it turns around and slashes you with a sword.\nBetter luck next time.")
                    break
                
                elif item_name == "book" and "book" in self.inventory and self.current_room.name == "Sorcerers Room":
                    type_out_text("You try to act cool and ask the Sorcerer if he knows anything about the book of potions.\nHe starts on an endless lecture about the history of potions. You die of old age after 67 years of learning about potions...")
                    break

                elif item_name == "book" and "book" in self.inventory and self.current_room.name == "Treasure Room":
                    if "key" in self.inventory:
                        type_out_text("You set aside the treasure chest key and start throwing the book at the treasure lock repeatedly.\nAfter an epic attmept at throwing the book, it rebounds and hits you in the face...\nYou wake up in heaven to your ancestors telling how you could have just used the dang key and been rich.")
                        break
                    else:
                        type_out_text("The book seems like its working. There is a micrioscopic dent in the chest. You feel satisfied and take nap.\nA dog thinks that you are food an eats you in your sleep. Bye!")
                        break
                    
                else:
                    type_out_text("You can't use that here.")
            else:
                type_out_text("Invalid command.")
#here is where i define all of the different rooms. A lot of them are useless.(meaning you can win the game without them.)I made all the rooms at the beginning stages of the game and it would be really tedious to try to remove a lot of them so I'm keeping them here. 
room1 = Room("Entrance", "You are standing in front of a castle entrance.", {"north": "Foyer"})
room2 = Room("Foyer", "You are standing in a grand foyer.", {"north": "Library", "east": "Dining Room", "south": "Entrance", "west": "Oratory"})
room3 = Room("Library", "You are standing in a large library. There is a librarian in the corner.", {"south": "Foyer"}, ["book"])
room4 = Room("Dining Room", "You are standing in a spacious dining room.", {"west": "Foyer", "south": "Kitchen"})
room5 = Room("Kitchen", "You are standing in kitchen.", {"north": "Dining Room", "east": "Garden"}, ["food"])    
room6 = Room("Garden", "You are standing in a beautiful garden with colorful flowers.", {"east": "Fountain", "west": "Kitchen"})
room7 = Room("Fountain", "You are standing in front of a grand fountain.", {"west": "Garden", "north": "Bedroom"})
room8 = Room("Bedroom", "There is an empty bed that is neatly made.", {"north": "Lavatories", "south": "Fountain", "east": "Gaurdroom"})
room9 = Room("Lavatories", "Nothing but an odd smell.", {"south": "Bedroom"})
room10 = Room("Gaurdroom", "A dusty room with a shiny sword.", {"west": "Bedroom", "east": "Dungeon Entrance"}, ["sword"])
room11 = Room("Oratory", "A private chapel.", {"east": "Foyer", "north": "Storeroom", "south": "Cellar"})
room12 = Room("Storeroom", "A room full of empty shelves.", {"south": "Oratory"})
room13 = Room("Cellar", "Full of cobwebs and unused storage space. It smells like moldy cheese.\nWait a second...An old man asks for some food.", {"north": "Oratory"})
room14 = Room("Dungeon Entrance", "Small and steep stairs lead you down the dark dungeon.", {"west": "Gaurdroom", "east": "Dungeon Cell", })
room15 = Room("Dungeon Cell", "You are closed off by iron bars. But wait... It looks like somebody broke through.\nThere is a cloaked figure in the corner.", {"west": "Dungeon Entrance", "east":"Dungeon Hallway"})
room16 = Room("Torture Chamber", "A dead man lays in a corner. There is a basket of heads near a guillotine. They look fresh.\nThere is no turning back now", {"south": "Sorcerers Room"})
room17 = Room("Dungeon Hallway", "It is very tight and oddly quiet. It smells odd.", {"west": "Dungeon Cell", "east": "Torture Chamber"})
room18 = Room("Sorcerers Room", "There is a powerful Sorcerer ready to kill you. You must defend yourself.", {"south": "Treasure Room"})
room19 = Room("Treasure Room", "You have found the treasure room!", {})
room20 = Room("Trap Door", "There is a trap door on the foor you didn't see before", {"north": "Graveyard", "south": "Storeroom"})
room21 = Room("Graveyard", "There is some writing on a tombstone that you want to read.", {"south":"Trap Door"})
#here i simply add all of the rooms to the game so you can access the items inside and go in them. 
game = Game()
game.add_room(room1)
game.add_room(room2)
game.add_room(room3)
game.add_room(room4)
game.add_room(room5)
game.add_room(room6)
game.add_room(room7)
game.add_room(room8)
game.add_room(room9)
game.add_room(room10)
game.add_room(room11)
game.add_room(room12)
game.add_room(room13)
game.add_room(room14)
game.add_room(room15)
game.add_room(room16)
game.add_room(room17)
game.add_room(room18)
game.add_room(room19)
game.add_room(room20)
game.add_room(room21)

game.start()
#the code is short but because of how complex it is it takes a long time. 