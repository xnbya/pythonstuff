lstL1 = ['church','champagne','chat','chutzpah','chop','challenge','chocolate','chunder','chips','champion','chaffinch','chainsaw','cholangiogram','churlish','chortle']
#lstL1 = [5,4,6,2]
print('insert sort')
print(lstL1)
#counters
#intSwaps = 0
#intCompa = 0
from datetime import datetime
tstart = datetime.now()

#current position
intPos = 1

while(intPos < (len(lstL1)-1)):    
    intLocCurr = intPos
    #go down from current marker
    while(intLocCurr >= 0):# and (lstL1[intLocCurr] > lstL1[intLocCurr+1]):
        #intCompa += 1
        #print('intLocCurr',intLocCurr)
       # print(lstL1)
        if(lstL1[intLocCurr] > lstL1[intLocCurr + 1]):
            #swap
            part = lstL1[intLocCurr]
            lstL1[intLocCurr] = lstL1[intLocCurr + 1]
            lstL1[intLocCurr + 1] = part
           # intSwaps += 1
        intLocCurr -= 1
    intPos += 1
    #print('intPos',intPos)
    #print(lstL1)

print(lstL1)
#print('swaps',intSwaps,'comparisons',intCompa)
print('Time = ' + str(datetime.now() - tstart))

