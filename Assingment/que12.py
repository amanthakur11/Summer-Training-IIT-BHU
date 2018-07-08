#que 12
a=input("enter file name: ")
f=open(a,"r")
l=[]
for i in f.read().split():
    l.append(i)
c=0
for i in l:
    c=c+len(i)
print("average length: ",c/len(l))
