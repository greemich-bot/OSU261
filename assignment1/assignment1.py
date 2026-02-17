# Name: Michael Green
# OSU Email: Greemich@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:1
# Due Date:January 27th, 2026
# Description: Implementation of various functions using StaticArray to practice
#              using python. Goal is to complete all 10 problems using only
#              the StaticArray data structure and O(n) time complexity where possible.


import random
from static_array import *




#-------------------- HelperFunctions ------------------------------------


#NA



# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------
#O(n)

def min_max(arr: StaticArray) -> tuple[int, int]:
#Initialize min and max to first element   
    min_val = arr[0]
    max_val = arr[0]
#Iterate through array to find min and max    
    for i in range(arr.length()):
        value = arr[i]
#Compare current value to min and max and update accordingly        
        if value < min_val:
            min_val = value
        elif value > max_val:
            max_val = value
    return (min_val, max_val)   
    


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------
#O(n)

def fizz_buzz(arr: StaticArray) -> StaticArray:
    newArr = StaticArray(arr.length())
    for i in range(arr.length()):
        value = arr[i]
        #first check if divisible by both 3 and 5 to avoid missing those cases
        if value % 3 == 0 and value % 5 == 0:
            newArr[i] = "fizzbuzz"
            #check if divisible by 3 or 5 separately
        elif value % 3 == 0:
            newArr[i] = "fizz"
        elif value % 5 == 0:
            newArr[i] = "buzz"
        else:
            newArr[i] = value
    return newArr   
    pass


# ------------------- PROBLEM 3 - REVERSE -----------------------------------
#O(n)

def reverse(arr: StaticArray) -> None:
   
   left = 0
   right = arr.length() - 1
   #swap values from start and end moving towards center
   while left < right:
       temp = arr[left]
       arr[left] = arr[right]
       arr[right] = temp
       left += 1
       right -= 1   
    
    


# ------------------- PROBLEM 4 - ROTATE ------------------------------------
#O(n)

def rotate(arr: StaticArray, steps: int) -> StaticArray:
   #create new static array to store rotated values
   result = StaticArray(arr.length())
#account for full rotations(amout of steps greater than array length)
   steps = steps % arr.length()
   #if we dont rotate, just copy the array
   if steps == 0:
         for i in range(arr.length()):
              result[i] = arr[i]
    #if we rotate to the right, 
   elif steps>0:
       #shift the front subset of values to the right by steps
       for i in range(result.length()-steps):
           result[i+steps]= arr[i]
         #move the end subset of values to the front   
       for i in range(steps):
           result[i]=arr[arr.length()-steps+i]
#if we rotate to to the left move the front subset to the back and the back subset to the front
   elif steps<0:
       steps=abs(steps)
       for i in range(steps, result.length()):
           result[i-steps]=arr[i]
       for i in range (steps):
           result[result.length()-steps+i]=arr[i]
   return result






# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------
#find the distance between start and end to determine length of new array
#create new static array of that length
#populate new array with values from start to end or end to start depending on which is larger

#O(n)
def sa_range(start: int, end: int) -> StaticArray:
    length = abs(end - start) + 1
    result = StaticArray(length)
    if start <= end:
        for i in range(length):
            result[i] = start + i
    else:
        for i in range(length):
            result[i] = start - i
    return result


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

#O(n)
def is_sorted(arr: StaticArray) -> int:
    #Initialize counters and result variable
    result = 0
    ascending = 0
    descending = 0

    
    #Iterate through array and compare adjacent values, increment counters accordingly
    for i in range(arr.length() - 1):
        if arr[i] < arr[i + 1]:
            ascending += 1
        elif arr[i] > arr[i + 1]:
            descending += 1 
    #If one of the counters matches the length minus one, the array is sorted in that order else it is unsorted
    if ascending == arr.length() - 1:
        result = 1
    elif descending == arr.length() - 1:
        result = -1
    else:
        result = 0

    return result


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------
#O(n)

def find_mode(arr: StaticArray) -> tuple[object, int]:
    #Initialize variables to track mode and frequency
    mode = arr[0]
    max_count = 1
    current_count = 1

    #Iterate through array and count frequency of each value
    for i in range(1, arr.length()):
        if arr[i] == arr[i - 1]:
            current_count += 1
        else:
            current_count = 1
        #Update mode and max_count if current_count exceeds max_count
        if current_count > max_count:
            max_count = current_count
            mode = arr[i]

    return (mode, max_count)


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

#O(n)
def remove_duplicates(arr: StaticArray) -> StaticArray:
    
    #Create new static array to store unique values
    unique_count = 1
    for i in range(1, arr.length()):
        if arr[i] != arr[i - 1]:
            unique_count += 1   
    result = StaticArray(unique_count)

    #First element is always unique so set it and start index at 1 to check element before current
    result[0] = arr[0]
    index = 1    
    #Iterate through array and add unique values to new array
    for i in range(1, arr.length()):
        if arr[i] != arr[i - 1]:
            result[index] = arr[i]
            index += 1  
    return result
# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:
    #Setup
    n = arr.length()

    #Check 
    if n == 0:
        return StaticArray(0)

    min_val, max_val = min_max(arr)
    range_of_values = max_val - min_val + 1
    
    #Initialize count array to 0
    count = StaticArray(range_of_values)
    for i in range(range_of_values):
        count[i] = 0
    
    #Frequency Count
    #Subtract min_val to ensure the smallest number maps to the first position
    for i in range(n):
        val = arr[i]
        count[val - min_val] += 1
        
    result = StaticArray(n)
    result_idx = 0
    
    #Iterate through the count array
    for i in range(range_of_values):
        # Retrieve how many times this specific number appeared
        frequency = count[i]
        
        # Place it into the result array 'frequency' times
        for _ in range(frequency):
            result[result_idx] = i + min_val
            result_idx += 1

    #It's backward so reverse it     
    reverse(result)
    return(result)

    

# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------


def sorted_squares(arr: StaticArray) -> StaticArray:
    
    n=arr.length()
    result = StaticArray(arr.length())
    #Setup L and R counter
    left=0
    right=n-1
    #Compare L and R, incremenr and decrement appropriately
    for i in range(n):
        if abs(arr[left])>abs(arr[right]):
            result[i]=arr[left]**2
            left+=1
        else:
            result[i]=arr[right]**2
            right-=1

    reverse(result)  
    return result

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result is not None and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(f"Before: {arr}")
        result = count_sort(arr)
        print(f"After : {result}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-10 ** 9, 10 ** 9 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
