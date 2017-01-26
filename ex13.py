#I ran this program by typing at the command line:
#python3 ex13.py help me please

from sys import argv

#argv are the 'argument variables', what is given at script invocation.
script, first, second, third = argv

print ("The script is called: ", script)
print ("Your first variable is: ", first)
print ("Your second variable is: ", second)
print ("Your third variable is: ", third)
