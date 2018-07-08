#que 11
a=input("enter the file name: ")
b=input("enter the file name in which you want write: ")
r=open(a,"r")
w=open(b,"w")
l=r.readlines()
c=1
for i in l:
    w.write(str(c))
    w.write('.')
    w.write(i)
    c=c+1
r.close()
w.close()
r1=open(b,"r")
print(r1.read())
r1.close()
