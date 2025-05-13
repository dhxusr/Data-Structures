"""
Implementing a Deque with a doubly linked list.
"""
from node import _Node
from doubly_linked_list import _DoublyLinkedBase

class LinkedDeque(_DoublyLinkedBase):


    def is_empty(self):
        """Return True if the Deque is empty."""
        return self._size == 0


    def first(self):
        """Return the first element at the front of the deque. error if empty."""

        if self.is_empty():
            raise Empty("The deque is empty.")

        first_node = self._header._next
        return first_node._element


    def last(self):
        """Return the first element at the back of the Deque. error if empty."""

        if self.is_empty():
            raise Empty("The Deque is empty.")

        last_node = self._trailer._prev
        return last_node._element


    def add_first(self, element):
        """Insert an element at the front of the Deque."""

        self._insert_between(element, self._header, self._header._next)


    def add_last(self, element):
        """Insert an element at the back of the Deque."""

        self._insert_between(element, self._trailer._prev, self._trailer)


    def delete_first(self):
        """Remove and return the first element at the front of the Deque. error if empty."""
        if self.is_empty():
            raise Empty("The Deque is empty.")

        return self._delete_node(self._header._next)


    def delete_last(self):
        """Remove and return the first element at the back of the Deque. error if empty."""

        if self.is_empty():
            raise Empty("The Deque is empty.")

        return self._delete_node(self._trailer._prev)


    def rotate(self):
        """Move the first element to the back of the Deque. error if empty."""

        if self.is_empty():
            raise Empty("The stack is empty.")

        #getting the node and setting the new last
        node = self._trailer._prev
        new_last = node._prev

        new_last._next = self._trailer
        self._trailer._prev = new_last

        #conecting the to the front
        current_first = self._header._next
        node._next = current_first
        current_first._prev = node

        self._header._next = node
        node._prev = self._header


class Empty(Exception):
    """Raise an Empty exception."""


import unittest

class TestArrayDeque(unittest.TestCase):

    def test_add_and_delete_first(self):
        dq = LinkedDeque()
        dq.add_first(10)
        dq.add_first(20)
        dq.add_first(30)
        self.assertEqual(dq.delete_first(), 30)
        self.assertEqual(dq.delete_first(), 20)
        self.assertEqual(dq.delete_first(), 10)
        with self.assertRaises(Empty):
            dq.delete_first()

    def test_add_and_delete_last(self):
        dq = LinkedDeque()
        dq.add_last(1)
        dq.add_last(2)
        dq.add_last(3)
        self.assertEqual(dq.delete_last(), 3)
        self.assertEqual(dq.delete_last(), 2)
        self.assertEqual(dq.delete_last(), 1)
        with self.assertRaises(Empty):
            dq.delete_last()

    def test_mixed_operations(self):
        dq = LinkedDeque()
        dq.add_last(1)
        dq.add_first(2)
        dq.add_last(3)
        dq.add_first(4)
        self.assertEqual(dq.delete_first(), 4)
        self.assertEqual(dq.delete_last(), 3)
        self.assertEqual(dq.delete_first(), 2)
        self.assertEqual(dq.delete_last(), 1)

    def test_last_method(self):
        dq = LinkedDeque()
        dq.add_last("a")
        dq.add_last("b")
        dq.add_last("c")
        self.assertEqual(dq.last(), "c")
        dq.delete_last()
        self.assertEqual(dq.last(), "b")

if __name__ == '__main__':
    unittest.main()        
