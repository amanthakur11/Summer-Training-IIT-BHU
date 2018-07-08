f=open("unixdict.txt","r")
f=f.read().split(" ")
a=input("enter the word: ")
l=len(a)
s=a[0]
s1=a[1]
if(l%2==0):
    l1=l/2
else:
    l2=l/2 +1
