"""
Implement a method, concatenate(Q2) for the LinkedQueue class that takes all elements of LinkedQueue Q2 and
appends them to the end of the  original queue. The operation should run in O(1) time and should resutl in
Q2 being an empty queue.
"""

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
        
        
    def concatenate(self, other_queue):
        """takes all elements in other_queue and appends them to the end of the original queue.        
           other_queue result in an empty queue."""

        if not isinstance(other_queue, LinkedQueue):
            raise ValueError("Invalid argument type. must be of type LinkedQueue.")

        if self.is_empty() or other_queue.is_empty():
            raise Empty("One of the Queue is empty.")

        if other_queue is self:
            raise ValueError("The given queue is the same as the original.")

        self._tail._next = other_queue._head
        self._tail = other_queue._tail        
        self._size += other_queue._size

        other_queue._tail = None
        other_queue._head = None
        other_queue._size = 0
        
class Empty(Exception):
    """Return an Empty exception"""


if __name__ == "__main__":

    q1 = LinkedQueue()
    q2 = LinkedQueue()

    for i in range(5):
        q1.enqueue(i+1)
        q2.enqueue(i+6)

    print("Testing concatenate empty.")
    q3 = LinkedQueue()

    try:
        q1.concatenate(q3)
    except Empty as err:
        print(err)
        pass

    print("Testing concatenate two queues.")
    q1.concatenate(q2)
    head = q1._head
    while head:
        print(head._element, end=' ')
        head = head._next

    print(' ')
    print(f"q2 is empty: {q2.is_empty()}")
    print("testing connection.")
    print("dequeueing...")
    for i in range(5):
        print(f"element: {q1.dequeue()}")

    print(f"first must be 6, is: {q1.first()}")

    print("Testing concatenate self queue.")
    try:
        q1.concatenate(q1)
    except ValueError as err:
        print(err)
        pass

    print("All tests passes.")
            
