# This example shows operation of dictionaries, `del` and `in`.
# More information about dictionaries can be found at:
# https://docs.python.org/3/tutorial/datastructures.html?highlight=dictionary#dictionaries
# The example is based on country calling codes

# This makes a dictionary with two elements.
call = {'Finland': 358, 'Australia': 61} 
print("Our starting call code dictionary with %d countries in it:" % len(call))
print(call)
call['China'] = 86 # Adds key China to dictionary
print("The call code for China is +%d" % call['China'])

# Dictionaries are unsorted pairs of keys and data.
print("This is what the dictionary is like, they are unsorted:")
print(call)

# We can print all the keys ordered or all the data values sorted. This does 
# not actually sort the dictionary itself though
print(sorted(call.keys()))
print(sorted(call.values()))

# Using `in` to test if Sweden is in our call code dictionary.
print("Is the Sweden's call code in our dictionary?", 'Sweden' in call)

# Deleting Australia from the call code dictionary
del call['Australia']
print("After deleting Australia:")
print(call)

# We can also pop elements (delete them) and return their value
print("The calling code for Finland is +%d" % call.pop('Finland'))
print("Is the calling code for China +86?", call['China'] is 86)
