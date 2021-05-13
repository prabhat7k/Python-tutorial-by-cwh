# break will exit the loop when encountered
# continue go to next iteration of loop ignore all the codes below it when encountered

# question : enter a number and you will be prompted as
# entered number is correctly guessed
# or your number is bigger 
# or your number is smaller
# along with number of attemps left
guessThisNumber=30
i=0
while i<10:
    i=i+1;
    a=int(input("Enter Your Number : "))
    if a==guessThisNumber:
        print("you found the number in ",i," attemps , it was ",guessThisNumber)
        # if this line is encountered then the loop will be breaked by following break command
        break
    if a>guessThisNumber:
        print("you entered a bigger number ",10-i," attemps left")
        # if this line is encountered then the loop will be iterated and the control will go to 
        # while and the loop will be runned again by following continue command
        continue
    if a<guessThisNumber:
        print("you entered smaller number ",10-i," attemps left") 
        # yaha pe isliye ni lgaae continue kyuki aise bhi upar wala  line execute krne ke 
        # baad loop band hi hona tha   
# upar likha program me elif ya if ek hi baat hai kyuki ek baar jab compiler loop ke andar jaega to ye 
# teeno me se koi ek hi if block execute hoga         