#nat lang processor
import re,random, time

simpdict = {'hello':'Hello!','how are you':'I\'m very good, thank you','open the pod bay doors':'I\'m sorry, Dave. I\'m afraid I can\'t do that.' }

mathdict = {'add':'+','minus':'-','times':'*','divide':'/'}
numbersdict = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15,'sixteen':16,'seventeen':17,'eighteen':18,'nineteen':19}
numberstdict = {'twenty':2,'thirty':3,'fourty':4,'fifty':5,'sixty':6,'seventy':7,'eighty':8,'ninety':9}


def numberwrd(number):
    prettynumber = ''
    if(number > 19):
        num2 = int(str(number)[0])
        number = int(str(number)[1])
        for key in numberstdict:
            if(numberstdict[key] == num2):
                prettynumber += key
    for key in numbersdict:
        if(numbersdict[key] == number):
            prettynumber += key
    return prettynumber

def printthink(string):
    for char in string:
        print(char, end='')
        time.sleep(random.uniform(0,0.2))

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
            for key in numbersdict:
                if key == word:
                    thingtodo += str(numbersdict[key])
        printthink('I believe that is equal to ' + numberwrd(eval(thingtodo)))       
        #print(parts)
        answered = True    
    if not answered:
        printthink('I\'m afraid I do not understand you')


while True:
    text = input("\nHAL>")
    #remove any non alphanumeric
    text = re.sub(r'[^\w, ]', '', text)
    text = text.lower()
    answer(text)
