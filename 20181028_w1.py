#Q2.
sum=0
for i in range(1,10001):
     if i%3==0:
          sum += i
print(sum)
#Q3.
num=(int)(input("number of rows?"))
for i in range(num,0,-1):
     for j in range(0, i):
          print("*", end='')
     print(" ")
