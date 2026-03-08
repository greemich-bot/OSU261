# Name: Michael Green
# OSU Email: greemich@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:6 separate chaining hash map implementation
# Due Date: 3/12/26
# Description: Implementation of hashmap that prevents collisions using chaining.
# Buckets are implemented using dynamic array class (provided), and each bucket contains a linked list (also provided) to store k/v pairs. 
# Dynamic array and link list classes are only accessed using thier provided methods, however SLNodes in the linked list can be accessed directly.



from a6_include import (DynamicArray, LinkedList,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self,
                 capacity: int = 11,
                 function: callable = hash_function_1) -> None:
        """
        Initialize new HashMap that uses
        separate chaining for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        self._hash_function = function
        self._size = 0

    def __str__(self) -> str:
        """
        Override string method to provide more readable output
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self._buckets.length()):
            out += str(i) + ': ' + str(self._buckets[i]) + '\n'
        return out

    def _next_prime(self, capacity: int) -> int:
        """
        Increment from given number and the find the closest prime number
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity % 2 == 0:
            capacity += 1

        while not self._is_prime(capacity):
            capacity += 2

        return capacity

    @staticmethod
    def _is_prime(capacity: int) -> bool:
        """
        Determine if given integer is a prime number and return boolean
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if capacity == 2 or capacity == 3:
            return True

        if capacity == 1 or capacity % 2 == 0:
            return False

        factor = 3
        while factor ** 2 <= capacity:
            if capacity % factor == 0:
                return False
            factor += 2

        return True

    def get_size(self) -> int:
        """
        Return size of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return capacity of map
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    # ------------------------------------------------------------------ #
    

    def put(self, key: str, value: object) -> None:
        """
        updatesor adds k/v pair in the hashmap. if a key exists the value is updated, if not a new k/v is added
        when called the method checks the load factor and resizes the table if >= 1.0.
        :param key: the key associated with the value to be added or updated
        :param value: the value to be added or updated
        """
        # check for resize first
        if self.table_load() >= 1.0:
            # double capacity
            self.resize_table(self._capacity * 2)
        
        # compute the element's bucket
        index = self._hash_function(key) % self._capacity
        # get the linked list at that bucket
        bucket = self._buckets[index]
        # using linked list methods, if key already exists, update value or insert new k/v pair and update size
        node = bucket.contains(key)
        if node:
            # SLNode can be accessed directly.
            node.value = value
        else:
            # add kv pair to the LL using linked list insert() method and update size
            bucket.insert(key, value)
            self._size += 1
            


    def resize_table(self, new_capacity: int) -> None:
        """
        changes the capacity of the underlying table, rehashing all table links to the new table
        is called by put when the LF is >= 1.0 and also calls put to rehash all k/v pairs to the new table
        :param new_capacity: the new capacity of the table
        """
        # check if new capacity is not less than 1, if so do nothing
        if new_capacity < 1:
            return
        # make sure new capacity is a prime number
        if not self._is_prime(new_capacity):
            # if not prime, find the next prime number and set new capacity to that
            new_capacity = self._next_prime(new_capacity)
        #store original capacity and buckets for rehashing
        og_capacity = self._capacity
        og_buckets = self._buckets
        # set new capacity and create new buckets
        self._capacity = new_capacity
        self._buckets = DynamicArray()
        self._size = 0

        # fill new buckets with empty linked lists like in init
        for _ in range(self._capacity):
            self._buckets.append(LinkedList())

        # rehash all k/v pairs from old buckets to new buckets
        for i in range(og_capacity):
            # for each bucket, get the linked list and traverse it
            bucket = og_buckets[i]
            for node in bucket:
                # indirect recursion allowed for put and resize only
                self.put(node.key, node.value)




        

    def table_load(self) -> float:
        """
        current load factor of the table.
        called by put to see if resize is needed.
        adapted from the formula in the Exploration
        """
        # load factor = n / m
        loadFactor = self.get_size() / self.get_capacity()
        return loadFactor
        

    def empty_buckets(self) -> int:
        """
        counts the number of empty buckets in the table.
        """
        #initialize counter
        counter = 0
        #loop through all buckets 
        for i in range(self._capacity):
            # use linked list length() to check if bucket is empty, if so increment counter
            if self._buckets[i].length() == 0:
                counter += 1
        return counter

    def get(self, key: str) -> object:
        """
        gets the value associated with the given key in the hashmap or None if key is not found.
        :param key: the key to get the value for
        """
        # compute the element's bucket
        index = self._hash_function(key) % self._capacity
        # get the linked list at that bucket
        bucket = self._buckets[index]
        # use linked list contains() to check if key exists
        node = bucket.contains(key)
        if node:
            # SLNode can be accessed directly.
            return node.value
        return None

    def contains_key(self, key: str) -> bool:
        """
        t if the given key is in the hashmap, false otherwise.
        :param key: the key to check for in the hashmap
        """
        # compute the element's bucket
        index = self._hash_function(key) % self._capacity
        # get the linked list at that bucket
        bucket = self._buckets[index]
        # use linked list contains() to check if key exists
        node = bucket.contains(key)
        if node:
            return True
        return False

    def remove(self, key: str) -> None:
        """
        removes the given key and its value from the hashmap
        when key is not found the method does nothing.
        :param key: the key to be removed from the hashmap
        """
        # compute the element's bucket
        index = self._hash_function(key) % self._capacity
        # get the linked list at that bucket
        bucket = self._buckets[index]
        # use linked list remove() to remove key if it exists, if removed update size
        node = bucket.contains(key)
        if node:
            bucket.remove(key)
            self._size -= 1


    def get_keys_and_values(self) -> DynamicArray:
        """
        returns a DA of tuples (key, value) stored in the hashmap.
        """
        # initialize storage
        kvArr = DynamicArray()
        # loop through all buckets 
        for i in range(self._capacity):
            bucket = self._buckets[i]
            # traverse the linked lists in each bucket 
            for node in bucket:
                # use DA append() to add a tuple of the node's key and value to the storage
                kvArr.append((node.key, node.value))
        return kvArr

    def clear(self) -> None:
        """
        O(N) complexity
        clears the contents of the hashmap without changing the underlying hash table capacity.

        """
        # set each bucket to a new empty linked list
        for i in range(self._capacity):
            self._buckets[i] = LinkedList()
        # reset size to 0 but keep the capacity unchanged
        self._size = 0


def find_mode(da: DynamicArray) -> tuple[DynamicArray, int]:
    """
    receives a DA (unsorted) and returns a tuple containing a DA of modes values and an integer representing the highest frequency.
    """
    # if you'd like to use a hash map,
    # use this instance of your Separate Chaining HashMap
    map = HashMap()

    # initialize storage and a counter
    modes = DynamicArray()
    frequency = 0

    # loop through the input da 
    for i in range(da.length()):
        # each unique element becomes a key, the value associated with the key is the number of times it occures in the input.
        key = da[i]
        occurrences = map.get(key)
        # if the key is in the map
        if map.contains_key(key):
            # increment its occurence count by 1
            occurrences += 1
            # update the key's value with put to the new occurence count
            map.put(key, occurrences)
        # if the key is not in the map, add it and initialize its occurence count to 1
        else:
            occurrences = 1
            map.put(key, occurrences)
        # update the frequency if the value(occurrences) is higher than the current frequency
        if occurrences > frequency:
            frequency = occurrences

    # use method to get a da of kv pairs in the format (input element, occurrence count).
    kvArr = map.get_keys_and_values()
    # loop through the kv pairs. 
    for i in range(kvArr.length()):
        # if the second element = fq, append the first element to the modes DA.
        if kvArr.get_at_index(i)[1] == frequency:
            modes.append(kvArr.get_at_index(i)[0])

    return (modes, frequency)


# ------------------- BASIC TESTING ---------------------------------------- #


if __name__ == "__main__":

    print('\nPDF - put example 1')
    print('-------------------')
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print('\nPDF - put example 2')
    print('-------------------')
    m = HashMap(41, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print('\nPDF - resize example 1')
    print('----------------------')
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.get_size(), m.get_capacity(), m.get('key1'), m.contains_key('key1'))

    print('\nPDF - resize example 2')
    print('----------------------')
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            # all inserted keys must be present
            result &= m.contains_key(str(key))
            # NOT inserted keys must be absent
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.get_size(), m.get_capacity(), round(m.table_load(), 2))

    print('\nPDF - table_load example 1')
    print('--------------------------')
    m = HashMap(101, hash_function_1)
    print(round(m.table_load(), 2))
    m.put('key1', 10)
    print(round(m.table_load(), 2))
    m.put('key2', 20)
    print(round(m.table_load(), 2))
    m.put('key1', 30)
    print(round(m.table_load(), 2))

    print('\nPDF - table_load example 2')
    print('--------------------------')
    m = HashMap(53, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(round(m.table_load(), 2), m.get_size(), m.get_capacity())

    print('\nPDF - empty_buckets example 1')
    print('-----------------------------')
    m = HashMap(101, hash_function_1)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key1', 30)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())
    m.put('key4', 40)
    print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print('\nPDF - empty_buckets example 2')
    print('-----------------------------')
    m = HashMap(53, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.get_size(), m.get_capacity())

    print('\nPDF - get example 1')
    print('-------------------')
    m = HashMap(31, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))

    print('\nPDF - get example 2')
    print('-------------------')
    m = HashMap(151, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.get_size(), m.get_capacity())
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)

    print('\nPDF - contains_key example 1')
    print('----------------------------')
    m = HashMap(53, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))

    print('\nPDF - contains_key example 2')
    print('----------------------------')
    m = HashMap(79, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)

    print('\nPDF - remove example 1')
    print('----------------------')
    m = HashMap(53, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')

    print('\nPDF - get_keys_and_values example 1')
    print('------------------------')
    m = HashMap(11, hash_function_2)
    for i in range(1, 6):
        m.put(str(i), str(i * 10))
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(2)
    print(m.get_keys_and_values())

    print('\nPDF - clear example 1')
    print('---------------------')
    m = HashMap(101, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print('\nPDF - clear example 2')
    print('---------------------')
    m = HashMap(53, hash_function_1)
    print(m.get_size(), m.get_capacity())
    m.put('key1', 10)
    print(m.get_size(), m.get_capacity())
    m.put('key2', 20)
    print(m.get_size(), m.get_capacity())
    m.resize_table(100)
    print(m.get_size(), m.get_capacity())
    m.clear()
    print(m.get_size(), m.get_capacity())

    print('\nPDF - find_mode example 1')
    print('-----------------------------')
    da = DynamicArray(['apple', 'apple', 'grape', 'melon', 'peach'])
    mode, frequency = find_mode(da)
    print(f'Input: {da}\nMode : {mode}, Frequency: {frequency}')

    print('\nPDF - find_mode example 2')
    print('-----------------------------')
    test_cases = (
        ['Arch', 'Manjaro', 'Manjaro', 'Mint', 'Mint', 'Mint', 'Ubuntu', 'Ubuntu', 'Ubuntu'],
        ['one', 'two', 'three', 'four', 'five'],
        ['2', '4', '2', '6', '8', '4', '1', '3', '4', '5', '7', '3', '3', '2']
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f'Input: {da}\nMode : {mode}, Frequency: {frequency}\n')
