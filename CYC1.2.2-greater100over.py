n=int(input("Enter the number of elements:"))
list1=[]
for i in range(0,n,1):
    m=int(input('Enter the elemet:'))
    if(m>100):
        list1.append("over")
    else:
        list1.append(i)
print(list1)
