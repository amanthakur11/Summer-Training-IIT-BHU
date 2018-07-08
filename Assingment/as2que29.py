from random import randint
f=open("sowpods.txt","r")
s=f.read().split("\n")
t=randint(0,len(s))
print("the random word from sowpods list: ",s[t])
