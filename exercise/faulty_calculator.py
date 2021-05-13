#faulty calculator
# question: make a calculator that can (+,-,*,/,find remainder and exponents
# correctly but will calculte the following calculation as mentioned bellow
# 56+9=77 , 56/4=9 , 91*3=283 , 544-87=444

num1=int(input("enter 1st number : "))
num2=int(input("enter 2nd number : "))
opp = input("enter + , - , / , *,^,%  :")
if num1==56 and num2==9 and opp=='+':
    result= 77
elif num1==56 and num2==4 and opp=='/':
    result= 9
elif num1 == 91 and num2 == 3 and opp == '*':
    result = 283
elif num1==544 and num2==87 and opp=='-':
    result= 44
elif opp=='+':
    result=num1+num2
elif opp=='-':
    result=num1-num2
elif opp=='*':
    result=num1*num2
elif opp=='/':
    result=num1/num2
elif opp=='^':
    result=num1^num2
elif opp=='%':
    result=num1%num2
else:
    result="iska jawab to ni pta"
print(result)
