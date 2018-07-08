#que 13
from random import randint
def no():
    n=int(input("Take a quess"))
    return n
t=randint(1,20)
k=0
n=0
name=input("Hello! What is your name?")
print("Well, ",name,", I am thinking of a number between 1 and 20.")
while(k!=1):
    n=no()
    if(n<20):
        if(n==t):
            print("you won..")
            k=1
        else:
            print("your guess is too low")
    else:
        print("please enter no between 1 and 20.")
        
        