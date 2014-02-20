import math

intLength = int(input("How many?"))

from datetime import datetime
tstart = datetime.now()

lstPrimes = list()
intCurrent = 3
lstPrimes.append(2)

while(len(lstPrimes) < intLength):
    blPrime = True
    y = 2
    while(y < math.sqrt(intCurrent) + 1 and blPrime):       
        if(intCurrent % y == 0):
            blPrime=False
        y += 1
    if(blPrime):
        #print(intCurrent)
        lstPrimes.append(intCurrent)
    intCurrent += 2

#print(lstPrimes)
print('Answer:' + str(intCurrent - 2))
print('Time = ' + str(datetime.now() - tstart))
