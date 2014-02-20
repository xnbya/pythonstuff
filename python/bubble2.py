lstL1 = ['church','champagne','chat','chutzpah','chop','challenge','chocolate','chunder','chips','champion','chaffinch','chainsaw','cholangiogram','churlish','chortle']
#lstL1=[5,4]
print('bubble sort')
print(lstL1)
#counters
#intSwaps = 0
#intCompa = 0
from datetime import datetime
tstart = datetime.now()

#current position
intPos = 0
#where we need to go up to
intEnd = len(lstL1) - 1
while(intEnd > 0):
    #do we need to swap?
    #intCompa += 1
    if(lstL1[intPos] > lstL1[intPos+1]):
        part = lstL1[intPos]
        lstL1[intPos] = lstL1[intPos + 1]
        lstL1[intPos + 1] = part
       # intSwaps += 1
    #move one down the list
    intPos += 1
    #if we have reached the end, the last one is correct, so we start again
    if((intPos) == intEnd):
        intEnd -= 1
        intPos = 0
    #print(intEnd)
print(lstL1)
#print('swaps',intSwaps,'comparisons',intCompa)
print('Time = ' + str(datetime.now() - tstart))
