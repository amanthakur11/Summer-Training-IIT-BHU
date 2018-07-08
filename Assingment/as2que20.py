import random
from random import randint
def password():
    pw=""
    s=input("enter your name: ")
    s=''.join(random.sample(s,len(s)))
    s1="!@#$*$"
    n="0123456789"
    s1=''.join(random.sample(s1,len(s1)))
    t=randint(0,int(len(s)/2))
    t1=randint(0,3)
    if(t1==0):
        pw=pw+s+s1[:t]+n[:t]
    elif(t1==1):
        pw=pw+s1[:t]+n[:t]+s
    else:
        pw=pw+n[:t]+s+s1[:t]
    return(pw)
print(password())
     
            
            