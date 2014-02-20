
lengthint = int(input('rows:'))

#pascal's triangle !
def pascal(lst):
    print(lst)
    lst2=[]
    for i in range(len(lst)+1):        
        #print(i)
       # print(len(lst))
       #if first or last item on line (=1)
        if(i<1) or (len(lst) < i+1):
            lst2.append(1)
        #elif(i == 0):
         #   lst2.append(1)
        else:
           # print(lst[i] + lst[i+1])
            lst2.append(lst[i] + lst[i-1])
    if(len(lst) < lengthint):
        pascal(lst2)

pascal([1])
