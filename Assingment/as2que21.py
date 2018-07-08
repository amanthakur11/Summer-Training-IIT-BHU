import random
from random import randint
def password(ch):
    pw=""
    s=input("enter your name: ")
    s=''.join(random.sample(s,len(s)))
    s1="!@#$*$"
    n="0123456789"
    s1=''.join(random.sample(s1,len(s1)))
    t=randint(0,int(len(s)/2))
    
    if(ch==0):
        pw=pw+s+s1[:2]+n[:2]
    elif(ch==1):
        pw=pw+s1[:4]+n[:4]+s
    else:
        pw=pw+n[:5]+s+s1[:5]
    return(pw)
    
def passw(l,a):
    for i in l:
        if i==a:
            return True
    return False
l=[11,2,3,4,1,5,6,66,44,67,7,8,55,56,54]
l=sorted(l)
a=int(input("enter the no: :"))
if(passw(l,a)):
    print("1.strong password\n2.stronger password\n3.strongest password")
    ch=int(input())
    if(ch==1):
        print("strong password: ",password(ch))
    elif(ch==2):
        print("stronger password: ",password(ch))
    else:
        print("stronggest password: ",password(ch))
else:
    print("your enterd no is not in list: ")
        
        