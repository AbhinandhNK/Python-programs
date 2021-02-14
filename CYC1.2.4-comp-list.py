list1=[5,3,4,5]
list2=[2,3,4,5]
if(len(list1)==len(list2)):
    print("Lists lengths are equal")
else:
    print("Lists lengths are unequal")
if(sum(list1)==sum(list2)):
    print("Lists sum are equal")
else:
    print("Lists sum are unequal")
print("The values occure in both")
print(set(list1)&set(list2))