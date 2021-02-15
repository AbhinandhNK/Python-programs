string1=input('Enter the string:')
newstr=' '
for i in range(0,len(string1)+1):
    if(i==0):
        newstr=string1[-1]
    elif(i==len(string1)):
        newstr=newstr+string1[0]
    else:
        newstr=newstr+string1[i]
print(newstr)