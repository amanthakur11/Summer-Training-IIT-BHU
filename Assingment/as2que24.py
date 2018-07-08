a=int(input("enter the size of the gameboard: "))
for i in range(a):
    for j in range(a):
        print(a*"-",end=" ")
    print("\n")
    for j in range(a+1):
        print("|",(a-1)*" ",end="")
    print("\n")
for i in range(a):
    print(a*"-",end=" ")
