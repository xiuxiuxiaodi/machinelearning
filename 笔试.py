#-*-encoding=utf-8-*-
import pandas as pd
import numpy as np
billDf=pd.read_csv(u'C:/Users/鲍明广/Desktop/笔试题/bill.csv')
print billDf.dtypes
print billDf[billDf.VIPFLAG==0].head(5)
print billDf[billDf.USER_STATE<>0].count()

callDf=pd.read_csv(u'C:/Users/鲍明广/Desktop/笔试题/call_detail.csv')

print callDf.drop_duplicates(subset='ID').count()

bill_callDF=billDf.merge(callDf.drop_duplicates('ID'),how='left',on='ID')


print billDf.groupby(['IN_NET','USER_STATE']).agg({'PAY_SUM':np.mean,'TRAFFIC_SUM':sum})

bill_callDF[['IMSI','IMEI']].fillna(0).to_csv('h:/ok.csv')