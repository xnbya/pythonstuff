import random
cont = True
while cont:
    print 'Please enter the number of sides (4,6 or 12)'
    numberofsides = raw_input()
    if numberofsides == '4' or numberofsides == '6' or numberofsides == '12':
        throw = random.randint(1,int(numberofsides))
        print numberofsides,' sided dice thrown, score ',throw
    else:
        print "Please enter 4, 6 or 12"
    print "Throw again? (y/n) [y]"
    if raw_input() == 'n':
        cont = False
    
