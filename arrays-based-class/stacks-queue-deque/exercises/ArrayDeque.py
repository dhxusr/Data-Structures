
"""
Give a complete ArrayDeque implementation of the double-ended queue ADT as sketched in Section 6.3.2
"""
from ArrayQueue import ArrayQueue as Queue
from ArrayStack import Full, Empty

class ArrayDeque(Queue):

    def __init__(self, maxlen: int | None = None):

        super().__init__(maxlen)

    def last(self):
        """Return the las element in the Queue."""

        if self.is_empty():
            raise Empty("The Deque is empty.")

        last = (self._first + self._size - 1) % len(self._data)
        return self._data[last]

    def add_first(self, element):
        """Add an element at front of the queue."""

        capacity = len(self._data)
        if self._size == self._maxlen:
            raise Full("The Deque is full.")

        if self._size == capacity:
            self._resize(2 * capacity)
            capacity = len(self._data)

        self._first = (self._first - 1) % capacity if self._size > 0 else 0
        self._data[self._first] = element
        self._size += 1


    def add_last(self, element):
        """Add an element at the back of the queue."""
        self.enqueue(element)
        

    def delete_first(self):
        """Delete the last element inserted in the queue and return it."""

        return self.dequeue()

        
    def delete_last(self):
        
        if self.is_empty():
            return Empty("The queue is empty.")
        
        capacity = len(self._data)
        last = (self._first + self._size - 1) % capacity
        element = self._data[last]
        self._data[last] = None
        self._size -= 1

        if 0 < self._size < capacity // 4:
            self._resize(capacity // 2)

        return element
