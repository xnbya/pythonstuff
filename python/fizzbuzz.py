x = 1
lst=[]
while(x<=100):
    if(x%3==0):
       if(x%5==0):
           lst.append("FizzBuzz")           
       else:
           lst.append("Fizz")
    elif(x%5==0):
       lst.append("Buzz")
    else:
       lst.append(x)
    x+=1

for item in lst:
    print(item)
