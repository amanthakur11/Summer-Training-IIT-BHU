#28
x=int(input("enter the variable x: "))
l=int(input("enter the length of the list: "))
print("enter the coefficient: ")
l8=[]
for i in range(l):
    l8.append(int(input()))
s=0
j=l
for i in range(l):
    t=x**j
    s=s+t*l8[i]
    j=j-1
print(s)


#29







#30
#a
def query(p,q):
    l=[]
    p=p.split(" ")
    if q in p:
        for i in range(len(p)):
            if(p[i]==q):
                l.append(i)
        return l
    
    return False
w=input("enter the string: ")
q=input("enter the query: ")
print(query(w,q))
print("\n")

#b
t=w.split(" ")
l2=[]
for i in t:
    if i not in l2:
        l2.append(i)
for i in l2:
    print(i,": ",query(w,i))
    
    
