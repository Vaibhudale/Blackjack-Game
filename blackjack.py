#list comprehension:
#k[i for i in range(11)]
#simple list creaation:
#k=[] for i in range(11) k.append(i) now k is list
from random import randint
#randint chooses a random integer from the given list
class Cards():
    cards={
        0:[i for i in range(1,11)],#red heart
        1:[i for i in range(1,11)],#red diamond
        2:[i for i in range(1,11)],#black spade
        3:[i for i in range(1,11)],#black flower #kin=joker=queen=10
        }#dictionary of cards
    print(cards)
    
class Dealer(Cards):
    dealercards=[]
    def __init__(self):
        i,j=randint(0,3),randint(0,9)#gives random cards from random sets.i for index of cards j for card numbers
        dc1=self.cards[i][j]
        i,j=randint(0,3),randint(0,9)
        dc2=self.cards[i][j]
        #appending to the card list
        self.dealercards.append(dc1)
        self.dealercards.append(dc2)
    def takeonecard(self):
        i,j=randint(0,3),randint(0,9)
        rc=self.cards[i][j]
        self.dealercards.append(rc)    
    
    
class User(Cards):
    usercards=[]
    def __init__(self):
        i,j=randint(0,3),randint(0,9)#gives random cards from random sets.i for index of cards j for card numbers
        uc1=self.cards[i][j]
        i,j=randint(0,3),randint(0,9)
        uc2=self.cards[i][j]
        self.usercards.append(uc1)
        self.usercards.append(uc2)
    def choose_option(self):
        print("1.HIT")
        print("2.STAND")
        option=input("PLEASE SELECT AN OPTION: ")
        return option
    def takeonecard(self):
        i,j=randint(0,3),randint(0,9)
        rc=self.cards[i][j]
        self.usercards.append(rc)
    
d=Dealer()
u=User()
print("dealer",d.dealercards)
print("user",u.usercards)
while u.choose_option().lower()!="stand":
    d.takeonecard()
    u.takeonecard()
    print("my cards: ",u.usercards)
    print("dealer cards: ",d.dealercards)
    if sum(u.usercards)>21:
        print("i lost the game")
        break #bcuz it should not ask hit ans
    elif sum(d.dealercards)>21:
        print("dealer lost the game")
        break 
        
if sum(u.usercards)>sum(d.dealercards):
    print("user won the game")
elif sum(u.usercards)<sum(d.dealercards):
    print("dealer won the game")
else:
    print("draw")

