"""
Implementing a Queue with a python list class.
this queue supports circular behavior, that means that the queue has a determined capacity  and if we want
to enqueue an element, if there are space it will seting there, otherwise, the queue is resized.  
"""

from ArrayStack import Full, Empty

class ArrayQueue:
    
    def __init__(self, maxlen=None):

        self._maxlen = maxlen
        self._data = [None] * (maxlen if maxlen != None else 10) 
        self._size = 0
        self._first = 0

    def __len__(self):

        if self.is_empty():
            raise Empty("The queue is empty.")

        return self._size


    def enqueue(self, element):
        capacity = len(self._data)

        if self._size == self._maxlen:
            raise Full("The Queue is full.")

        if self._size == capacity:
            capacity *= 2
            self._resize(capacity)

        new = (self._first + self._size) % capacity
        self._data[new] = element
        self._size += 1


    def dequeue(self):
        if self.is_empty():
            return Empty("The queue is empty.")
        
        capacity = len(self._data)
        element = self._data[self._first]
        self._data[self._first] = None
        self._first = (self._first + 1) % capacity
        self._size -= 1

        if 0 < self._size < capacity // 4:
            self._resize(capacity // 2)

        return element


    def _rotate(self, number: int):
        """rotate a certain number of elements in the queue."""
        if number == 0:
            raise ValueError("Invalid argument value: 0.")

        capacity = len(self._data)

        for _ in range(number):
            element = self._data[self._first]
            self._data[self._first] = None
            new = (self._first + self._size) % capacity
            self._data[new] = element
            self._first = (self._first + 1) % capacity            

        
    def first(self):
        return self._data[self._first]
    

    def is_empty(self):
        return self._size == 0


    def _resize(self, capacity):
        old = self._data
        self._data = [None] * capacity

        for i in range(self._size):
            self._data[i] = old[self._first]
            self._first = (self._first + 1) % len(old)

        self._first = 0
