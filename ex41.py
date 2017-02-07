# There is a downloaded copy of words.txt in this repository
import random
from urllib.request import urlopen # NOTE: changed from Python 2 from just 
# being urllib.
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = { # PHRASES is a dictionary. x: y is a key, value pair (x,y)
        "class %%%(%%%):":
            "Make a class named %%% that is-a %%%.",
        "class %%%(object):\n\tdef __init__(self, ***)":
            "class %%% has-a __init__ that takes self and *** parameters.",
        "class %%%(object):\n\tdef ***(self, @@@)":
            "class %%% has-a function named *** that takes self and @@@ parameters.",
        "*** = %%%()":
            "Set *** to an instance of class %%%.",
        "***.***(@@@)":
            "From *** get the *** function, and call it with parameters self, @@@.",
        "***.*** = '***'":
            "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else: # This happens if anything but "english" is given.
    PHRASE_FIRST = False

# load up the words from the webstie
for word in urlopen(WORD_URL).readlines(): # connects to the URL reading lines
        # NOTE: readlines in Python 2 would be returning strings, it Python 3 
        # it returns bytes which needs to be decoded using the `.decode()` 
        # method.
        WORDS.append(word.decode().strip()) 

# It is odd styling to have a function in the middle of the main script
def convert(snippet, phrase):
    class_names = [w.capitalize() for w in 
            random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


# keep going until they hit CTRL-D (^D)
try:
    while True:
        #snippets are code, phrases are English
        snippets = list(PHRASES.keys()) # NOTE: In Python 2 a list is returned,
        # in Python 3 it has to be explictly converted to a list to shuffle it.
        random.shuffle(snippets) # shuffles order of elements in snippets

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input("> ")
            print("ANSWER: %s\n\n" % answer)
except EOFError: # EOF is End Of File and can be triggered by ^D (CTRL-D).
    print("\nBye")
