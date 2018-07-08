#13
def reverse(a):
    x=""
    i=len(a)-1
    while(i!=-1):
        x=x+a[i]
        i=i-1
    return x

print(reverse("i am testing"))


#14
a=input("enter the string: ")
c=reverse(a)
if(c==a):
    print("palindrome: ")
else:
    print("not palindrome: ")

#15
def is_member(a,l):
    if a in l:
        return True
    else:
        return False

l=[1,2,3,4,5]
l1=["asd","aman","ankit"]
a=int(input("enter the no to check it is memeber of given list: "))
if(is_member(a,l)):
    print("yes ",a," is member of list")
else:
    print(a," is not memeber of list")
b=input("enter the string to check it is member of list or not: ")
if(is_member(b,l1)):
    print("yes ",b," is member of list")
else:
    print(b," is not memeber of list")



#16
def overlapping(g,h):
    for i in range(len(g)):
        for j in range(len(h)):
            if(g[i]==h[j]):
                return True
    return False
g=input("enter first string: ")
h=input("enter second string: ")
if(overlapping(g,h)):
    print("overlapps")
else:
    print("not overlapps")




#17
def generate_n_chars(n,c):
    x=""+c*n
    return x
print(generate_n_chars(5,"x"))




#18

def histogram(l):
    for i in l:
        for j in range(i):
            print("*",end='')
        print("\n")

ll=[4,9,7]
histogram(ll)













