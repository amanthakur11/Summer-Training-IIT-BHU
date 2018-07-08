#5
#using reduce function
l=[2,3,1,54,3]
def max_in_list(l):
    return max(l)
def reduce(a,k):
    print("max is",a(k))
reduce(max_in_list,l)

#6

#using for loop
w=["asd","asdf","er","qwert"]
l1=[]
for i in range(len(w)):
    l1.append(len(w[i]))
print(l1)

#using map function
l2=[]
def wordlen(x):
    return len(x)
def map(d,h):
    for i in range(len(h)):
        l2.append(wordlen(h[i]))
map(wordlen,w)
print(l2)

#comprehension
l3=[len(w[i]) for i in range(len(w))]
print(l3)
