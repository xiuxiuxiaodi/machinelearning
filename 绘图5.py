a=[1,2,3,4,5]
b=list(range(1,70,10))
c=list("ABCDEF")

d=sorted(zip(a,b,c))

with open('some.csv','w') as f:
    writer=csv.writer(f,lineterminator='\n')
    writer.writerow(['id','score','rank'])
    writer.writerows(d)

with open('some.csv','r') as f:
    reader=csv.reader(f)
    your_list=list(reader)

print your_list