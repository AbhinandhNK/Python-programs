s=input("Enter the list of words(in comma seperated form)")
list1= s.split(",")
print(list1)
word=list1[0]
for i in list1:
    if len(word)< len(i):
        word=i
print("Length of Longest Word : ",len(word))