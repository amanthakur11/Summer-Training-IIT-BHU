import numpy
import pandas as pd
def nn(m1,m2,w1,w2,b):
    z=m1*w1+m2*w2+b
    return sigmoid(z)
def sigmoid(x):
    return 1/(1+numpy.exp(-x))
w1=numpy.random.randn()
w2=numpy.random.randn()
b=numpy.random.rand()
dataset=pd.read_csv("iris.csv")
dataset=dataset.values
#print(dataset)
train=[]
for i in dataset:
    train.append(i[2:])
for i in train:
    if i[-1]=='Setosa':
        i[-1]=0
    elif i[-1]=='Versicolor':
        i[-1]=1
    else:
        i[-1]=2
    
phrases=['seems like its','i quess','i think','possibly','looks like','guessing..']
#data=[[3,1.5,1],[2,1,0],[4,1.5,1],[3,1,0],[3.5,1.5,1],[2,5,0],[5.5,1,1],[1,1,0]]
rand_data=train[numpy.random.randint(len(train))]
m1=rand_data[0]
m2=rand_data[1]


prediction=nn(m1,m2,w1,w2,b)
print(prediction)
prediction_text=['blue','red'][int(numpy.round(prediction))]
phrase=numpy.random.choice(phrases)+" "+prediction_text
print(phrase)
print("it's really "+["blue","red"][rand_data[2]])



























































