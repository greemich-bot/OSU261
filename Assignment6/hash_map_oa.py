# Name: Michael Green
# OSU Email: Greemich@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:6 - HashMap with Open Addressing
# Due Date: 3/12/2026
# Description: Implementation of hashmap that uses open addressing with quadratic probing for collision resolution.

from a6_include import (DynamicArray, HashEntry,
                        hash_function_1, hash_function_2)


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Initialize new HashMap that uses
        quadratic probing for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._buckets = DynamicArray()

        # capacity must be a prime number
        self._capacity = self._next_prime(capacity)
        for _ in range(self._capacity):
            self._buckets.append(None)

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
        Increment from given number to find the closest prime number
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
        adds/updates kv pair in hashmap. if a key exists, the value assosciated is replaced.
        :param key: the key to be added/updated in the table
        :param value: the value to be associated with the key in the table
        """
        # if the load factor is too high, resize the table to double its current capacity
        while self.table_load() >= 0.5:
            self.resize_table(self._capacity * 2)
        # find the index to begin probing
        initialIndex = self._hash_function(key) % self._capacity
        index = initialIndex

        # iniialize i and firstTombstoneIndex to keep track of the first tombstone we find while probing
        i = 0   
        firstTombstoneIndex = None
        # probe until we find an empty bucket
        while self._buckets[index] is not None: 
            entry = self._buckets[index]
            # if we find the key, update the value and return
            if entry.key==key:
                # if it was a tombstone we need to mark it as active again and update the size
                if entry.is_tombstone:
                    entry.is_tombstone = False
                    self._size += 1
                entry.value = value
                return
            # when probing, save the first tombstone so we can use it for insertion if we don't find the key
            if entry.is_tombstone and firstTombstoneIndex is None:
                firstTombstoneIndex = index
            # increment i and calculate the next index to probe
            i += 1
            index = (initialIndex + i**2) % self._capacity
        # if we found a tombstone while probing, put the new kv pair there 
        if firstTombstoneIndex is not None:
            self._buckets[firstTombstoneIndex] = HashEntry(key, value)
        # otherwise, put it in the first empty bucket we found
        else:
            self._buckets[index] = HashEntry(key, value)
        # increment the size in either case.
        self._size += 1

    def resize_table(self, new_capacity: int) -> None:
        """
        changes the capacity of the underlying table. all non tombstone links are rehashed.
        :param new_capacity: the new capacity of the table. 
        """
        # make sure it will fit all the current elements
        if new_capacity < self._size:
            return
        # make sure the new capacity is prime
        if not self._is_prime(new_capacity):
            new_capacity = self._next_prime(new_capacity)
        
        # save the old capacity and buckets for rehashing
        og_capacity = self._capacity
        og_buckets = self._buckets
        # create new buckets and update capacity and size
        self._capacity = new_capacity
        self._buckets = DynamicArray()
        # initialize new buckets to None
        for _ in range(self._capacity):
            self._buckets.append(None)  
        self._size = 0
        # rehash only the non tombstone entries from the old buckets
        for i in range(og_capacity):
            if og_buckets[i] is not None and og_buckets[i].is_tombstone is False:
                # indirect recursion allowed for resize and put methods.
                self.put(og_buckets[i].key, og_buckets[i].value)

    def table_load(self) -> float:
        """
        returns the current hash table load factor
        load factor = (number of elements in the table) / (capacity of the table)
        """
        loadFactor = self._size / self._capacity
        return loadFactor

    def empty_buckets(self) -> int:
        """
        returns the number of empty buckets in the table
        """
        emptyBuckets = 0
        for i in range(self._capacity):
            if self._buckets[i] is None or self._buckets[i].is_tombstone is True:
                emptyBuckets += 1
        return emptyBuckets 

    def get(self, key: str) -> object:
        """
        returns the value associated with the given key. if the key is not in the table, returns None.
        :param key: the key to find in the table
        """
        pass

    def contains_key(self, key: str) -> bool:
        """
        checks to see if the given key exists
        :param key: the key to find in the table
        """
        pass

    def remove(self, key: str) -> None:
        """
        removes the given key and its value from the hashmap
        :param key: the key to remove from the table
        """
        pass

    def get_keys_and_values(self) -> DynamicArray:
        """
        returns a dynamic array of all keys and values in the hashmap
        """
        pass

    def clear(self) -> None:
        """
        clears the hashmap, removing all keys and values without changing the underlying capacity
        """
        pass

    def __iter__(self):
        """
        TODO: Write this implementation
        """
        pass

    def __next__(self):
        """
        TODO: Write this implementation
        """
        pass


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
    keys = [i for i in range(25, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.get_size(), m.get_capacity())

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        if m.table_load() > 0.5:
            print(f'Check that the load factor is acceptable after the call to resize_table().\n'
                  f'Your load factor is {round(m.table_load(), 2)} and should be less than or equal to 0.5')

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
    m = HashMap(11, hash_function_1)
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

    m.resize_table(2)
    print(m.get_keys_and_values())

    m.put('20', '200')
    m.remove('1')
    m.resize_table(12)
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

    print('\nPDF - __iter__(), __next__() example 1')
    print('---------------------')
    m = HashMap(10, hash_function_1)
    for i in range(5):
        m.put(str(i), str(i * 10))
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)

    print('\nPDF - __iter__(), __next__() example 2')
    print('---------------------')
    m = HashMap(10, hash_function_2)
    for i in range(5):
        m.put(str(i), str(i * 24))
    m.remove('0')
    m.remove('4')
    print(m)
    for item in m:
        print('K:', item.key, 'V:', item.value)
