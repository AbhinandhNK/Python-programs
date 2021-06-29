s=input("Enter the string ")

if s.endswith("ing"):
    s=s+"ly"
else:
    s=s+"ing"
print("New String : ",s) 