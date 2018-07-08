# Logistic Regression Classification
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.metrics import confusion_matrix
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2)
num_folds = 10
kfold = KFold(n_splits=10, random_state=7)
model = LogisticRegression().fit(x_train,y_train)
y_predict=model.predict(x_test)

cm=confusion_matrix(y_test,y_predict)
#print(y_predict)
#print(cm)
results = cross_val_score(model, X, Y, cv=kfold)
print(results)
print(results.mean())
