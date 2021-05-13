# question: enter a number and display its corresponding alphabet (also for number greater than 26)
# example: 
#             enter a number : 28
#             AB

num=int(input("enter your number"))
s=0
i=0
a=0
while s<num:
   i+=1
   s=s + (26**i)
   #print(s)
   #print(i)
for j in range(i):
    a=a+ 26**j
    #print(a)
num=num-a
s=""
for j in range(i):
    c=chr((num%26)+65)
    s=str(c)+s
    #print(num)
    #print(c)
    #print(s)

    num=num//26
print(s)
print("number a is greater than 26" ) if num>26 else print("number is lesser than 26")
