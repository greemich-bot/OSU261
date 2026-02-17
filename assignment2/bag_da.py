# Name:Michael Green
# OSU Email:Greemich@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment:2 part 2
# Due Date:Feb 2, 2026
# Description: implementation of Bag ADT using Dynamic Array

#
from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

        # populate bag with initial values (if provided)
        # before using this feature, implement add() method
        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da.get_at_index(_))
                          for _ in range(self._da.length())])
        return out + ']'

    def size(self) -> int:
        """
        Return total number of items currently in the bag
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def add(self, value: object) -> None:
        '''
        Docstring for add
        adds an object to the bag
        :param self: Bag instance
        :param value: object to be added to the bag
        
        ''' 
        self._da.append(value)

    def remove(self, value: object) -> bool:

        '''
        Docstring for remove
        removes one occurrence of an object from the bag, if found
        :param self: Bag instance
        :param value: object to be removed from the bag
        :return: True if the object was removed, False otherwise
        '''
        #initialize removed to false
        removed = False
        #iterate through dynamic array to find value, when/if found remove and set removed to true
        #break after first removal
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                self._da.remove_at_index(i)
                removed = True
                break
        return removed  

    def count(self, value: object) -> int:
        '''
        Docstring for count
        counts the number of occurrences of an object in the bag
        :param self: Bag instance
        :param value: object to count in the bag
        :return: number of occurrences of the specified object in the bag
        '''
        
        count = 0
        for i in range(self._da.length()):
            if self._da.get_at_index(i) == value:
                count += 1
        return count


    def clear(self) -> None:
        '''
        Docstring for clear
        empties the bag of all its contents
        :param self: Bag instance
        '''
        self._da = DynamicArray()   


    def equal(self, second_bag: "Bag") -> bool:
        '''
        Docstring for equal
        determines whether two bags are equal in terms of their contents and counts of each element
        :param self: Bag instance
        :param second_bag: Bag instance to compare with
        :return: True if the bags are equal, False otherwise
        '''

        #check if sizes are different, possible early exit
        if self.size() != second_bag.size():
            return False
        
        #compare counts of each unique element in self to counts in second_bag
        for i in range(self._da.length()):
            current_value = self._da.get_at_index(i)
            count_self = self.count(current_value)
            count_second = second_bag.count(current_value)

            if count_self != count_second:
                return False

        return True

    def __iter__(self):
      '''
      Docstring for __iter__
      
      :param self: Bag instance 
      :return: iterator object
      '''
      self._index = 0
      return self

    def __next__(self):
        '''
        Docstring for __next__
        
        :param self: Bag instance
        :return: next object in the bag during iteration
        :raises StopIteration: when there are no more items to iterate over    
        '''     
        if self._index < self._da.length():
            value = self._da.get_at_index(self._index)
            self._index += 1
            return value
        else:
            raise StopIteration
       

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# add example 1")
    bag = Bag()
    print(bag)
    values = [10, 20, 30, 10, 20, 30]
    for value in values:
        bag.add(value)
    print(bag)

    print("\n# remove example 1")
    bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
    print(bag)
    print(bag.remove(7), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)
    print(bag.remove(3), bag)

    print("\n# count example 1")
    bag = Bag([1, 2, 3, 1, 2, 2])
    print(bag, bag.count(1), bag.count(2), bag.count(3), bag.count(4))

    print("\n# clear example 1")
    bag = Bag([1, 2, 3, 1, 2, 3])
    print(bag)
    bag.clear()
    print(bag)

    print("\n# equal example 1")
    bag1 = Bag([10, 20, 30, 40, 50, 60])
    bag2 = Bag([60, 50, 40, 30, 20, 10])
    bag3 = Bag([10, 20, 30, 40, 50])
    bag_empty = Bag()

    print(bag1, bag2, bag3, bag_empty, sep="\n")
    print(bag1.equal(bag2), bag2.equal(bag1))
    print(bag1.equal(bag3), bag3.equal(bag1))
    print(bag2.equal(bag3), bag3.equal(bag2))
    print(bag1.equal(bag_empty), bag_empty.equal(bag1))
    print(bag_empty.equal(bag_empty))
    print(bag1, bag2, bag3, bag_empty, sep="\n")

    bag1 = Bag([100, 200, 300, 200])
    bag2 = Bag([100, 200, 30, 100])
    print(bag1.equal(bag2))

    print("\n# __iter__(), __next__() example 1")
    bag = Bag([5, 4, -8, 7, 10])
    print(bag)
    for item in bag:
        print(item)

    print("\n# __iter__(), __next__() example 2")
    bag = Bag(["orange", "apple", "pizza", "ice cream"])
    print(bag)
    for item in bag:
        print(item)
