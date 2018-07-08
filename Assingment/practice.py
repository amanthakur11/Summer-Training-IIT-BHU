#1
for i in range(2,11):
    print(1/i)


#2
def val():
    a=int(input("enter any no: "))
    return a
k=0
while(k!=1):
    a=val()
    if(a>=0):
        while(a!=-1):
            print(a)
            a=a-1
            k=1
    else:
        print("you entered a negative no please enter positive no: ")




#3
c=int(input("enter base: "))
b=int(input("enter exponent: "))
exponent=1
for j in range(b):
    exponent=exponent*c
print(c," power ",b,"=",exponent)
    



#4
def even():
    n=int(input("enter the no: "))
    return n%2
d=0
f=0
while(d!=1):
    if(even()==0):
        print("congratulations you entered a even no: ")
        d=1
    else:
       print("sorry ,please enter a even no: ")
       

