#-*-encoding=utf-8-*-
import pandas as pd
from IPython.display import display
import numpy as np
import sklearn01

df=pd.DataFrame({"name":["David",'Tom','Jack','Allen'],'type':['e','B','C','B'],'number':[1234,2233,2244,2355]})
def judge(x):
    if x.name!="" and x.type in ["A",'B','C','D'] and len(str(x.number))==4:
        return True
    else:
        return False

df['is_valid']=df.apply(judge,axis=1)
print df