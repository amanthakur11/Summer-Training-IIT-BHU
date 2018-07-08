import string
#19
def max_in_list(l):
    return max(l)
l=[2,3,54,6,7,564,23]
print(max_in_list(l))


#20
l1=["asd","serfc","sfdfrgthyrgth","sdfererf","edrv"]
l2=[]
def length(x):
    return len(x)
def map(a,b):
    for i in b:
        l2.append(a(i))
map(length,l1)
print(l2)


#21
def find_longest_word(w):
    m=len(w[0])
    
    for i in range(len(w)):
        if m<len(w[i]):
            m=len(w[i])
            g=w[i]
    return g

print(find_longest_word(l1))


#22
l3=[]
def filter_long_words(l,n):
    for i in l:
        if len(i)>n:
            l3.append(i)
n=int(input("enter the length: "))
filter_long_words(l1,n)
print(l3)


#23
s=input("enter the string/phrase: ")
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
    print("palindrome")
else:
    print("not palindrome")



#24
z=input("enter the string: ")
l= []
for ch in z:
    if ch not in l:
        l.append(ch)
z="".join(l)
c=0
for x in range(len(z)):
    if(string.ascii_lowercase.find(z[x])!=-1):
        c=c+1;
if(c==26):
    print("given sentence is panagram")
else:
    print("given sentence is not panagram")




#25
y=input("enter the string: ")
y=y.split(" ")
l3=[]
i=len(y)-1
while(i!=-1):
    l3.append(y[i])
    i=i-1
y1=" ".join(l3)
    
print(y1)

























        
    
