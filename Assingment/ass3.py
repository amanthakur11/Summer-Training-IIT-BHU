
    #QUE 3

key={'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z','n':'a','o':'b',
     'p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m','A':'N','B':'O',
     'C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z','N':'A','O':'B'
    ,'P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I','W':'J','X':'K','Y':'L','Z':'M'}


def encode(s):
    s1=""
    for i in s:
        if i in key.keys():
            s1=s1+key[i]
        else:
            s1=s1+i
    return s1
def decode(s):
    s2=""
    for i in s:
        if i in key.values():
            for j in key.keys():
                if(key[j]==i):
                    s2=s2+j
        else:
            s2=s2+i
    return s2

s=input("enter the string: ")
ch=int(input("1.encode\n2.decode"))
if(ch==1):
    print("your encoded string is: ",encode(s))
elif(ch==2):
    print("your decoded string is: ",decode(s))
