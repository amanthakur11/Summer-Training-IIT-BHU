
#que 4
def correct(s):
    s1=""
    k=0
    for i in range(len(s)):
        if s[i]==" ":
            k=k+1
            if(k==1):
                s1=s1+s[i]  
        elif s[i]=='.' and s[i+1]!=" ":
            s1=s1+s[i]+" "
            k=0
        else:
            s1=s1+s[i]
            k=0
        
    return s1
s=input("enter string: ")
print("corected string:",correct(s))
        

#que 5

def make_3sg_form(s):
    if s.endswith('y'):
        return s[:len(s)-1]+"ies"
    elif s.endswith('o') or s.endswith('ch') or s.endswith('s') or s.endswith('sh') or s.endswith('x') or s.endswith('z'):
        return s+"es"
    else:
        return s+"s"
a=input("enter the verb: ")
print("the third person singular form of the verb: ",make_3sg_form(a))


#que 6
def make_ing_form(s):
    s1=s[:len(s)-1]
    s2=s[:len(s)-2]
    if s.endswith('e') and s not in ["be","flee","see","knee"]:
        return s[:len(s)-1]+"ing"
    elif s.endswith('ie'):
        return s[:len(s)-2]+'y'+'ing'
    elif s[-1] not in ['a','e','i','o','u','A','E','I','O','U']:
        if s1[-1] in ['a','e','i','o','u','A','E','I','O','U']:
            if s2[-1] not in ['a','e','i','o','u','A','E','I','O','U']:
                return s+s[-1]+"ing"
            else:
                return s+"ing"
        else:
            return s+"ing"
    else:
        return s+"ing"


a=input("enter the verb: ")
print("the present participle form of the verb is: ",make_ing_form(a))















            
        
