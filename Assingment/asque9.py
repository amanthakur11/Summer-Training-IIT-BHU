#que 9
def char_freq_table(a):
    f=open(a,"r")
    a=f.read()
    lc={}
    for l in a:
        lc[l]=lc.get(l,0)+1
    return lc
a=input("enter file name: ")
l1=char_freq_table(a)
for i in sorted(l1.keys()):
    print("frequency of ",i," is: ",l1[i])


