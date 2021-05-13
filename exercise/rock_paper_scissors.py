# qustion: build a rock paper scissor game 
# play 10 times and get promted who wins and number of rounds left
# at the end display who wis how many times and the final winner
import random
i=0
h=0
c=0
t=0
def comparator(a,b):
    if(a==1):
        print("computer choose rock")
    elif (a == 2):
        print("computer choose paper")
    else:
        print("computer choose scissor")
    if ((a==1 and b=='p') or (a==2 and b=='s') or (a==3 and b=='r')):
        return 1
    if (a==1 and b=='r') or (a==2 and b=='p') or (a==3 and b=='s'):
        return 2
    else:
        return 0


while(i<10):
    i+=1
    print(f"round {i}")
    inp=input("dikhao (r,p,s)\n")
    compi=random.randrange(1,3,1)
    out=comparator(compi, inp)
    if out==1:
        #print("you win")
        h+=1
    elif out==2:
        #print("tie")
        t+=1
    else:
        #print("Computer won")
        c+=1
    print("")
    print(f"you win {h} times \ncomputer won {c} times\ntied {t} times")
if h>c:
    print("you won")
else :
    print("you loose")