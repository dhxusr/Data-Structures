
"""
notes that stacks are often used to provide "undo" support in applications like a web browser or text editor.
while support for undo can be implemented with an unbounded stack, many applications provide only limited
support for such an undo history, with a fixed-capacity stack. When push is invoked with the stack at full
capacity, rather than throwing a Full exception, a more typical semantic is to accpet the pushed element at
the top while "leaking" the oldest element from the bottom of the stack to make room. Give an implementation
of such a LeakyStack abstraction, using a circular array with appropiate storage capacity. This class should
have a public interface similar to the bounded-capacity stack in Exercise C6-16, but with the desired leaky
semantics when full.
"""
from ArrayStack import Full, Empty
class LeakyStack():
    def __init__(self, maxlen=None):

        self._maxlen = maxlen
        self._data = [None] * (maxlen if maxlen != None else 10)
        self._top = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""

        return self._size == 0

    def top(self):
        return self._data[self._top]


    def push(self, element):
        """Insert an element at the top of the stack."""

        capacity = len(self._data)
        if self.is_empty():
            self._data[0] = element
            self._top = 0
        
        else:
            self._top = (self._top + 1) % capacity
            self._data[self._top] = element

        self._size += 1


    def pop(self):
        """Delete the element at the top of the stack and returns it."""

        capacity = len(self._data)
        if self.is_empty():
            raise Empty("The stack is empty.")

        element = self._data[self._top]
        self._data[self._top] = None
        self._top = (self._top - 1) % capacity
        return element
