lstIN = [54,76,12,34,98,56,23,12,34,56,77,4,32,1,5]

def do2rows(lstTop,lstBot):
    intLocTop = 0
    intLocBot = 0
    while(intLocBot < len(lstBot)):
        for _ in range(2):
            if(intLocBot < len(lstBot)):
                print(lstBot[intLocBot])
                print(lstBot[intLocBot])
                if(lstBot[intLocBot] > lstTop[intLocTop]):
                    part = lstBot[intLocBot]
                    lstBot[intLocBot] = lstTop[intLocTop]
                    lstTop[intLocTop] = part
            intLocBot += 1
        intLocTop += 1
    return ([lstTop, lstBot])
            


lstLsts = []
intAdded = 0
while(intAdded < len(lstIN)):
    intNumInRow = 2**(len(lstLsts))
   # print('s')
    #print(len(lstLsts))
    #print(intAdded)
    #print(intNumInRow)
    
    lstRow = lstIN[intAdded:intNumInRow+intAdded]
    intAdded += len(lstRow)
    lstLsts.append(lstRow)
print(lstLsts)

intDone = len(lstLsts)
while(intDone > 1):
    lstReturn = do2rows(lstLsts[intDone-2],lstLsts[intDone-1])
    print('e')
    print(lstReturn)
    
    print(lstLsts)
    lstLsts[intDone-2] = lstReturn[0]
    lstLsts[intDone-1] = lstReturn[1]
    print(lstLsts)
    intDone -= 1
    



print(lstLsts)
