import random, os, pickle

players = {}

if(os.path.exists('~/Docs/python/playersdict')):
    openfile = input("Do you want to open the existing file? (y/n) [y] ")
    if(openfile != 'n'):
        filetoload = open("playersdict","rb")
        players = pickle.load(filetoload)
        filetoload.close()

def printplayers():
    print("Current players are: ")   
    for player in players.keys():
        print(player)

printplayers()

def diceroll(numberofsides):
    return random.randint(1,int(numberofsides))

def getbittoadd():
    dicea = diceroll(12)
    diceb = diceroll(4)
    return round(dicea/diceb)

def createplayer(name):
    strength = 10
    skill = 10
    skill += getbittoadd()
    strength += getbittoadd()
    player = {'name':name, 'skill':skill, 'strength':strength}
    return player




while(input("Add another player? (y/n) [n] ") == 'y'):
    name = input("Enter the player's name: ")
    players[name] = createplayer(name)
    printplayers()

printplayers()
print(players)

filetosave = open('playersdict','wb')
pickle.dump(players,filetosave)
filetosave.close()

