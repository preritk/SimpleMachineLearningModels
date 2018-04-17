import csv
import math
import operator

def getEucledian(instance1=[],instance2=[]):
    distance = 0.0
    for x in range(4):
        a = float(instance1[x])
        b = float(instance2[x])
        c = a-b
        distance += pow(c,2)
    return math.sqrt(distance)

def getneighbors(instance1=[],training=[]):
    distances = []
    for x in range(0,len(training)):
        mydistance = getEucledian(instance1,training[x])
        distances.append([training[x],mydistance])
    distances.sort(key = operator.itemgetter(1))
    k=5
    a,b,c=0,0,0
    for x in range(k):
        distances.append(distances[k][0])
    for x in range(k):
        if distances[x][0][4]=="setosa":
            a+=1
        elif distances[x][0][4]=="versicolor":
            b+=1
        else:
            c+=1
    max  = a
    if(b>max):
        max =b
    if(c>max):
        max = c
    if max == a:
        return "setosa"
    elif max == b:
        return "versicolor"
    else:
        return "virginica"

def getaccuracy(test=[],predictions=[]):
    p = 0
    for x in range(len(test)):
        if(test[x][4]==predictions[x]):
            p +=1
    accuracy = p/len(test)
    return accuracy
def main():
    with open("iris.csv", 'r') as csvfile:

        lines = csv.reader(csvfile)

        dataset = list(lines)

        for x in range(len(dataset)):

            for y in range(4):

                dataset[x][y] = float(dataset[x][y])
    predictions = []
    split = input("Enter the split ratio between 0 and 1: ")
    split = float(split)
    train = dataset[0:int(len(dataset)*split)]
    test = dataset[:int(len(dataset)*split)]
    for i in range(0,len(test)):
        type = getneighbors(test[i],train)
        print("Test case is: {} ; Prediction : {}".format(test[i],type))
        predictions.append(type)

    percentaccu =  getaccuracy(test,predictions)*100
    print(percentaccu)
main()
