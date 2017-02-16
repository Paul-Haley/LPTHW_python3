# TODO:
#   * Put items descriptions in a dictionary
#   * The map and lever could be better implemented together
#   * Better ending
#   * Maybe a saving system
import ex45_rooms

import time
import random as rand # This shortens random.suffle() to rand.shuffle()
from sys import argv
from enum import Enum, unique

# Enum[erated] constants. Useful for having constants bound to real words.
class Direction(Enum):
    """Positive is for North or East directions."""
    NORTH = 1
    EAST = 1
    SOUTH = -1
    WEST = -1

def print_help():
    """Prints out game help."""
    print("""Game commands:
    COMMAND                     DESCRIPTION
    help                        Prints this screen
    go <direction>              Takes NORTH, SOUTH, EAST or WEST
    use <item>                  Use an item in the room
    use <item1> on <item2>      Use an inventory item on something else
    pickup <item>               Pickup the item in the room
    see                         Describe what you see
    contents                    Displays the rooms contents
    inventory                   Displays what you have in your inventory

    exit                        Closes the game
    """)

class Engine(object):
    
    def __init__(self, game_map, name):
        """Intialise the game Engine. game_map is a instance of Map and name 
        is the username to use throughout the game."""

        # Get a random starting position
        self.row = rand.randint(0, game_map.ROWS - 1)
        self.col = rand.randint(0, game_map.COLS - 1)
        self.inventory = [] # empty inventory
        self.game = game_map
        self.room = self.game.layout[self.row][self.col]

    def play(self):
        print("\t\tThe Adventures of %s\n" % name)
        print("You awake in a dimly lit room...\n")
        alive = True
        while alive: # main game loop
            self.room = game_map.get_room(self.row, self.col)
            print(self.room.description)
            self.read_input(input("> "))
        
        end_game(alive)
            
    

    def read_input(self, command):
        """Handles reading the commands given by the user. This function 
        will make the required changes to the game state. The returns:
            0 if the command could not be read
            1 if command was read successfully
            2 if user died
            3 if user won the game
            """
        commands = command.split(' ')
        if not len(commands) or commands[0] == 'help': # help or <nothing>
            print_help()
            return 1
        elif commands[0] == 'go' and len(commands) == 2: # go <direction>
            for i in Directions:
                if commands[1] == i.name:
                    heading = self.row + i.value
                    if i is Direction.NORTH or i is Direction.SOUTH:
                        if 0 < heading or heading < game_map.ROWS:
                            self.row = heading
                    else: # Must be traversing East or West
                        if 0 < heading or heading < game_map.COLS:
                            self.col = heading
                    print("You open the %s door and proceed through." % i.name)
                    return 1
            print("Invalid direction")
            return 0 # direction could not be read
        elif len(commands) == 2 and commands[0] == 'use': # use <item>
            if command[1] == 'lever' and 'lever' in self.room.contains:
                self.game_map.lever_used = True
                print("You toggle the lever and hear grinding in the distance")
                return 1
            elif command[1] == 'monster' and 'monster' in self.room.contains:
                monster_attack()
                return 2 # player has died
            elif command[1] == 'exit' and 'exit' in self.room.contains \
                    and self.game_map.lever_used: # use exit
                if self.game_map.lever_used: # if the lever has been used
                    win()
                    return 3 # player has won the game
                else:
                    print("The hatch is closed and there is no clear")#TODO:
        elif len(commands) == 4 and commands[0] == 'use' and \
                commands[2] == 'on': # use <item1> on <item2>
            if commands[1] in self.inventory:
                pass # TODO: do something with the item
        elif len(commands) == 2 and commands[0] == 'pickup': # pickup <item>
            pass # handle pickuping up item and failures. See Room method
        elif command[0] == 'see': # see
            print(self.room.description)
            return 1
        elif command[0] == 'contents':
            self.room.display_contents()
            return 1
        elif command[0] == 'inventory': # inventory
            print(self.inventory) # TODO: Make this print pretty
            return 1
        elif command[0] == 'exit':
            confirm = input("Type Y to exit or anything else to continue: ")
            if confirm == 'Y':
                exit(1)
            return 1
        return 0 # Otherwise the command is not valid

    def win(self):
        """Handles the player winning the game."""
        print("You enter the hatch in the floor.")
        time.sleep(1)
        print("You climb down the ladder and begin walking the tunnel")
        for i in range(3):
            time.sleep(i)
            print("...and walking")
        print("You see a a green blur ahead and run to it.")
        time.sleep(2)
        print("You climb the steps and realise it is an exit sign.")
        time.sleep(2)
        print("You open the door below the sign and step outside.")
        time.sleep(2)
        print("As your eyes adjust to the outside light you hear the door "\
                "slam behind you.\a")
        time.sleep(3)
        print("You find yourself in a forest.")
        time.sleep(2)
        return

    def monster_attack(self):
        """Handles the monster killing the player."""
        print("GROWL")
        time.sleep(1)
        print("The monster scratches you accross the chest\a. You "\
                "crash to the ground in pain!")
        time.sleep(2)
        print("The monster approaches you as you hopelessly crawl.")
        time.sleep(2)
        print("You are flipped onto your back and stare the monster "\
                "in the eye.\a")
        time.sleep(1)
        print("\n\t\tThose green eyes, they are memorising.")
        time.sleep(3)
        print("\n\aYou take your final strike and pass out.")
        time.sleep(5)
        return
    
    def end_game(self, alive):
        """Prints the final end game message based if the player is alive 
        (alive == True) or dead (alive == False)."""
        if alive:
            print("\n\n\t\tYou managed to escape! Well done!")
        else:
            print("\n\n\t\tOh dear, you are dead!")


