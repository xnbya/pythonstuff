import random
def diceroll(numberofsides):
    return random.randint(1,int(numberofsides))

strength = 10
skill = 10

def getbittoadd():
    dicea = diceroll(12)
    diceb = diceroll(4)
    return round(dicea/diceb)

skill += getbittoadd()
strength += getbittoadd()

print(skill)
print(strength)
