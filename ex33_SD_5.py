def counting(end, increment):
    """Prints counting messages about the counting from 0 to 'end' in 
    increments 'increment'."""
    i = 0
    numbers = []
    
    for i in range(0, end, increment):
        print("At the top i is %d" % i)
        numbers.append(i)

        # We have commented out the increment for Study Drill 5
        #i = i + increment # recall this could be i += 1
        #print("Numbers now: ", numbers)
        #print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)

print("We will count to 12 in increments of 2")
counting(12, 2)
