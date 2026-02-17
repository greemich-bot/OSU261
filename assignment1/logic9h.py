import random
from static_array import *
from assignment1 import *

testArr = StaticArray(10);

testArr[0] = 0
testArr[1] = 1
testArr[2] = -4           
testArr[3] = 3
testArr[4] = 2
testArr[5] = 4
testArr[6] = 1
testArr[7] = 5
testArr[8] = 8
testArr[9] = 3
#-------------------- HelperFunctions ------------------------------------
def cs(arr: StaticArray) -> StaticArray:
#create a container, find the min max and range
    result=StaticArray(arr.length())
    min=min_max(arr)[0]
    max=min_max(arr)[1]  
    rangeOfValues = max + 1
#create a container to store counts of each occurence then initialize ea to 0
    count=StaticArray(rangeOfValues)  
    for i in range(count.length()):
        count[i] = 0
#populate count array with occurences
    for i in range (arr.length()):
        index=arr[i]
        count[index]+=1
#populate result array based on counts
    for i in range(count.length()):
        for j in range(abs(count[i])):
            resultIndex=0
            for k in range(i):
                resultIndex+=count[k]
            result[resultIndex + j]=i

    return result

# ------------------- SplitandMerge --------------------------------




posArrSize=0
negArrSize=0
for i in range(testArr.length()):
    if testArr[i]>=0:
        posArrSize+=1
    if testArr[i]<0:
        negArrSize+=1


posArr=StaticArray(posArrSize)

negArr=StaticArray(negArrSize)

p=0
n=0

for i in range(testArr.length()):
    
    if testArr[i]>=0:
        posArr[p]=testArr[i]
        p+=1
    if testArr[i]<0:
        negArr[n]=testArr[i]
        n+=1


#print('posArr before sort:', posArr)


sortedPos=cs(posArr)
reverse(sortedPos)
print('posArr after sort:', sortedPos)

#print('negArr before sort:', negArr)

for i in range(negArr.length()):
    negArr[i]=abs(negArr[i])

#print('negArr after abs:', negArr)

sortedNeg=cs(negArr)

#print("sorted neg: ", sortedNeg)

for i in range (sortedNeg.length()):
    sortedNeg[i]= sortedNeg[i]*-1

print('neg sortedNeg: ', sortedNeg)


completeSize=sortedPos.length()+sortedNeg.length()

result=StaticArray(completeSize)

for i in range (sortedPos.length()):
    result[i]=sortedPos[i]

for i in range (sortedNeg.length()):
    result[i+sortedPos.length()]=sortedNeg[i]

print(result)








