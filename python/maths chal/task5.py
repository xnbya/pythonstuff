maxfactor = int(input("Enter the largest factor"))
mby = 1

found = False
while not found:
    #print(mby)    
    works = True
    nototest = mby * maxfactor
   # if(nototest % 1000 == 0):        
    #    print(nototest)
    x = maxfactor
    while(x > 0):
        if(nototest % x != 0):
            works = False
        x = x - 1
    if(works):
        print("Answer is ", nototest)
        found = True
    mby += 1
    
