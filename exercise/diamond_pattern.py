# diamond builder

num1=int(input("enter the number"))
for x in range(0,num1):
    print()
    for z in range(0,num1-x):
        print(' ',end='')
    for y in range(1,(x)+1):
        print(chr(y+64) , end='')
    for a in range(1,(x)):
        print(chr(x-a+64) , end='')


for x in range(0, num1):
    print()


    for z in range(0,x):
        print(' ',end='')
    for y in range(1,(num1-x+1)):
        print(chr(y+64) , end='')
    for a in range(1,(num1-x)):
        print(chr(num1-x-a+64) , end='')
