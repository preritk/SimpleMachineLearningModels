import csv
import matplotlib.pyplot as plt

def estimate_coef(x=[],y=[]):
    m1,m2 = 0.0,0.0
    for i in range(len(x)):
        m1 += x[i]
    m1 = m1/len(x)
    for i in range(len(y)):
        m2 += y[i]
    m2 = m2/len(y)
    p,q = 0.0,0.0
    for i in range(len(x)):
        p += x[i]*y[i]-len(x)*m1*m2
        q += x[i]*x[i]- len(x)*m1*m1
    b_1 = p/q
    b_0 = m2 - b_1*m1
    return (b_0,b_1)

def plot_function(x=[],y=[],b=[]):
    plt.scatter(x,y,color = "r",marker = "o",s=30 )
    predictions = []
    for i in range(len(x)):
        predictions.append(b[0]+(b[1]*x[i]))
    plt.plot(x,predictions,color = "g")
    plt.xlabel('Square feet')
    plt.ylabel('Price')
    plt.show()

def main():
    x = []
    y = []
    with open("linear.csv","r") as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for i in range(len(dataset)):
            x.append(float(dataset[i][0]))
            y.append(float(dataset[i][1]))

    b = estimate_coef(x,y)
    print("Estimated coefficients are : {} and {}".format(b[0],b[1]))
    plot_function(x,y,b)
main()
