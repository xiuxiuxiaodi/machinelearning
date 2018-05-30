#encoding=utf-8
#算法
#插入排序
import numpy as np
import time
def InsertSort(list):
    for i in range(1,len(list)):
        key=list[i]
        j=i-1
        while j>=0 and list[j]>key:
            list[j+1]=list[j]
            j=j-1
        list[j+1]=key
    return list
s=np.random.randint(1,10000,10000)
c1=time.time()
print "time1 start at ",c1
a=InsertSort(s)
c2=time.time()
print "time1 end at",c2,",consume ",c2-c1," seconds!"
c4=time.time()
print "time2 start at ",c4
b=s.sort()
c3=time.time()
print "time2 end at",c3," seconds",' consume',float(c3-c4),' seconds'
print c3-c4
#print "system is ",(c2-c1)/float(c3-c4),"倍"
print a
//*[@id="subject_list"]/div[2]/span[4]/a