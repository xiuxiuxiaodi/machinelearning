#encoding=utf-8
import numpy as np
import re
import pandas as pd
import json
from compiler.ast import flatten
string=open('G:\desktop\pingtec\changan.txt').read()
import pandas
pattern=re.compile(r'({.*})')
data=pattern.findall(string)
data2=[json.loads(i)['mobileTelemetry'] for i in data]
d1=flatten(data2)
#print d1[0:2]
#d=pd.DataFrame(d1)
#print d.shape
#d2=reduce(lambda x,y:x+y,data2)
#d3=pd.DataFrame(d2)
#print d3
#print len(data)
#print json.loads(data[0])
df=pd.DataFrame(json.loads(data[0])['mobileTelemetry'])
print df
for i in range(1,len(data)):

    df_append=pd.DataFrame(json.loads(data[i])['mobileTelemetry'])

    df=df.append(df_append,ignore_index=True)

df.to_csv("h:/gps.csv")





