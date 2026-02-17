import random
from static_array import *
from assignment1 import *

testArr = StaticArray(10);

testArr[0] = 1
testArr[1] = 2
testArr[2] = 3              
testArr[3] = 4
testArr[4] = 5
testArr[5] = 6
testArr[6] = 0
testArr[7] = 0
testArr[8] = -4
testArr[9] = -4

 #initialize min and max to first element   

result=StaticArray(testArr.length())

negativeSize=abs(min_max(testArr)[0])
positiveSize=min_max(testArr)[1]

negativeArr=StaticArray(negativeSize)
for i in range(negativeSize):
        negativeArr[i]=0
positiveArr=StaticArray(positiveSize)
for i in range(positiveSize):
        positiveArr[i]=0

countArr=StaticArray(testArr.length())
for i in range(testArr.length()):
    countArr[i]=0


for i in range(countArr.length()):
    if testArr[i]<0:
        negativeArr[abs(testArr[i])-1]+=1
    elif testArr[i]>0:
        positiveArr[testArr[i]-1]+=1

reverse(negativeArr)

for i in range(negativeArr.length()):
    countArr[i]=negativeArr[i]
for i in range(positiveArr.length()):
    countArr[i+negativeArr.length()]=positiveArr[i]

for i in range(countArr.length()):
    if countArr[i]>0:
        n=countArr[i]
        value=i-4
        while n>0:
             result[i]=value
             n-=1
             i+=1
             

    
    

print(negativeArr)
print(positiveArr)
print(countArr)
print(testArr)
print(result)



