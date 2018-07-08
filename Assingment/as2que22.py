f=open("one.txt","r")
f1=open("two.txt","r")
s=f.read().split("\n")
s1=f1.read().split("\n")
l=[]
for i in s:
    if i in s1:
        l.append(i)
print(l)
