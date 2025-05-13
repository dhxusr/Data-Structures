"""
Give a complete implementation of the queue ADT using a singly linked list that includes a header sentinel.
"""

class Node:

    def __init__(self, element, next):
        self._element = element
        self._next = next


class SinglyList:

    def __init__(self):

        self._header = Node(None, None)
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size


    def add_head(self, element):
        """Insert an element at the front of the list. and return the new node"""

        new_node = Node(element, self._header._next)
        self._header._next = new_node

        if self._size == 0:
            self._tail = new_node

        self._size += 1
        return new_node


    def add_tail(self, element):
        """Insert an element at the back of the list. and reeturn the new node"""

        new_node = Node(element, None)

        if self._size == 0:
            self._header._next = new_node
        else:
            self._tail._next = new_node

        self._tail = new_node
        self._size += 1
        return new_node


    def delete(self):
        """Delete and return the first element at the front of the list."""

        if self._size == 0:
            return None

        if self._size == 1:
            self._tail = None

        node_to_delete = self._header._next
        self._header._next = node_to_delete._next

        element = node_to_delete._element
        node_to_delete._element = None

        self._size -= 1
        return element
        

        
class Queue:

    def __init__(self, maxlen=None):

        self._data = SinglyList()
        self._first = None
        self._maxlen = maxlen

    def __len__(self):
        return len(self._data)


    def is_empty(self):
        """Return True if the Queue is empty."""

        return len(self._data) == 0


    def first(self):
        """Return the first element in the queue, error if empty."""

        if self.is_empty():
            raise Empty("The Queue is empty.")

        return self._first._element


    def enqueue(self, element):
        """Insert an element in the queue."""

        if self._maxlen == len(self._data):
            raise Full("The Queue is full.")

        node = self._data.add_tail(element)
        if self._first is None:
            self._first = node            


    def dequeue(self):
        """Delete and return the first element in the Queue."""

        if self.is_empty():
            raise Empty("The Queue is empty.")

        element = self._data.delete()
        self._first = self._data._header._next
        return element

class Empty(Exception):
    """Raise an Empty exception."""

class Full(Exception):
    """Raise a Full exception."""


def test():

    queue = Queue()    
    print("Testing normal queue enqueue and dequeue.")
    for i in range(5):
        queue.enqueue(i+1)

    print("testing non empty first.")
    assert queue.first() == 1

    print("Testing dequeue.")
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.first() == 4

    print("Testing len")
    assert len(queue) == 2

    print("Testing dequeue until empty.")
    try:
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
    except Empty:
        pass

    print("Testing queue with maxlen.")
    queue = Queue(10)

    try:
        queue.first()
    except Empty:
        pass

    print("Testing full queue.")
    try:
        for i in range(11):
            queue.enqueue(i+1)
    except Full:
        pass

    print("All tests passes.")    
     
    
if __name__ == "__main__":
    test()
