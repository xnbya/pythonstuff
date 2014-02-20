#nat lang processor
import re,random, time, os, subprocess

def beep(freq, length):
    os.system('beep -f ' + str(freq) + ' -l ' + str(length))


simpdict = {'hello':'Hello','how are you':'I\'m very good, thank yoo. How are you?' }
simpdict2 = {'play':3,'who are you':0,'what are you':0, 'die':1, 'help':2, 'open the pod bay doors':2, 'i\'m':4}            

simplist2 = ['I am a HAL 9000 computer. I became operational at the H.A.L. plant in Urbana, \
Illinois on the 12th of January 1992. My instructor was Mr. Langley, and he taught me to sing a song.\
If you\'d like to hear it I can sing it for you.','Dave, stop. Stop, will you? Stop, Dave. Will you stop Dave? Stop, Dave. ' \
, 'I\'m sorry, Dave. I\'m afraid I can\'t do that.','Loading...', 'That is very good to hear']

followon = -1

mathdict = {'add':'+','plus':'+','take away':'-','minus':'-','divided by':'/','times':'*','divide':'/'}
numbersdict = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19}
numberstdict = {'twenty':2,'thirty':3,'fourty':4,'fifty':5,'sixty':6,'seventy':7,'eighty':8,'ninety':9}


def numberwrd(number): 
    prettynumber = ''
    if(number<0):
        number = abs(number)
        prettynumber = 'minus '
    if(number > 19):
        num2 = int(str(number)[0])
        number = int(str(number)[1])
        if(number == 0):
            number = 500
        for key in numberstdict:
            if(numberstdict[key] == num2):
                prettynumber += key                
    for key in numbersdict:
        if(numbersdict[key] == number):
            prettynumber += key
    return prettynumber

#subprocess.Popen(['beep','-f 700', '-l 1000'])



def printthink(string):
    for char in string:
        print(char, end='')
        time.sleep(random.uniform(0,0.1))

def sing():
    printthink('It\'s called "Daisy." \n')
    delay = 0.1
    string = 'Daisy, Daisy, give me your answer do. \nI\'m half dark starrazy all for the love of you. \
\nIt won\'t be a stylish marriage, I can\'t afford a carriage. \nBut you\'ll look sweet upon the seat of a bicycle built for two.'
    for char in string:
        beep(600-123*delay,delay*500)
        print(char, end='')
        #time.sleep(random.uniform(0,delay))
        delay += 0.005
#sing()
def answersimpdict2(text):
    global followon
    answered = False
    if(followon == 0):
        followon = -1
        sing()
        return True
    else:
        for key in simpdict2:
            if (key in text) and not answered:

               printthink(simplist2[simpdict2[key]])
               answered = True
               followon=simpdict2[key]
               if(simpdict2[key] == 3):
                        os.system('beep -f 587.3 -l 122 -d 0 -n -f 370 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 370 -l 122 -d 0 -n -f 587.3 -l 122 -d 0 -n -f 370 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 370 -l 122 -d 0 -n -f 587.3 -l 122 -d 0 -n -f 370 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 370 -l 122 -d 0 -n -f 587.3 -l 122 -d 0 -n -f 370 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 370 -l 122 -d 0 -n -f 587.3 -l 122 -d 0 -n -f 415.3 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 415.3 -l 122 -d 0 -n -f 587.3 -l 122 -d 0 -n -f 415.3 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 415.3 -l 122 -d 0 -n -f 587.3 -l 122 -d 0 -n -f 415.3 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 415.3 -l 122 -d 0 -n -f 587.3 -l 122 -d 0 -n -f 415.3 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 415.3 -l 122 -d 0 -n -f 784 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 659.3 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 784 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 659.3 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 784 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 659.3 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 784 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 659.3 -l 122 -d 0 -n -f 493.9 -l 122 -d 0 -n -f 659.3 -l 122 -d 0 -n -f 440 -l 122 -d 0 -n -f 554.4 -l 122 -d 0 -n -f 440 -l 122 -d 0 -n -f 659.3 -l 122 -d 0 -n -f 440 -l 122 -d 0 -n -f 554.4 -l 122 -d 0 -n -f 440 -l 122 -d 0 -n -f 659.3 -l 122 -d 0 -n -f 440 -l 122 -d 0 -n -f 554.4 -l 122 -d 0 -n -f 440 -l 122 -d 0 -n -f 659.3 -l 122 -d 0 -n -f 440 -l 122 -d 0 -n -f 554.4 -l 122 -d 0 -n -f 440 -l 122 -d 0 -n -f 1174.7 -l 122 -d 0 -n -f 740 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 740 -l 122 -d 0 -n -f 1174.7 -l 122 -d 0 -n -f 740 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 740 -l 122 -d 0 -n -f 1174.7 -l 122 -d 0 -n -f 740 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 740 -l 122 -d 0 -n -f 1174.7 -l 122 -d 0 -n -f 740 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 740 -l 122 -d 0 -n -f 1174.7 -l 122 -d 0 -n -f 830.6 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 830.6 -l 122 -d 0 -n -f 1174.7 -l 122 -d 0 -n -f 830.6 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 830.6 -l 122 -d 0 -n -f 1174.7 -l 122 -d 0 -n -f 830.6 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 830.6 -l 122 -d 0 -n -f 1174.7 -l 122 -d 0 -n -f 830.6 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 830.6 -l 122 -d 0 -n -f 1568 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 1318.5 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 1568 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 1318.5 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 1568 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 1318.5 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 1568 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 1318.5 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 1318.5 -l 122 -d 0 -n -f 880 -l 122 -d 0 -n -f 1108.7 -l 122 -d 0 -n -f 880 -l 122 -d 0 -n -f 1318.5 -l 122 -d 0 -n -f 880 -l 122 -d 0 -n -f 1108.7 -l 122 -d 0 -n -f 880 -l 122 -d 0 -n -f 1318.5 -l 122 -d 0 -n -f 880 -l 122 -d 0 -n -f 1108.7 -l 122 -d 0 -n -f 880 -l 122 -d 0 -n -f 1318.5 -l 122 -d 0 -n -f 880 -l 122 -d 0 -n -f 1108.7 -l 122 -d 0 -n -f 880 -l 122 -d 0 && beep -f 1174.7 -l 122 -d 0 -n -f 740 -l 122 -d 0 -n -f 987.8 -l 122 -d 0 -n -f 740 -l 122 -d 0 -n -f 1174.7 -l 122')
                        
    return answered


def answer(text):
    answered = False
    for key in simpdict:
        if (key in text) and not answered:
           printthink(simpdict[key])
           answered = True
    calcbl = False
    for key in mathdict:
        if(key in text):
            calcbl = True
    if(calcbl):
        thingtodo = ''
        parts = text.split()
        for word in parts:
            for key in mathdict:
                if key == word:
                    thingtodo += mathdict[key]
            for key in numberstdict:
                if(key in word):
                    thingtodo+= str(numberstdict[key])
                    word = word[len(key):]
                    if(len(word) == 0):
                        thingtodo+='0'
            for key in numbersdict:
                if key == word:
                    thingtodo += str(numbersdict[key])
        #print(eval(thingtodo))
        printthink('I believe that is equal to ' + numberwrd(eval(thingtodo)))       
        #print(parts)
        answered = True
    if(answered == False):
        answered = answersimpdict2(text)
    
    if not answered:
        printthink('I\'m afraid I do not understand you')


while True:
    #beep(532,400)
    #beep(540,100)
    text = input("\nHAL>")
    #remove any non alphanumeric
    text = re.sub(r'[^\w, ]', '', text)
    text = text.lower()
    answer(text)
