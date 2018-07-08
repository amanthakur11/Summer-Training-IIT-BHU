#que 7

a=input("enter the file name: ")
f=open(a,"r")
l=f.readlines()
c=0
for j in range(len(l)):
    s=l[j][:len(l[j])-1]
    e=s
    s=s.split(" ")
    s="".join(s)
    s1=""
    s2=""
    for i in range(len(s)):
        if s[i] in [',','!','\'','?','"',"."]:
            continue
        else:
            if(s[i].islower()):
                s2=s2+s[i]
            else:
                s2=s2+ s[i].lower()
    i=len(s2)-1
    while(i!=-1):
        s1=s1+s2[i]
        i=i-1

    if(s1==s2):
        print("palindromic line in file: ",e)
        c=c+1
if c==0:
    print("there is no palindromic line in the file; ")
        
    
