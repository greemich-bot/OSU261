# Name:Michael Green
# OSU Email:greemich@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 2/9/2026
# Description: Dynamic array implementation of a stack data structure.
# The stack supports push, pop, and top operations.



from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self._da.length()) + " elements. ["
        out += ', '.join([str(self._da[i]) for i in range(self._da.length())])
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the stack is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.is_empty()

    def size(self) -> int:
        """
        Return number of elements currently in the stack
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._da.length()

    # -----------------------------------------------------------------------

    def push(self, value: object) -> None:
        '''
        Docstring for push
        adds a value to the top of the stack
        :param self: the stack instance
        :param value: the value to be pushed onto the stack
        '''
        self._da.append(value)


    def pop(self) -> object:
        '''
        Docstring for pop
        removes and returns the value from the top of the stack
        
        :param self: the stack instance
        :return: the value removed from the top of the stack
        '''
        if self._da.is_empty():
            raise StackException
        value = self._da[self._da.length() - 1]
        self._da.remove_at_index(self._da.length() - 1)
        return value

    def top(self) -> object:
        '''
        Docstring for top
        returns the value from the top of the stack without removing it
        
        :param self: the stack instance
        :return: the value at the top of the stack
        '''
        if self._da.is_empty():
            raise StackException
        return self._da[self._da.length() - 1]


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# push example 1")
    s = Stack()
    print(s)
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    print(s)

    print("\n# pop example 1")
    s = Stack()
    try:
        print(s.pop())
    except Exception as e:
        print("Exception:", type(e))
    for value in [1, 2, 3, 4, 5]:
        s.push(value)
    for i in range(6):
        try:
            print(s.pop())
        except Exception as e:
            print("Exception:", type(e))

    print("\n# top example 1")
    s = Stack()
    try:
        s.top()
    except Exception as e:
        print("No elements in stack", type(e))
    s.push(10)
    s.push(20)
    print(s)
    print(s.top())
    print(s.top())
    print(s)
