# this is if_else tutorial
num1=int(input("enter 1st number : "))
num2=int(input("enter 2nd number : "))
 #comparision
#  normal if else
if (num1>num2):
     print("1st number was greater than 2nd number")
elif (num1>=20) and (num1==10 or num2==30):
    print("ye \'and\' aur \'or\' ka use dekh lo ")
else:
    print("wahi if else ")    

# ye short hand if else hai

a=10
b=20
if a>b: print("a is greater than b")
else: print("b bada hai")

# isko english jaisa padhna
print("b bada hai a se") if b>a else print("a bada hai bhai")