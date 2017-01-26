from sys import argv

script, filename = argv

print ("We're going to erase %r." % filename)
print ("If you don't want that, hit CTRL-C (^C)")
print ("if you do want that, hit RETURN")

# Technically you could type anything here, as long as you give it a EOF (^D) 
# or press return it will continue.
input("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("TRuncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("And finally, we clost it.")
target.close()
