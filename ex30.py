people = 30
cars = 40
trucks = 15

# if statements must always be first in a stack of conditional statements.
# An if statement will always be tested when reached.
if cars > people:
    print("We should take the cars.")
elif cars < people:#if the first statemetn is not true, the next statement is
    #considered. elif is short for else if
    print("We should not take the cars.")
else:#else will be done if all the above statements are evaluated to false
    print("We can't decide.")

# Study Drill 4: English explainations of these if statements
if trucks > cars:
    # We print this line if there are more trucks than cars
    print("That's too many trucks.")
elif trucks < cars:
    # This line is printed if there is less trucks than cars.
    # Recall, we reached here because there were NOT more trucks than cars 
    # earlier.
    print("Maybe we could take the trucks.")
else:
    # If both of the above statements above are false, then trucks == cars
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

