print("I will now count my chickens:")

#prints the Hens count calculated in the print statement before printing
print("Hens", 25 + 30 // 6) # NOTE: In Python 3, `//` does integer division. 
#Python 2 does integer division when only `/` is used.
#Study Drill 5: Using `/` instead of `//` will do float calculations.
print("Rooster", 100 - 25 * 3 % 4)

print("Now I will count the egges:")

# Do an abitary calculation in a print statement to find the egg count
print(3 + 2 + 1 - 5 + 4 % 2 - 1 // 4 + 6) # We put `//` again here.

print("Is it true that 3 + 2 < 5 - 7?")

# When we have `<`, `<=`, `>` or '`>=` it wil do a test to see if the 
# statement is True or False.
print(3 + 2 < 5 - 7) # Testing if 5 < -2 effectively

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

# more testing of inequalities
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)
