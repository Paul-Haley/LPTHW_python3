from sys import argv

script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C)")
print ("if you do want that, hit RETURN")

# Technically you could type anything here, as long as you give it a EOF (^D) 
# or press return it will continue.
input("?")

# Opens or creates the file specified
print ("Opening the file...")
target = open(filename, 'w')

# Truncates the file. 
# Study Drill 5: Truncate is not needed as read() with 'w' parameter will 
# automatically truncate the file.
print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

# Prompts users for lines
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Writes each given line followed by a newline (\n)
# Original way of writing the lines to the file:
#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# Study Drill 3: Writing all lines and newlines to the file
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print ("And finally, we clost it.")
target.close()
