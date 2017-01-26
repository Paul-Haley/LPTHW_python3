from sys import argv

script, input_file = argv

def print_all(f):
    """This function reads the whole file (f)"""
    print (f.read())

def rewind(f):
    """Rewinds (moves the reading position) back to the start of the 
    file (f)"""
    f.seek(0)

def print_a_line(line_count, f):
    """Prints the current line of the file specified (f)"""
    print (line_count, f.readline())

current_file = open(input_file)

print ("First let's print the whole file:\n")

print_all(current_file)

print ("Now let's rewind, kind of like a tape.")
# Expanding on this point, a file it just a single continuous array of bytes.
# Calling read starts at index 0, read all puts the 'reader' or 'tape-head' at 
#index len()

rewind(current_file)

print ("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

# The file reader is now at the start of the second line.
current_line = current_line + 1 #current_line=2
print_a_line(current_line, current_file)

# Study Drill 5:
# current_line += x, this would add x to the current value of current_line

# The file reader is now at the start of the third line.
current_line = current_line + 1 #current_line=3
print_a_line(current_line, current_file)
