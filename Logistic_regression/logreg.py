import csv
import random
import numpy as np
import matplotlib.pyplot as plt
alpha = 0.015               # learning rate
iterations = 15000          # No. of iterations

def gradient_descent(theta,X,Y):
    xTrans = np.transpose(X)
    for i in range(0,iterations):
        hypothesis = 1.0 / (1.0 + np.exp((-1) *np.dot(X, theta)))
        loss = hypothesis - Y
        gradient = np.dot(xTrans,loss)/(len(X))
        theta = theta - (alpha * gradient)
    return theta


def main():
    X = []
    with open("logreg.csv",'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for i in range(1,len(dataset)):
            X.append([1.0,float(dataset[i][1]),float(dataset[i][2]),float(dataset[i][3])])   #importing dataset
    random.shuffle(X)
    train_x = []
    train_y = []
    for i in range(len(X)):
        train_x.append([X[i][0],X[i][1],X[i][2]])            #feature dataset
        train_y.append(X[i][3])                              #Output dataset

    theta = [0.0,0.0,0.0]      #as there are only 2 parameters in this case
    theta = gradient_descent(theta,train_x,train_y)
    pred = []
    for i in range(len(train_x)):
        t = 1.0 / (1.0 + np.exp((-1) *np.dot(train_x[i], theta)))
        if(t>=0.5):
            pred.append(1.0)
        else:
            pred.append(0.0)
    count =0.0
    for i in range(len(pred)):
        if(pred[i]==train_y[i]):    
            count += 1                  #counting correct output
    print("Accuracy is:{}".format(float(count/len(pred))*100))    # accuracy = correct_output/total output
main()
