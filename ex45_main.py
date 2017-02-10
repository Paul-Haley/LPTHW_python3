# TODO:
#   * Put items descriptions in a dictionary
#   * The map and lever could be better implemented together
import ex45_rooms

import random as rand # This shortens random.suffle() to rand.shuffle()
from sys import argv
from enum import Enum, unique

# Enum[erated] constants. Useful for having constants bound to real words.
@unique
class Direction(Enum):
    UNDEF = -1
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Engine(object):
    
    def __init__(self, game_map, name):
        """Intialise the game Engine. game_map is a instance of Map and name 
        is the username to use throughout the game."""

        # Get a random starting position
        self.row = rand.randint(0, game_map.ROWS - 1)
        self.col = rand.randint(0, game_map.COLS - 1)
        self.inventory = [] # empty inventory

    def play(self):
        print("\t\tThe Adventures of %s\n" % name)
        print("You awake in a dimly lit room...\n")
        alive = True
        while alive: # main game loop
            room = game_map.get_room(self.row, self.col)
            print(room.description)
            if input("do something") == "die":
                alive = False

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
