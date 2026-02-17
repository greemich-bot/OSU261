import random
from static_array import *
from assignment1 import *

testArr = StaticArray(10);

testArr[0] = 1
testArr[1] = 3
testArr[2] = 1         
testArr[3] = 3
testArr[4] = 4
testArr[5] = -1
testArr[6] = 0
testArr[7] = 7
testArr[8] = 1
testArr[9] = 2
#-------------------- HelperFunctions ------------------------------------

def min_max(arr: StaticArray) -> tuple[int, int]:
#initialize min and max to first element   
    min_val = arr[0]
    max_val = arr[0]
#iterate through array to find min and max    
    for i in range(arr.length()):
        value = arr[i]
#compare current value to min and max and update accordingly        
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return (min_val, max_val) 



def csl(arr: StaticArray) -> StaticArray:
    # 1. Setup metadata
    n = arr.length()
    if n == 0:
        return StaticArray(0)

    # Assuming min_max is a helper you've already defined
    min_val, max_val = min_max(arr)
    range_of_values = max_val - min_val + 1
    
    # 2. Initialize count array to 0
    count = StaticArray(range_of_values)
    for i in range(range_of_values):
        count[i] = 0
    
    # 3. Frequency Count
    # We subtract min_val to ensure the smallest number maps to index 0
    for i in range(n):
        val = arr[i]
        count[val - min_val] += 1
        
    # 4. Reconstruct Result (Linear Time)
    result = StaticArray(n)
    result_idx = 0
    
    # Iterate through the count array
    for i in range(range_of_values):
        # Retrieve how many times this specific number appeared
        frequency = count[i]
        
        # Place it into the result array 'frequency' times
        for _ in range(frequency):
            result[result_idx] = i + min_val
            result_idx += 1
            
    return result


ans=csl(testArr)
reverse (ans)
print (ans)

    


    










