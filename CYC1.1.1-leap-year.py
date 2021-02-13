lb = int(input('Enter the lowerbound year:'))
ub=int(input('Enter the upperbound year:'))
print("*******The Leap years*********")
for i in range (lb,ub+1,1):
    if(i%4==0 or i%100!=0 and i%400==0):
        print(i)