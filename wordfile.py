import random
choice=['a','b','c','d','e','f','g','h','\t','\t','\t','\n']
i=0
random.choice(choice)
with open('h:/wordcount.txt','wb+') as file:
    while i<100000000:
        a=random.choice(choice)
        file.write(a)
        i+=1
file.close()

