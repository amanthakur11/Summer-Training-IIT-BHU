s="tiger"
k=0
while(k!=1):
    s1=""
    a=input()
    for j in a:
        if j in s:
            if s.index(j)==a.index(j):
                s1=s1+'['+j+']'
            else:
                s1=s1+'('+j+')'
        else:
            s1=s1+j
    print("Clue: ",s1)
    if a==s:
        k=1
        