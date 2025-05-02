"""
Implementing a Queue with a Circulaly Linked List

To implement the queue ADT using a circularly linked list, we rely on the intuition in which the queue has
a head and a tail, but with the next reference of the tail linked to the head. Given such a model, there is no
need for us to explicitly store references to both the hed an the tail; as long as we keep a reference to the
tail, we can always find the head by following the tail's next reference.

provide an implementation of a CircularQueue class based on this model. The only two instance variables are
_tail and _size.

In addition to the traditional queue operations, the CircularQueue class supports a rotate method
"""


class CircularQueue:

    class _Node:

        def __init__(self, element, next):

            self.element = element
            self.next = next

    def __init__(self):

        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """Return True if the Queue is empty. False otherwise"""

        return self._size == 0


    def first(self):
        """Return the first element in the Queue. raise an Empty error if empty."""
        if self.is_empty():
            raise Empty("The queue is empty.")

        return self._tail.next.element


    def enqueue(self, element):
        """Insert an element in the Queue."""

        new_node = self._Node(element, None)

        # if the queue is empty, tail points to itself
        if self.is_empty():
            new_node.next = new_node

        else:
            new_node.next = self._tail.next
            self._tail.next = new_node

        self._tail = new_node
        self._size += 1


    def dequeue(self):
        """Delete and return the first element in the queue. raise an Empty erro if empty."""

        if self.is_empty():
            raise Empty("The queue is empty.")

        # if just is tail in the queue setting as to_remove emediatly
        to_remove = self._tail.next
        if self._size > 1:
            self._tail.next = to_remove.next

        else:
            self._tail = None
            
        self._size -= 1
        return to_remove.element


    def rotate(self, times: int):
        """Rotate the first value a certain number of times"""

        if self.is_empty():
            raise Empty("The queue is empty.")

        if times <= 0:
            raise ValueError("Invalid number of times to rotate, must be a positive number.")

        if times > self._size:
            raise ValueError("Invalid number of times to rotate. is greater than the actual number of values.")

        for _ in range(times):
            self._tail = self._tail.next


class Empty(Exception):
    """Raise an empty exception."""


def test():

    queue = CircularQueue()

    print("Testing...")
    print('-'*20)
    print("Testing empty")
    try:
        queue.dequeue()

    except Empty as e:
        print(e)

    try:
        queue.first()

    except Empty as e:
        print(e)

    print('-'*20)
    print("Testing enqueue.")
    print("enqueueing 1-5")
    for i in range(5):
        queue.enqueue(i+1)

    print(f"first must be 1. is: {queue.first()}")

    print('-'*20)
    print("Testing dequeue.")
    print("dequeueing...")
    print(f"must be 1. is: {queue.dequeue()}")
    print(f"first must be 2. is {queue.first()}")
    print(f"must be 2. is: {queue.dequeue()}")
    print(f"must be 3. is: {queue.dequeue()}")
    print(f"must be 4. is: {queue.dequeue()}")
        
    print('-'*20)
    print("Testing one element.")
    queue.dequeue()
    print(f"is empty? must be true. is: {queue.is_empty()}")
    queue.enqueue(1)
    print(f"first must be 1. is: {queue.first()}")
    
    print('-'*20)
    print("Testing new queue one element.")
    queue = CircularQueue()
    queue.enqueue(1)
    print(f"first must be 1. is: {queue.first()}")
    queue.dequeue()

    print("All tests passes...")

if __name__ == "__main__":
    test()
