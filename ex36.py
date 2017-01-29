import time #this is used for the timing functionality
import random

# The functions at the top are called helper functions, they are used 
# throughout the program to avoid repetition and allow for shorter functions.
def direction():
    """Asks user for direction"""
    return input("Which way will you go? ")

def try_door():
    """Call when trying door."""
    time.sleep(1)
    print("You try to open the door.")

def door_locked():
    """Call when the door being attempted is locked."""
    try_door()
    time.sleep(1)
    print("The door is locked.")

def bad_command():
    print("I don't understand.")

def second_room():
    print("This room appears identical to the last room.")
    print("I better not get lost.")
    print("Which door should I take?")
    heading = direction()

    if heading == 'S': # return to start
        try_door()
        print("You fall asleep in the room...")
        time.sleep(5)
        start()
    elif heading == 'W':
        try_door()
        print("You feel a parallel universe engulf you...")
        time.sleep(2)
        print("Something, something, bear room")
        time.sleep(2)
        print("Something else, something else, gold room")
        time.sleep(2)
        print("Somthing greedy, something, something")
        time.sleep(4)
        print("\n\n\n\n")
    elif heading == 'N':
        try_door()
        print("It never hurts to repeat history...")
        second_room()
    elif heading == 'E':
        try_door()
        print("Cake, you win!\n\n")
        print("Yes this game is too short, sorry.")
    else: # bad input given
        print("The light disappears")
        time.sleep(2)
        print("You hear sounds")
        time.sleep(2)
        if random.randint(0, 3) < 3: # 75% chance of dream
            print("The insanity makes you drift off into a distant dream.\n\n")
        else: # otherwise fake a memory error
            print("\n" * 24) # printing 24 newlines
            print("\t\tSYSTEM CORE DUMP!", "\n" * 6) # tabbing and message

            # This print statement is a little complex, see this link:
            # http://www.python-course.eu/python3_formatted_output.php
            #
            # Effectively it converts a 2^64 number to hexadecimal (0 - 9 then 
            # A - E which gives us 16 'numbers').
            print("Memory error at %#8.8X" % random.randint(0, 2**64 - 1))
            time.sleep(10)

            # The game will restart when reaching here due to no more 
            # functions being called.

def start():
    """Starting place of adventure"""
    print("You awake in a room with doors labelled,")
    print("N[orth], S[outh], E[ast] and W[est]")
    
    # loop until N is given
    stuck = True
    while stuck:
        heading = direction()
        if heading == 'S' or heading == 'E' or heading == 'W':
            door_locked()
        elif heading == 'N':
            stuck = False
            try_door()
            second_room()
        else:
            bad_command()


#main loop of program. 
while input("Play game? ") == "yes":
    start()
print("Hope you enjoyed my game.")
