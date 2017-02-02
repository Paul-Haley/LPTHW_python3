for i in range(0,10):
    for j in range(10, -1, -1): # we count backwards to -1 so we include 0
        if(i == j):
            print("i == j, so we break")
            break
        else:
            print("i = %d, j= %d" % (i, j))
    