class Room(object):
    """Class used to represent a in game room"""

    def __init__(self):
        self.description = "There is nothing special about this room"
        self.contains = [] # Items in room (can include monster)
        self.locked = False # True if the door is locked

    def display_contents(self):
        print("This room contains:")
        if len(contains) == 0:
            print("\tNothing...")
        else:
            for item in self.contains:
                print("*\t%s" % item)

    def get_item(self, item):
        return self.contains.pop(item, None) # returns None if item not present

    def unlock(self):
        self.locked = False

class Map(object):
    """Class that contains Rooms and the other complexities of the game. The 
    map is randomly generated but has a fixed size of 3 by 4 rooms."""
    
    def __init__(self):
        self.ROWS = 3
        self.COLS = 4
        self.lever_used = False
        self.layout = [[], [], []]
        for row in range(len(self.layout)): # Go through each map row
            for room in range(self.COLS): # Go through each room in a row
                self.layout[row].append(Room()) # Intialise Room

        # Placing items in game
        things = ['key', 'sword', 'monster', 'exit', 'lever']
        while len(things): # continues untils 0
            row = rand.randint(0, self.ROWS - 1)
            col = rand.randint(0, self.COLS - 1)
            room = self.layout[row][col]

            if len(room.contains) > 0: # room non-empty
                continue # Find another room
            else: # add an item from the things list
                item = things.pop()
                room.contains.append(item)
                if item == 'monster':
                    room.description = "I hear growling"
                elif item == 'lever':
                    room.description = "There is a lever on the wall..."
                    if rand.randint(0, 1):
                        room.contains.append('monster')
                        room.description += "I hear growling"
                elif item == 'exit':
                    room.description = "There is a hatch in the floor."
                elif item == 'key':
                    room.description = "There is a small "\
                            "brass key on the ground."
                elif item == 'sword':
                    room.description = "A long sword "\
                            "shimmers before your eyes. The sword is a "\
                            "beautiful white colour with a golden hilt."

        to_lock = 2
        while to_lock: # Locking two rooms that do not have the key
            row = rand.randint(0, self.ROWS - 1)
            col = rand.randint(0, self.COLS - 1)
            room = self.layout[row][col]
            if 'key' in room.contains:
                continue
            else:
                room.locked = True
                to_lock -= 1

    def get_room(self, row, col):
        return self.layout[row][col]



# Start main script
name = "Frank Browning"
if len(argv) > 1: # replace hero's name if another is given
    name = argv[1]

game_map = Map()
game_engine = Engine(game_map, name)
game_engine.play()
