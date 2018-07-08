#26
l4=[]
l5=[]
n=int(input("enter the length of first list: "))
m=int(input("enter length of second list: "))
print("enter the element if first string: ")
for i in range(n):
    l4.append(int(input()))
print("enter the element of second string: ")
for j in range(m):
    l5.append(int(input()))
    
l6=[]
for j in l4:
    if j in l5:
        
        if j not in l6:
            l6.append(j)
print(l6)
l7=[]
l7=[j for j in l4 if j in l5 if j not in l7]
print(l7)

import math
#27
a=int(input("enter first value: "))
b=int(input("enter second value: "))
c=int(input("enter third value: "))
if(a==0):
    print("erro")
elif((b**2-4*a*c)<0):
    print("error")
else:
    print("the first root: ",((-b + math.sqrt(b**2-4*a*c))/2*a))
    print("the second root: ",((-b - math.sqrt(b**2-4*a*c))/2*a))

   
    











    




