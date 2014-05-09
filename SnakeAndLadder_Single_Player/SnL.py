import random

def rolldice():
    sum = 0
    while(sum!=1):
        raw_input("Enter to roll dice ")
        sum = random.randrange(1,7)
        print "You got "+str(sum)+"\n"
        
    print "Ok..you are into the game now \n" 
    while(sum!=100):
        raw_input("enter to roll dice")
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

    print "Congrats...."
def SorL(x):
    return{6:16,9:31,19:38,21:79,28:84,51:67,72:92,80:100,18:5,43:23,49:33,56:26,65:44,88:63,92:71,99:35}.get(x,x)
                  
    

rolldice()
