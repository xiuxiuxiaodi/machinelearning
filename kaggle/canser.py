%matplotlib inline
import os
import numpy as np
import pandas as pd
import glob
import hashlib
from scipy.misc import imresize
import matplotlib.pyplot as plt
import seaborn as sns

hashes = {}
labels = {} #map fname -> label

print('computing md5 of training data:')
for base_dir in ["additional", "train"]:
    print(base_dir)
    for fname in glob.glob("../input/{}/**/*.jpg".format(base_dir)):
        labels[fname] = fname.split('/')[-2]
        h = hashlib.md5(open(fname, 'rb').read()).digest()
        if h in hashes:
            hashes[h].append(fname)
        else:
            hashes[h] = [fname]
print(len(hashes))

repeated=sum(1 for k,v in hashes.items() if len(v)>1)
print 'files appearing more than once in train + additonal:'
print repeated

print 'identical files with different labels:'
for k,v in hashes.items():
    if len(v)>1:
        c=set([labels[x] for x in v])
        if len(c)>1:
            print v,c


#find the test files alse present in traning data
leaks=[]
for fname in glob.glob('../input/test/*.jpg'):
    h=hashlib.md5(open(fname,'rb')).digest()
    if h in hashes:
        leaks.append((fname,hashes[h]))


