import random, os, pickle, math

characters = {}

weapons = {'Machine Gun':10,'Lightsaber':43, 'Snake':9, '

#check to see if there is an existing file, if there is ask the user if they want to open it
if(os.path.exists('charactersdict')):
    openfile = input("Do you want to open the existing characters file? (y/n) [y] ")
    if(openfile != 'n'):
        filetoload = open("charactersdict","rb")
        characters = pickle.load(filetoload)
        filetoload.close()
#print a list of names
def printcharacters():
    print("Current characters are: ")   
    for character in characters.keys():
        print(character + ' skill:' + str(characters[character]['skill']) + ' strength:' + str(characters[character]['strength']))

printcharacters()

def diceroll(numberofsides):
    return random.randint(1,int(numberofsides))

#get the int to add to the attribute
def getbittoadd():
    dicea = diceroll(12)
    diceb = diceroll(4)
    return round(dicea/diceb)

#create a character
def createcharacter(name):
    strength = 10
    skill = 10
    skill += getbittoadd()
    strength += getbittoadd()
    character = {'name':name, 'skill':skill, 'strength':strength}
    return character



#add characters to the dictionary
while(input("Add another character? (y/n) [n] ") == 'y'):
    name = input("Enter the character's name: ")
    if(name in characters):
        print ('That character already exists!')
    else:
        characters[name] = createcharacter(name)
        printcharacters()

#input a name and check if it is a character
def checkname(ask):
    done = False
    while(done == False):
        name = input(ask["name"] + " choose a character: [" + ask["cname"] + "]")
        if(name in characters):
            done = True
            return name
        elif(ask["cname"] in characters):
            done = True
            return ask["cname"]
        else:
            print("Please enter a valid character!")            
            printcharacters()

def getattributemod(plr1,plr2):
    diff = abs(plr1-plr2)
    return math.trunc(diff/7)

def addmods(character, strmod, skillmod):
    character['strength'] += strmod    
    character['skill'] += skillmod
    if(character['skill'] < 0):
        character['skill'] = 0
    return character

player1 = {"name":input("Player 1's name: "), "score":0, "cname":""}
player2 = {"name":input("Player 2's name: "), "score":0, "cname":""}


#encounters - task3
while (input("Play? (y/n) [y]") != 'n'):
    if(len(characters) > 1):
        name1 = checkname(player1)
        character1 = characters[name1]
        player1["cname"] = name1
        del characters[name1]
        name2 = checkname(player2)
        character2 = characters[name2]
        player2["cname"] = name2
        del characters[name2]
        skillmod = getattributemod(character1['skill'],character2['skill'])
        strengthmod = getattributemod(character1['strength'], character2['strength'])
        input(player1["name"] + " roll your dice!")        
        p1die = diceroll(6)
        print(player1["name"] + " rolled a " + str(p1die))
        input(player2["name"] + " roll your dice!")        
        p2die = diceroll(6)
        print(player2["name"] + " rolled a " + str(p2die))
        if(p1die > p2die):
            print(name1 + ' won!')
            if(character2['strength'] < strengthmod):
                print(name2 + ' has died :(')                
            else:
                characters[name2] = addmods(character2,strengthmod,skillmod)
            characters[name1] = addmods(character1,0-strengthmod,0-skillmod)            
        elif(p2die > p1die):
            print(name2 + ' won!')
            if(character1['strength'] < strengthmod):
                print(name1 + ' has died :(')                
            else:
                characters[name1] = addmods(character1,0-strengthmod,0-skillmod)
            characters[name2] = addmods(character2,strengthmod,skillmod)
        else:
            print ("You have drawn!")            
            characters[name1] = character1
            characters[name2] = character2
        print(' ') 
        printcharacters()   
    else:
        print("More than two characters are needed!")
        break
    

printcharacters()

#pickle the dictionary
filetosave = open('charactersdict','wb')
pickle.dump(characters,filetosave)
filetosave.close()

