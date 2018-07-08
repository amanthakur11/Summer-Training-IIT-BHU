#que 10
import string
def hapax(a):
    f=open(a,"r")
    l=[]
    for i in f.read().split():
        l.append(i.lower())
    for i in l:
        c=0
        for j in l:
            if(i==j):
                c=c+1
        if(c==1):
            print(i)
            
a=input("enter file name: ")
hapax(a)

