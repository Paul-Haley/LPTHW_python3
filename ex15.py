from sys import argv

# Read arguments given
script, filename = argv

# opens the file requested (first user given argument)
txt = open(filename)

# Prints the file contents after short message
print ("Here's your file %r:" % filename)
print (txt.read())

# Part of Study Drill 7 to close the file
txt.close()

# Takes the user's next file from stdin
print ("Type the filename again:")
file_again = input("> ")

# Reads requested file
txt_again = open(file_again)

# Displays the requested file
print (txt_again.read())

# Part of Study Drill 7 to close the file
txt_again.close()
