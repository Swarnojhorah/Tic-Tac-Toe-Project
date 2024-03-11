#first create a board
#condition check
#Start game
#Instruction
s=["_","_","_","_","_","_","_","_","_"]
def createboard():
    
    print("|",s[0],"|",s[1],"|",s[2],"|")
    print("|",s[3],"|",s[4],"|",s[5],"|")
    print("|",s[6],"|",s[7],"|",s[8],"|")

createboard()
player0 =input("First Player: ")
player1=input("Second Player: ")
print(player0,"You will be using X")
print(player1, "You will be using 0")

def winningcondition(s):
        a='x'
        b='o'
        if s[0]==s[1]==s[2]==a or s[0]==s[1]==s[2]==b:
            return True
        elif s[3]==s[4]==s[5]==a or s[3]==s[4]==s[5]==b:
            return True
        elif s[6]==s[7]==s[8]==a or s[6]==s[7]==s[8]==b:
            return True
        elif s[0]==s[4]==s[8]==a or s[0]==s[4]==s[8]==b:
            return True
        elif s[2]==s[4]==s[6]==a or s[2]==s[4]==s[6]==b:
            return True
        elif s[0]==s[3]==s[6]==a or s[0]==s[3]==s[6]==b:
            return True
        elif s[1]==s[4]==s[7]==a or s[1]==s[4]==s[7]==b:
            return True
        elif s[2]==s[5]==s[8]==a or s[2]==s[5]==s[8]==b:
            return True
        else:
             return False
winningcondition(s)
def startgame(s):
    x=int(input("Enter the position: "))
    if s[x-1]!="_":
        print("Given position already taken, please choose new position: ")
        return startgame(s)
    else:
        return x

for i in range(1,10):
    if i%2!=0:
        print("Turn of First Player",player0)
        y=startgame(s)
        s[y-1]='x'
        createboard()
        if winningcondition(s):
            print("First player",player0,"won the game")
            break
    else:
        print("Turn of Second Player",player1)
        y=startgame(s)
        s[y-1]='o'
        createboard()
        if winningcondition(s):
            print("Second player",player1,"won the game")
            break
        
print("Game Over")
        
        
        
    
    
    
    
    

    
 

