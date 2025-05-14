
"""
Give a complete ArrayDeque implementation of the double-ended queue ADT as sketched in Section 6.3.2
"""

from queues.ArrayQueue import ArrayQueue as Queue
from stack.ArrayStack import Full, Empty

class ArrayDeque(Queue):

    def __init__(self, maxlen: int | None = None):

        super().__init__(maxlen)

    def last(self):
        """Return the las element in the Deque."""

        if self.is_empty():
            raise Empty("The Deque is empty.")

        last = (self._first + self._size - 1) % len(self._data)
        return self._data[last]

    def add_first(self, element):
        """Add an element at front of the Deque."""

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
        """Add an element at the back of the Deque."""
        self.enqueue(element)
        

    def delete_first(self):
        """Delete the first element inserted in the Deque and return it."""

        return self.dequeue()

        
    def delete_last(self):
        """Delete the last element in the Deque."""
        if self.is_empty():
            raise Empty("The Deque is empty.")
        
        capacity = len(self._data)
        last = (self._first + self._size - 1) % capacity
        element = self._data[last]
        self._data[last] = None
        self._size -= 1

        if 0 < self._size < capacity // 4:
            self._resize(capacity // 2)

        return element


import unittest

class TestArrayDeque(unittest.TestCase):

    def test_add_and_delete_first(self):
        dq = ArrayDeque()
        dq.add_first(10)
        dq.add_first(20)
        dq.add_first(30)
        self.assertEqual(dq.delete_first(), 30)
        self.assertEqual(dq.delete_first(), 20)
        self.assertEqual(dq.delete_first(), 10)
        with self.assertRaises(Empty):
            dq.delete_first()

    def test_add_and_delete_last(self):
        dq = ArrayDeque()
        dq.add_last(1)
        dq.add_last(2)
        dq.add_last(3)
        self.assertEqual(dq.delete_last(), 3)
        self.assertEqual(dq.delete_last(), 2)
        self.assertEqual(dq.delete_last(), 1)
        with self.assertRaises(Empty):
            dq.delete_last()

    def test_mixed_operations(self):
        dq = ArrayDeque()
        dq.add_last(1)
        dq.add_first(2)
        dq.add_last(3)
        dq.add_first(4)
        self.assertEqual(dq.delete_first(), 4)
        self.assertEqual(dq.delete_last(), 3)
        self.assertEqual(dq.delete_first(), 2)
        self.assertEqual(dq.delete_last(), 1)

    def test_last_method(self):
        dq = ArrayDeque()
        dq.add_last("a")
        dq.add_last("b")
        dq.add_last("c")
        self.assertEqual(dq.last(), "c")
        dq.delete_last()
        self.assertEqual(dq.last(), "b")

    def test_full_capacity(self):
        dq = ArrayDeque(maxlen=3)
        dq.add_first(1)
        dq.add_last(2)
        dq.add_first(3)
        with self.assertRaises(Full):
            dq.add_last(4)

    def test_resize_down(self):
        dq = ArrayDeque()
        for i in range(8):  # Fill up to resize
            dq.add_last(i)
        for _ in range(6):  # Shrink capacity
            dq.delete_last()
        # Ensure it still works after resizing
        dq.add_last(100)
        self.assertEqual(dq.last(), 100)

if __name__ == '__main__':
    unittest.main()

    
