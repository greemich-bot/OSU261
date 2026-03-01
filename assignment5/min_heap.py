# Name:Michael C. Green
# OSU Email:greemich@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: March 2, 2026
# Description: Iterative array implementation of a minimum heap data structure (no recursion allowed).
# Methods such as add(), remove_min(), build_heap(), and heapsort() were adapted from algorithms described in the Exploration.
# Other methods such as is_empty(), get_min(), size(), and clear() were implemented using DynamicArray methods.



from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MinHeap with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MinHeap content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return "HEAP " + str(heap_data)

    def add(self, node: object) -> None:
        """
        adds a new object to the heap while maintaining the heap property
        Amortized O(log n)
        adapted from Inserting Into a Heap
        :param self: The MinHeap object
        :param node: The object added to the heap
        """
        #put the new element at the end of the array
        self._heap.append(node)
        # compute the inserted element's parent index
        index = self._heap.length()-1
        parent = (index - 1) // 2
        # compare the value of the inserted element with its parent
        while index > 0 and self._heap[index] < self._heap[parent]:
            # Swap if the value of the parent is greater(percolate up)
            vindex = self._heap[index]
            self._heap[index] = self._heap[parent]
            self._heap[parent] = vindex
            index = parent
            parent = (index - 1) // 2
            


    def is_empty(self) -> bool:
        """
        checker for whether the heap is empty or not
        O(1)
        :param self: The MinHeap object
        :return: True if the heap is empty, False otherwise
        """
        if self._heap.length() == 0:
            return True
        else:
            return False

    def get_min(self) -> object:
        """
        gets the minimum value (root) of the heap without removing it
        O(1) 
        :param self: The MinHeap object
        :return: The minimum value in the heap
        raises MinHeapException if the heap is empty
        """
        if self.is_empty():
            raise MinHeapException
        else:
            return self._heap[0]
        

    def remove_min(self) -> object:
        """
        removes the minimum value (root) of the heap while maintaining the heap property
        amortized O(log n)
        adapted from Removing From a Heap
        :param self: The MinHeap object     
        :return: The minimum value in the heap that was removed
        raises MinHeapException if the heap is empty
        """
        # check if the heap is empty
        if self.is_empty():
            raise MinHeapException
        else:
            # preserve the minimum value to return later
            minimum =self.get_min()
            # move the last element to the root
            self._heap[0] = self._heap[self._heap.length()-1]
            # remove the last element from the array
            self._heap.pop()
            # check if the heap is not empty after removing the minimum element
            if self._heap.is_empty() == False:
                # percolate down the new root element to restore the heap property
                _percolate_down(self._heap, 0)
            return minimum

    def build_heap(self, da: DynamicArray) -> None:
        """
        turns a DynamicArray into a MinHeap
        O(n)
        adapted from Building a Heap, and Removing From a Heap steps 3-5
        :param self: The MinHeap object
        :param da: The DynamicArray to become a MinHeap
        """
        # copy the elements of the input da into the heap
        self._heap = DynamicArray()
        for i in range(da.length()):
            self._heap.append(da[i])
        # start at the first non leaf element 
        start = (self._heap.length() // 2) - 1
        # move backwards and percolate down each element
        for i in range(start, -1, -1):
            _percolate_down(self._heap, i)

    def size(self) -> int:
        """
        returns the number of elements currently stored in the heap
        O(1)    
        :param self: The MinHeap object
        :return: The number of elements in the heap
        """
        return self._heap.length()

    def clear(self) -> None:
        """
        clears the contents of the heap
        O(1)
        :param self: The MinHeap object
        """
        self._heap = DynamicArray()


def heapsort(da: DynamicArray) -> None:
    """
    takes a da and sorts in place (non-ascending) without creating any data structures
    O(n log n)
    :param da: The DynamicArray to be sorted
    """
    # O(n) heapify the input da using the the same logic as build_heap
    start = (da.length() // 2) - 1
    for i in range(start, -1, -1):
        _percolate_down(da, i)
    # start at one less than the size of the array and shrink the "heap" portion by one element each time until we reach the beginning of the array
    for k in range(da.length() - 1, 0, -1):
        # swap the first element with the kth element
        first = da[0]
        da[0] = da[k]
        da[k] = first
        # percolate down the new root using the limiter
        _percolate_down(da, 0, k)
        

    
    


# It's highly recommended that you implement the following optional          #
# helper function for percolating elements down the MinHeap. You can call    #
# this from inside the MinHeap class. You may edit the function definition.  #

def _percolate_down(da: DynamicArray, parent: int, limit: int = None) -> None:
    """
    helper method for  remove_min() that percolates an element down the heap to restore the heap property iteratively.
    O(log n) 
    adapted from Removing From a Heap steps 3-5 
    :param da: The DynamicArray representing the heap
    :param parent: The index of the element to percolate down
    :param limit: The index limit for percolation (to use k in heapsort)
    :return: None
    """
    percolate = True
    # percolate to the last element of the heap if no limit is provided
    if limit is None:
        limit = da.length()

    while percolate:
        # compute the indices of the left and right children of the parent
        left = 2 * parent + 1
        right = 2 * parent + 2
        minimum = parent

        # compare the value of the parent with its children and find the minimum value
        if left < limit and da[left] < da[minimum]:
            minimum = left   
        if right < limit and da[right] < da[minimum]:
            minimum = right 
        # if the minimum value is the parent stop percolating down
        if minimum == parent:
            break

        # swap the parent with the minimum value
        temp = da[parent]
        da[parent] = da[minimum]
        da[minimum] = temp
        parent = minimum


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference the same object in memory")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")
