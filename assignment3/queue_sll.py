# Name: Michael Green
# OSU Email: greemich@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 3
# Due Date: 2/9/26
# Description: Singly linked list implementation of a queue data structure. 
# The queue supports enqueue, dequeue, and front operations.


from SLNode import SLNode


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self) -> None:
        """
        Initialize new queue with head and tail nodes
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._head = None
        self._tail = None

    def __str__(self):
        """
        Return content of queue in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = 'QUEUE ['
        if not self.is_empty():
            node = self._head
            out = out + str(node.value)
            node = node.next
            while node:
                out = out + ' -> ' + str(node.value)
                node = node.next
        return out + ']'

    def is_empty(self) -> bool:
        """
        Return True is the queue is empty, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._head is None

    def size(self) -> int:
        """
        Return number of elements currently in the queue
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        node = self._head
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    # -----------------------------------------------------------------------

    def enqueue(self, value: object) -> None:
        '''
        Docstring for enqueue
        add a new value to the back of the queue
        :param self: the instance of the Queue class
        :param value: the value to be added to the back of the queue
        '''
        new_node = SLNode(value)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def dequeue(self) -> object:
        '''
        Docstring for dequeue
        remove and return the value at the front of the queue
        :param self: the instance of the Queue class
        :return: the value at the front of the queue
        :raises QueueException: if the queue is empty
        '''
        if self.is_empty():
            raise QueueException("Queue is empty")
        else:
            value = self._head.value
            self._head = self._head.next
            if self._head is None:
                self._tail = None
            return value

    def front(self) -> object:
        '''
        Docstring for front
        check the value at the front of the queue without removing it
        :param self: the instance of the Queue class
        :return: the value at the front of the queue without removing it
        '''
        if self.is_empty():
            raise QueueException("Queue is empty")
        else:
            return self._head.value


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# enqueue example 1")
    q = Queue()
    print(q)
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)

    print("\n# dequeue example 1")
    q = Queue()
    for value in [1, 2, 3, 4, 5]:
        q.enqueue(value)
    print(q)
    for i in range(6):
        try:
            print(q.dequeue())
        except Exception as e:
            print("No elements in queue", type(e))

    print('\n#front example 1')
    q = Queue()
    print(q)
    for value in ['A', 'B', 'C', 'D']:
        try:
            print(q.front())
        except Exception as e:
            print("No elements in queue", type(e))
        q.enqueue(value)
    print(q)
