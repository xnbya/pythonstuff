import random, os, pickle

players = {}

#check to see if there is an existing file, if there is ask the user if they want to open it
if(os.path.exists('playersdict')):
    openfile = input("Do you want to open the existing players file? (y/n) [y] ")
    if(openfile != 'n'):
        filetoload = open("playersdict","rb")
        players = pickle.load(filetoload)
        filetoload.close()
#print a list of names
def printplayers():
    print("Current players are: ")   
    for player in players.keys():
        print(player)

printplayers()

def diceroll(numberofsides):
    return random.randint(1,int(numberofsides))

#get the int to add to the attribute
def getbittoadd():
    dicea = diceroll(12)
    diceb = diceroll(4)
    return round(dicea/diceb)

#create a player
def createplayer(name):
    strength = 10
    skill = 10
    skill += getbittoadd()
    strength += getbittoadd()
    player = {'name':name, 'skill':skill, 'strength':strength}
    return player



#add players to the dictionary
while(input("Add another player? (y/n) [n] ") == 'y'):
    name = input("Enter the player's name: ")
    players[name] = createplayer(name)
    printplayers()

printplayers()
print(players)

#pickle the dictionary
filetosave = open('playersdict','wb')
pickle.dump(players,filetosave)
filetosave.close()

