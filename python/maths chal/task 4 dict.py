import random, os, pickle, math

characters = {}

weapons = {'Machine Gun':34, 'Lightsaber':86, 'Snake':33}


def beep(freq, length):
    os.system('beep -f ' + str(freq) + ' -l ' + str(length))

'''beep(494,200)
beep(988,340)
beep(784,1000)'''





def shoot():
    x = 3000
    while (x > 0):
        beep(x,5)
        x = x - 5
        number = int(str(number)[1])
        for key in numberstdict:

shoot()

#startup sound    
os.system('beep -f 659 -l 460 -n -f 784 -l 340 -n -f 659 -l 230 -n -f 659 -l 110 -n \
     -f 880 -l 230 -n -f 659 -l 230 -n -f 587 -l 230 -n \
     -f 659 -l 460 -n -f 988 -l 340 -n -f 659 -l 230 -n -f 659 -l 110 -n \
     -f 1047 -l 230 -n -f 988 -l 230 -n -f 784 -l 230 -n -f 659 -l 230 -n \
     -f 988 -l 230 -n -f 1318 -l 230 -n -f 659 -l 110 -n -f 587 -l 230 -n \
     -f 587 -l 110 -n -f 494 -l 230 -n -f 740 -l 230 -n -f 659 -l 460')


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

def weaponadd(player,name1):
    print(player["name"] + ", your character " + name1 + " can one of the following weapons")
    for key in weapons.keys():
        print(key)
    weapon = input('Select a weapon: ')
    while(weapon not in weapons):
       
        print('that weapon doesn\'t exist')
        weapon = input('Select a weapon: ')
    return weapons[weapon]



def diesf():
    os.system('beep -l 350 -f 392 -D 100 -n -l 350 -f 392 -D 100 -n -l 350 -f 392 \
     -D 100 -n -l 250 -f 311.1 -D 100 -n -l 25 -f 466.2 -D 100 -n \
     -l 350 -f 392 -D 100 -n -l 250 -f 311.1 -D 100 -n -l 25 -f 466.2 \
     -D 100 -n -l 700 -f 392 -D 100 -n -l 350 -f 587.32 -D 100 -n \
     -l 350 -f 587.32 -D 100 -n -l 350 -f 587.32 -D 100 -n -l 250 \
     -f 622.26 -D 100 -n -l 25 -f 466.2 -D 100 -n -l 350 -f 369.99 \
     -D 100 -n -l 250 -f 311.1 -D 100 -n -l 25 -f 466.2 -D 100 -n \
     -l 700 -f 392 -D 100 -n -l 350 -f 784 -D 100 -n -l 250 -f 392 \
     -D 100 -n -l 25 -f 392 -D 100 -n -l 350 -f 784 -D 100 -n \
     -l 250 -f 739.98 -D 100 -n -l 25 -f 698.46 -D 100 -n \
     -l 25 -f 659.26 -D 100 -n -l 25 -f 622.26 -D 100 -n \
     -l 50 -f 659.26 -D 400 -n -l 25 -f 415.3 -D 200 -n \
     -l 350 -f 554.36 -D 100 -n -l 250 -f 523.25 -D 100 -n \
     -l 25 -f 493.88 -D 100 -n -l 25 -f 466.16 -D 100 -n \
     -l 25 -f 440 -D 100 -n -l 50 -f 466.16 -D 400 -n \
     -l 25 -f 311.13 -D 200 -n -l 350 -f 369.99 -D 100 -n \
     -l 250 -f 311.13 -D 100 -n -l 25 -f 392 -D 100 -n \
     -l 350 -f 466.16 -D 100 -n -l 250 -f 392 -D 100 -n \
     -l 25 -f 466.16 -D 100 -n -l 700 -f 587.32 -D 100 -n \
     -l 350 -f 784 -D 100 -n -l 250 -f 392 -D 100 -n \
     -l 25 -f 392 -D 100 -n -l 350 -f 784 -D 100 -n \
     -l 250 -f 739.98 -D 100 -n -l 25 -f 698.46 -D 100 -n \
     -l 25 -f 659.26 -D 100 -n -l 25 -f 622.26 -D 100 -n \
     -l 50 -f 659.26 -D 400 -n -l 25 -f 415.3 -D 200 -n \
     -l 350 -f 554.36 -D 100 -n -l 250 -f 523.25 -D 100 -n \
     -l 25 -f 493.88 -D 100 -n -l 25 -f 466.16 -D 100 -n \
     -l 25 -f 440 -D 100 -n -l 50 -f 466.16 -D 400 -n \
     -l 25 -f 311.13 -D 200 -n -l 350 -f 392 -D 100 -n \
     -l 250 -f 311.13 -D 100 -n -l 25 -f 466.16 -D 100 -n \
     -l 300 -f 392.00 -D 150 -n -l 250 -f 311.13 -D 100 -n')



#encounters - task3
while (input("Play? (y/n) [y]") != 'n'):
    if(len(characters) > 1):
        #load characters
        name1 = checkname(player1)
        character1 = characters[name1]
        player1["cname"] = name1
        del characters[name1]
        name2 = checkname(player2)
        character2 = characters[name2]
        player2["cname"] = name2
        del characters[name2]
        #get the modifiers
        skillmod = getattributemod(character1['skill'],character2['skill'])
        strengthmod = getattributemod(character1['strength'], character2['strength'])
        #unessecary parts
        input(player1["name"] + " roll your dice!")        
        p1die = diceroll(6)
        print(player1["name"] + " rolled a " + str(p1die))
        input(player2["name"] + " roll your dice!")        
        p2die = diceroll(6)        
        print(player2["name"] + " rolled a " + str(p2die))
        #weapons
        #if(character1['skill'] > character2['skill']):
        p1die += weaponadd(player1,name1) * character1['skill']
        #else:
        p2die += weaponadd(player2,name2) * character1['skill']
        #soundfx
        shoot()
        
            


        
        #find out who won
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
                diesf()
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
        #someone must have died
        print("More than two characters are needed!")
        break
    

printcharacters()

#pickle the character dictionary
filetosave = open('charactersdict','wb')
pickle.dump(characters,filetosave)
filetosave.close()

