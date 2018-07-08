print("guess any no in your mind: ")
print("press any key after guessing: ")
c=input()
if(c):
    k=0 
    a=0
    b=101
    ct=0
    while(k!=1):
        m=(a+b)//2
        print("no guessed by me: ",m)
        print("1.too high\n2.too low\n3.your no")
        ch=int(input())
        if ch==1:
            b=m
        elif ch==2:
            a=m
        else:
            print("your guessed no: ",m)
            k=1
        ct=ct+1
    print("i guessed your no in ",ct," times")
else:
    print("tyr again!")
