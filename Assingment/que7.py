#7
w=["asd","asdfdrt","er","qwert"]
print(max(w))
l2=[]
def wordlen(x):
    return len(x)
def map(d,h):
    for i in range(len(h)):
        l2.append(wordlen(h[i]))
map(wordlen,w)
print(max(l2))

#8
l3=[]
def filter_long_words(x):
    return len(x)
def filter(d,h):
    a=int(input("enter the length: "))
    for i in range(len(h)):
        c=filter_long_words(h[i])
        if(c>a):
            l3.append(h[i]

                      )
filter(filter_long_words,w)
print(l3)


#9
def max_of_three(x,y,z):
    m=x
    if(y>m):
        m=y
    if(z>m):
        m=z
    return m
print(max_of_three(2,4,5))



#10

def vowel(x):
    if x in ['a','A','e','E','i','I','o','O','u','U']:
        return True

s=input("enter a character: ")
if(vowel(s)):
    print("entered value is vowel: ")
else:
    print("entered value is not vowel: ")





#11
def translate(x):
    s1=""
    for i in range(len(x)):
        if x[i] not in ['a','A','e','E','i','I','o','O','u','U'," "]:
            s1=s1+x[i]+'o'+x[i]
        else:
            s1=s1+x[i]
    return s1
print(translate("this is fun"))





#12
def suma(a):
    s=0
    for i in range(len(a)):
        s=s+a[i]
    return s
def mul(a):
    m=1
    for i in range(len(a)):
        m=m*a[i]
    return m
a=[1,3,4,5,2]
print("sum of no in list is: ",suma(a))
print("multiplication of no in list: ",mul(a))



















































