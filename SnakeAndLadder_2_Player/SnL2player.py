import random

user1 = raw_input("enter user1's name ")
user2 = raw_input("enter user2's name ")

userDict = {user1:0,user2:0}


def rolldice():
    sum1, sum2 = 1,1
    while(sum1!=100 or sum2!=100):
        if(userDict[user1]!=1):
            raw_input(user1+" Enter to roll dice to get into game")
            userDict[user1] = random.randrange(1,7)
            print "You got "+str(userDict[user1])+"\n"
            #if(userDict[user1]==1):continue
            
        if(userDict[user2]!=1):
            raw_input(user2+" Enter to roll dice to get into game")
            userDict[user2] = random.randrange(1,7)
            print "You got "+str(userDict[user2])+"\n"
            #if(userDict[user2]==1):continue
            
        if(userDict[user1]==1):
            sum1 = climb(user1,sum1)

        if sum1 == 100:
            print "Congrats "+user1+" you won."
            break;

        if(userDict[user2]==1):
           sum2 = climb(user2,sum2)

        if sum2 == 100:
            print "Congrats "+user2+" you won."
            break;



def climb(un,sum):
    raw_input(un+" enter to roll dice")
    dice = random.randrange(1,7)
    print "you got "+str(dice) +"\n"
    sum = sum+ dice
    if( sum >100):
        print "Sorry try again"
        sum = sum- dice
    print "now you are at " + str(sum) +"\n"
    if SorL(sum) > sum:
        print "you got a ladder to "+str(SorL(sum))+"\n"
    elif SorL(sum) < sum:
        print "you got bit by a snake "+str(SorL(sum))+"\n"
        
    sum = SorL(sum)
    return sum
           
def SorL(x):
    return{6:16,9:31,19:38,21:79,28:84,51:67,72:92,80:100,18:5,43:23,49:33,56:26,65:44,88:63,92:71,99:35}.get(x,x)
                  
    

rolldice()
