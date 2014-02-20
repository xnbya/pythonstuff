
def pascal(lst):
    print(lst)
    lst2=[]
    for i in range(len(lst)+1):        
        #print(i)
       # print(len(lst))
        if(len(lst) < i+2):
            lst2.append(1)
        #elif(i == 0):
         #   lst2.append(1)
        else:
           # print(lst[i] + lst[i+1])
            lst2.append(lst[i] + lst[i+1])
    if(len(lst) < 50):
        pascal(lst2)

pascal([1])
