import numpy as np
import matplotlib.pyplot as plt
 
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x - n*m_y*m_x)
    SS_xx = np.sum(x*x - n*m_x*m_x)
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return(b_0, b_1)
 
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 300)
 
    # predicted response vector
    y_pred = b[0] + b[1]*x
 
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
 
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
 
    # function to show plot
    plt.show()


def predict(b0,b1,x):
    y=b0+b1*x
    return y

def main():
    # observations
    x = np.array([0, 1, 3, 10, 4, 11, 15, 17, 15, 19,21,16,27,23,20,25,18,17,13,18,27,12,2,3,4,5,13,5])
    y = np.array([1, 3, 2, 5, 7, 11,7 , 9, 10, 12,6,7,8,5,13,15,2,3,4,5,7,7,8,6,5,4,4,7])
    
    #x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15])
    #y = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
 
    # estimating coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients:\nb_0 = {}  \
          \nb_1 = {}".format(b[0], b[1]))
    
    xi=int(input("enter the x value to predict: "))
    pred=predict(b[0],b[1],xi)
    print("the prdictected value is: ",pred)
    
 
    # plotting regression line
    plot_regression_line(x, y, b)
 
if __name__ == "__main__":
    main()