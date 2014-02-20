lstL1 = ['church','champagne','chat','chutzpah','chop','challenge','chocolate','chunder','chips','champion','chaffinch','chainsaw','cholangiogram','churlish','chortle']
#lstL1=[5,4]
print('python sort')
print(lstL1)
#counters
#intSwaps = 0
#intCompa = 0
from datetime import datetime
tstart = datetime.now()
lstL1.sort()
print(lstL1)
#print('swaps',intSwaps,'comparisons',intCompa)
print('Time = ' + str(datetime.now() - tstart))
