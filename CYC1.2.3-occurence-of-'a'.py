list1=['abhinandhan','abin','bibin','john']
count=0
for i in list1:
    for j in i:
        if(j=='a'):
            count=count+1
print("The number of a occurences of a=",count)
