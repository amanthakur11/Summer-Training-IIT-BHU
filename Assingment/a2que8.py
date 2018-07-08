#que 8
a=input("enter the file name: ")
f=open(a,"r")
l=[]
for i in f.read().split():
    l.append(i)
    
for i in l:
    s=""
    k=len(i)-1
    while(k!=-1):
        s=s+i[k]
        k=k-1

    if s in l:
        print(i," ",s)

        

