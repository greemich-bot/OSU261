from static_array import StaticArray

class DynamicArrayException(Exception):

    """

    Custom exception class to be used by Dynamic Array

    DO NOT CHANGE THIS CLASS IN ANY WAY

    """

    pass

class DynamicArray: 
    def __init__(self, start_array=None): 
        """ 
        Initialize new dynamic array 
        DO NOT CHANGE THIS METHOD IN ANY WAY 
        """ 
        self.size = 0 
        self.capacity = 4 
        self.data = StaticArray(self.capacity)

        # populate dynamic array with initial values (if provided) 
        # before using this feature, implement append() method 
        if start_array is not None: 
            for value in start_array: 
                self.append(value) 
                

    def dynArrayAddAt(self, index: int, value: object) -> None: 
        
        if index < 0 or index > self.size: 
            raise DynamicArrayException("invalid index") 

        if self.size == self.capacity: 
            newcapacity = self.capacity * 2 
            newdata = DynamicArray()  
            for i in range(self.size): 
                newdata[i] = self.data[i] 
            self.data = newdata 
            self.capacity = newcapacity

        for i in range(self.size, index, -1): 
            self.data[i] = self.data[i - 1] 

        self.data[index] = value 
        self.size += 1



dynArray = DynamicArray()
dynArray.dynArrayAddAt(0, 1)
dynArray.dynArrayAddAt(1, 2)
dynArray.dynArrayAddAt(1, 3)


print(dynArray.data[0])
print(dynArray.data[1])
print(dynArray.data[2])
print (dynArray.size)
print (dynArray.capacity)
print(dynArray)
