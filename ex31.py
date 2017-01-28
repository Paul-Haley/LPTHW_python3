print("You eneter a dark room with two doors. Do you go through door #1 or door #2?")

# NOTE: The same prompt is used in all inputs, we could have a varible like
# prompt = "> " and at each input use input(prompt). The reason to do this is 
# to avoid hard coding the value. When a value is hardcoded everywhere it is 
# used, if the value needs to be changed everywhere later, they will all need 
# to be individual changed. By using a varible, you only change the varible 
# once.
door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probablly better. Bear runs away." % bear)

# This is a continuation of the the first if statement with the door
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespin.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")

# Study Drill 2: This is my own one for door == "3"
elif door == "3":
    print("""You have found the hidden door! 
There are two more doors in front of you. 
The fog of coding forms into the question 
\n\t\t'Have you done Study Drill 2?'\n
1. No, I have not done Study Drill 2
2. Yes, I have done Study Drill 2""")
    good_programmer = input("> ")
    if good_programmer == "1":
        print("Go do the study drills!")
    elif good_programmer == "2":
        print("Very good. Let's play again!")

# Study Drill 2: Put your own options here, remember to update the door list
#elif door == "4"


else:
    print("You stumble around an fall on a knife and die. Good job!")
