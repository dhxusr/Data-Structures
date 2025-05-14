
"""
Describe how to implement the stack ADT using a single queue as an instance variable, and only constant
addtional local memory within the method bodies. what is the running time of the push(), pop(), and top()
methods for your design.
"""

from stack.ArrayStack import Empty
from queues.ArrayQueue import ArrayQueue as Queue

class StackQueue:

    def __init__(self):

        self._data = Queue()
        self._top = None
        
    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self._data.is_empty()

    def top(self):
        """Return the top element in the stack."""
           
        if self.is_empty():
            raise Empty("The stack is empty")

        return self._top

    def push(self, element):
        """The enqueue method has the same behavior of the stack push method."""

        self._top = element
        self._data.enqueue(element)

    def pop(self):
        """delete the last element in the stack.

           in the queue we have to dequeue all elements before to get the lastest.
           so we re-enqueue all the n-1 elements."""

        if self.is_empty():
            raise Empty("The stack is empty.")

        if len(self._data) == 1:
            return self._data.dequeue()

        #re-inserting n-1 elements        
        to_rotate = len(self._data) - 1
        self._data._rotate(to_rotate)

        element = self._data.dequeue()
        self._top = self._data.first()
        return element


import unittest

class TestStackQueue(unittest.TestCase):

    def test_push_and_pop(self):
        s = StackQueue()
        s.push(10)
        s.push(20)
        s.push(30)
        self.assertEqual(s.pop(), 30)
        self.assertEqual(s.pop(), 20)
        self.assertEqual(s.pop(), 10)
        self.assertTrue(s.is_empty())

    def test_top(self):
        s = StackQueue()
        s.push("a")
        s.push("b")
        self.assertEqual(s.top(), "b")
        s.pop()
        self.assertEqual(s.top(), "a")

    def test_empty(self):
        s = StackQueue()
        self.assertTrue(s.is_empty())
        with self.assertRaises(Empty):
            s.pop()
        with self.assertRaises(Empty):
            s.top()

    def test_single_element_pop(self):
        s = StackQueue()
        s.push(42)
        self.assertEqual(s.pop(), 42)
        self.assertTrue(s.is_empty())

    def test_order_with_rotation(self):
        s = StackQueue()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        s.push(4)
        self.assertEqual(s.pop(), 4)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

if __name__ == '__main__':
    unittest.main()
