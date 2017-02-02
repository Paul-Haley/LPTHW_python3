ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# split() splits a string at each delimiter specified in the string (space in 
# this case) and returns a list of the string split up. 
stuff = ten_things.split(' ')
# Study Drill 1: stuff = split(ten_things, ' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    # Study Drill 1: next_one = pop(more_stuff)
    print("Adding: ", next_one)
    stuff.append(next_one)
    # Study Drill 1: append(stuff, next_one)
    print("There are %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy; Negative indexing starts from the end
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
# Study Drill 1: print(join(' ', stuff))
print('#'.join(stuff[3:5])) # super stellar!; Does not include final element
# Study Drill 1: print(join('#', stuff[3:5]))
