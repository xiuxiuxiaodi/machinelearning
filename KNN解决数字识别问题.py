import pandas as pd
from pandas import *
import numpy as np

def loadTrainData():
    l=[]
    with open("train.csv") as file:
        lines=csv.reader(file)
        for line in lines:
            l.append(line)
        l.remove(0)
        l=np.array(l)
        label=l[:,0]
        data=l[:,1:]
        return normalizing(toInt(data)),toInt(label)

def toInt(array):
    array=mat(array)
    m,n=shape(array)
    newArray=zeros((m,n))
    for i in xrange(m):
        for j in xrange(n):
            newArray[i,j]=int(array[i,j])
    return newArray

def nomalizing(array):
    m,n=shape(array)
    for i in xrange(m):
        for j in xrange(n):
            if array[i,j]!=0:
                array[i,j]=1
    return array

def loadTestData():
    l=[]
    with open('test.csv') as file:
        lines=csv.reader(file)
        for line in lines:
            l.append(line)
        l.remove(l[0])
        data=array(l)
        return nomalizing(toInt(data))

def loadTestResult():
    l=[]
    with open("")