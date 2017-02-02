class Song(object): # everything is some sort of subclass of object; object is 
    # the highest level class.

    # the __init__ method is also known as the constructor
    def __init__(self, lyrics): 
        self.lyrics = lyrics # This is assigning the given lyrics from the call
        # `Song(lyric)` to the instatiation of Song we are making.

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    # Study Drill 3: This is where your hacking would be, adding more methods
    # to the class or instance variables in the __init__ method.

happy_bday = Song(["Happy birthday to you",
    "I don't want to get sued",
    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
    "with pockets full of shells"])

# Study Drill 1: Songs go here

# Study Drill 2: The main reason it is preferred to use varibles is to make 
# function call clearer. Another reason is that it allows Python to only send 
# pointer (small index/location in memory) instead of the whole list of strings
# in the function call.

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
