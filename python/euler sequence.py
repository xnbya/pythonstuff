
x = 0
product = 0
while (x < 1000):
    if(x%3 == 0):
        print(x)
        product += x
    elif(x%5 == 0):
        print(x)
        product += x
    x += 1

print(product)
