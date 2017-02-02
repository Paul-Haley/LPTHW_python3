# Study Drill 1: Try doing it for Australia, there are not too many states and 
# territories.
# Study Drill 2 & 3: The limitations of dictionaries are reasonable well 
# explained in ex37_notes.txt and ex37_dictionary.py from earlier.
# I would still highly recommend looking up the Python documentation.

# create a mapping of U.S.A. states to abbreviations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of U.S.A. states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10) # prints '-' 10 times, `print('--' * 5)` would be the same.
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10) # we have done this more than once, should make a function
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print ever city in state
print('-' * 10) # see above...
# the items() method returns a pair (key, value), these are assigned to abbrev 
# and city respectively.
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('-' * 10) # ...
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])) # where to split lines is 'style' 
    # related issue. I will follow that of LPTHW

print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas') # returns None as 'Texas' is not there.

if not state: # The negation of None is True, None is not False though!
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist') # This is a good place to use None
print("The city for the state 'TX' is: %s" % city)
