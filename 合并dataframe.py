# -*- encoding:utf-8 -*-
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3, 4), columns=list('abcd'))
print df
index1 = range(3, 5)
df1 = pd.DataFrame(np.random.randn(2, 4), columns=list('abcd'))
print df1
df2 = df.append(df1)  # df1中的2行数据会加到df中，且新产生的df的各行的索引就是原来数据的索引
print df2
df3 = df.append(df1, ignore_index=True)  # df1中的2行数据会加到df中，且新产生的df的索引会重新自动建立
print df3