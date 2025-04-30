
"""
Describe how to implement the stack ADT using a single queue as an instance variable, and only constant
addtional local memory within the method bodies. what is the running time of the push(), pop(), and top()
methods for your design.
"""

from ArrayStack import Full, Empty
import ArrayQueue as Queue

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
        
        top = len(self._data) - 2 
        self._data._rotate(top)

        self._top = self._data.dequeue()
        self._data.enqueue(self._top)
        return self._data.dequeue()
