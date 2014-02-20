import random, os, pickle

players = []

if(os.path.exists('player')):
   openfile = raw_input("Do you want to open the existing file? (y/n) [y]")
   if(openfile != 'n'):
       filetoload = open("players","rb")
       players = pickle.load(filetoload)
       filetoload.close()

print "Current players are "
for player in players:
    

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




while(raw_input("Add another player? (y/n) [n]") == 'y'):
    players.append(createplayer(raw_input("Enter the player's name")))

print players

filetosave = open('players','wb')
pickle.dump(players,filetosave)
filetosave.close()

