x = 0

def pascal(lst):        
        lst2 = lst
        lst2.append(1)
        for i in range(len(lst)):
                if(i<len(lst)-1):
                        lst2[i] += lst[i+1]                      

        pascal(lst2)
        if(len(lst)<10):
                pascal(lst2)
        


print(pascal([1]))


