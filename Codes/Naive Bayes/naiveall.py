import pandas as pd
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

url="https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.data"
dataset=pd.read_csv(url, sep=',', header=None)
#dataset=np.loadtxt(raw_data,delimiter=',')
#print(dataset)
x=dataset.values[:,0:48]
y=dataset.values[:,-1]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33, random_state=17)

#using nernoulis

bern=BernoulliNB(binarize=0.1)
bern.fit(x_train,y_train)
#print(bern)
y_pred=bern.predict(x_test)
print("accuracy of bernouli model: ",accuracy_score(y_test,y_pred))

#using mulitinomial naive bayes theeorem
multinb=MultinomialNB()
multinb.fit(x_train,y_train)
#print(multinb)
y_pred=multinb.predict(x_test)
print("accuracy of mulitinomial model: ",accuracy_score(y_test,y_pred))

gaussnb=GaussianNB()
gaussnb.fit(x_train,y_train)
#print(gaussnb)
y_pred=gaussnb.predict(x_test)
print("accuracy of gaussina model: ",accuracy_score(y_test,y_pred))
