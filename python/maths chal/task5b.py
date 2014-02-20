maxfactor = int(input("Enter the largest factor"))

currentfactor = 1
#1 to maxfactor

currentnumber = 1
#the answer

#return the lowest common multiple of 2 numbers, b should be bigger
def lcm(a,b):
    x = 1
    found = False
    while not found:
        #print(x)
        if((x * b) % a == 0):
            found = True
            return x * b
        x += 1


#put the numbers 1 to maxfactor and the currentnumber into lcm
while(currentfactor < maxfactor):
    currentnumber = lcm(currentfactor,currentnumber)
    currentfactor += 1
    print("cn:",currentnumber,"cf:",currentfactor)

print("answer",currentnumber)
