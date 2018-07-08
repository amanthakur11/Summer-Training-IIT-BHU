def maxm(a,b,c):
    m=a
    if(b>m):
        m=b
    if(c>m):
        m=c
    return m
a=int(input("enter first no: "))
b=int(input("enter second no: "))
c=int(input("enter third no: "))
print("maximmum no: ",maxm(a,b,c))