
#assingment 2
#que 1
dic={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
def translate(l):
    l1=[]
    for i in l:
        if i in dic.keys():
            l1.append(dic[i])
    return l1     
a=input("enter the english words: ")
a=a.split(" ")
t=translate(a)
t=" ".join(t)
print(t)




#que 2

def char_freq(a):
    lc={}

    for l in a:
        lc[l]=lc.get(l,0)+1
    return lc
    
s=input("enter the string: ")
print(char_freq(s))


                
            
    

        
