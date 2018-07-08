n=input("enter file name: ")
f=open(n,"r")
a=f.read()
#for i in range(len(a)):
   # if a[i]=='.' or a[i]=='?' or a[i]=='!':
       # if a[i+1]==' ':
           # if a[i+2].isupper():
               # if a[i:i+3]!="Mr." and a[i:i+4]!="Mrs." and a[i:i+3]=="Dr.":
                   # print(a[:i+1]
a=a.split(" ")
j=0
for i in range(len(a)):
    if a[i]!="Mr." and a[i]!="Mrs." and a[i]!="Dr.":
        if a[i][len(a[i])-1]=='.' or a[i][len(a[i])-1]=='?' or a[i][len(a[i])-1]=='!':
            if(i!=len(a)-1):
                if(a[i+1][0].isupper()):
                    print(' '.join(a[j+1:i+1]))
                    j=i
            else:
                print(' '.join(a[j+1:i+1]))
            
            