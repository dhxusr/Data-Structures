"""
Implementing a Queue with a single linked List
"""

from types import new_class


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:

        def __init__(self, element, next):

            self._element = element
            self._next = next


    def __init__(self):

        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):

        return self._size


    def first(self):
        """Return the oldest element in the queue."""

        if self.is_empty():
            raise Empty("The Queue is empty.")

        return self._head._element


    def is_empty(self):
        """Return True if the Queue is empty. False otherwise."""

        return self._size == 0


    def enqueue(self, element):
        """Insert an element in the Queue."""

        new_node = self._Node(element, None)

        if self.is_empty():
           self._head = new_node

        else:
            self._tail._next = new_node

        self._tail = new_node
        self._size += 1


    def dequeue(self):
        """Delete and return the oldest element in the Queue.""" 

        if self.is_empty():
            raise Empty("The Queue is empty.")

        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return element

    def rotate(self):
        """Move the first element of the queue. to the back."""

        if self.is_empty():
            raise Empty("The Queue is empty.")

        self._tail._next = self._head
        self._tail = self._head
        self._head = self._head._next
        self._tail._next = None
        
        
class Empty(Exception):
    """Return an Empty exception"""


def test():

    queue = LinkedQueue()

    print("Testing linkedqueue")
    print("testing enqueue")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"first must be 1. is: {queue.first()}")
    queue.enqueue(4)
    queue.enqueue(5)
    print("Testing len.")
    print(f"len must be 5. is: {len(queue)}")
    print('-'*20)
    print("testing dequeue.")
    print(f"dequeue must be 1. is: {queue.dequeue()}")
    print(f"dequeue must be 2. is: {queue.dequeue()}")
    print(f"dequeue must be 3. is: {queue.dequeue()}")
    print(f"dequeue must be 4. is: {queue.dequeue()}")
    queue.enqueue(6)
    print(f"first must be 5. is: {queue.first()}")

    print('-'*20)
    print("Testing empty")
    print("dequeueing...")
    for _ in range(5):
        try:
            queue.dequeue()
        except Empty as err:
            print(err)
            break

    print("Testing No elements.")
    queue = LinkedQueue()
    try:
        queue.first()
    except Empty as err:
        print(err)

    print("Testing rotate...")
    for i in range(5):
        queue.enqueue(i)
    
    print("first:", queue.first())
    print("rotating...")
    queue.rotate()
    print("new first", queue.first())
        
    print("All test passes...")

if __name__ == "__main__":
    test()
