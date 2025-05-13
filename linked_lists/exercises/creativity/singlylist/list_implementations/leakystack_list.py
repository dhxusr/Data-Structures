"""
Implement a LeakyStack ADT using a singly linked list for storage.

LeakyStack:

- The capacity storage is limited to maxlen elements, where maxlen is an optional parameter to the constructor
(that defaults to None).

- If push is called when the stack is at full capacity, throw a Full exception.

"""

class LinkedLeakyStack:

    class Node:

        def __init__(self, element, next):

            self._element = element
            self._next = next

    def __init__(self, maxlen=None):

        self._top = None
        self._maxlen = maxlen
        self._size = 0


    def __len__(self):

        return self._size


    def is_empty(self):
        """Return True if the stack is empty."""
        
        return self._size == 0


    def top(self):
        """Return the element at the top of the Stack."""

        if self.is_empty():
            raise Empty("The Stack is empty.")

        return self._top._element

    
    def push(self, element):
        """Insert an element in the stack."""

        if self._size == self._maxlen:
            raise Full("The Stack is full of capacity.")

        node = self.Node(element, None)
        node._next = self._top
        self._top = node
        self._size += 1


    def pop(self):
        """Delete and return the element at the top of the stack."""

        if self.is_empty():
            raise Empty("The Stack is empty.")

        node_to_delete = self._top
        self._top = self._top._next

        node_to_delete._next = None
        self._size -= 1
        return node_to_delete._element


class Emtpy(Exception):
    """Return an Empty exception"""

class Full(Exception):
    """Return a Full exception."""


if __name__ == "__main__":

    stack = LinkedLeakyStack(10)
    infinite_stack = LinkedLeakyStack()

    for i in range(10):
        stack.push(i+1)
        infinite_stack.push(i+1)

    try:
        stack.push(11)

    except Full as err:
        print(err)

    infinite_stack.push(11)

    print(stack.top())
    print(infinite_stack.top())












"""
What is this?

How does it works?

Why did i chose this approach

What did i learned?

What would i improve?
"""
