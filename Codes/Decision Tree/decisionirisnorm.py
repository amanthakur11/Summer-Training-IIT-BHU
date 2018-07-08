import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
 
# Function importing Dataset
def importdata():
    balance_data = pd.read_csv("iris.csv")
     
    # Printing the dataswet shape
    print ("Dataset Lenght: ", len(balance_data))
    print ("Dataset Shape: ", balance_data.shape)
     
    # Printing the dataset obseravtions
    print ("Dataset: ",balance_data.head())
    return balance_data
 

# Convert string column to float
def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column])
        
# Function to split the dataset
def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])-1):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax

# Rescale dataset columns to the range 0-1
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)-1):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])    


def splitdataset(balance_data):
 
    # Seperating the target variable
    X = balance_data[:, 0:4]
    Y = balance_data[:, 4]
                            
 
    # Spliting the dataset into train and test
    X_train, X_test, y_train, y_test = train_test_split( 
    X, Y, test_size = 0.3, random_state = 100)
     
    return X, Y, X_train, X_test, y_train, y_test
     
# Function to perform training with giniIndex.
def train_using_gini(X_train, X_test, y_train):
 
    # Creating the classifier object
    clf_gini = DecisionTreeClassifier(criterion = "gini",
            random_state = 100,max_depth=3, min_samples_leaf=5)
 
    # Performing training
    clf_gini.fit(X_train, y_train)
    return clf_gini
     
# Function to perform training with entropy.
def tarin_using_entropy(X_train, X_test, y_train):
 
    # Decision tree with entropy
    clf_entropy = DecisionTreeClassifier(
            criterion = "entropy", random_state = 100,
            max_depth = 3, min_samples_leaf = 5)
 
    # Performing training
    clf_entropy.fit(X_train, y_train)
    return clf_entropy
 
 
# Function to make predictions
def prediction(X_test, clf_object):
 
    # Predicton on test with giniIndex
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred
     
# Function to calculate accuracy
def cal_accuracy(y_test, y_pred):
     
    print("Confusion Matrix: ",
        confusion_matrix(y_test, y_pred))
     
    print ("Accuracy : ",
    accuracy_score(y_test,y_pred)*100)
     
    print("Report : ",
    classification_report(y_test, y_pred))
 
# Driver code
def main():
     
    # Building Phase
    
    names=['sepal.length','sepal.width','petal.length','petal.width']
    dataset=pd.read_csv("iris.csv").values
    
    for i in range(len(dataset[0])-1):
        str_column_to_float(dataset, i)
    # normalize
    minmax = dataset_minmax(dataset)
    normalize_dataset(dataset, minmax)
    x=dataset[:,:4]
    y=dataset[:,4]
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
    clf_gini = train_using_gini(x_train, x_test, y_train)
    clf_entropy = tarin_using_entropy(x_train, x_test, y_train)
     
    # Operational Phase
    print("Results Using Gini Index:")
     
    # Prediction using gini
    y_pred_gini = prediction(x_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)
     
    print("Results Using Entropy:")
    # Prediction using entropy
    y_pred_entropy = prediction(x_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy)
    

    from sklearn.externals.six import StringIO  
    from sklearn.tree import export_graphviz
    import pydotplus

    dot_data = StringIO()

    export_graphviz(clf_gini, out_file=dot_data,feature_names=names,filled=True, rounded=True,special_characters=True)

    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
    graph.write_png('analysis_result1.png') 
# Calling main function
if __name__=="__main__":
    main()