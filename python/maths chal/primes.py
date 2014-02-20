primes = []
numbers = list(range(100))
print(numbers)

for number in numbers:
    x = 1
    while(x<number):
        if(number%x!=0):
            numbers.remove(number)
        x+=1

print(numbers)

    
