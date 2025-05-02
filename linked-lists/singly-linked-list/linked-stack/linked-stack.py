"""
Implementing a Stack with a Single Linked List
"""

class _Node:
    """Lightweight, nonpublic class for storing a singly linked node."""
    __slots__ = "_element", "_next"

    def __init__(self, element, next):

        self._element = element
        self._next = next

    def element(self):
        """Return the element of the node."""
        return self._element

    def next(self):
        """Return the next element of the Node."""
        return self._next


class LinkedStack:

    def __init__(self):

        self._top = None
        self._size = 0
        

    def __len__(self):
        return self._size


    def top(self):
        """Return the first element in the stakc."""

        if self._top == None:
            raise Empty("The stack is empty.")

        return self._top.element()


    def is_empty(self):
        """Return True if the stack is empty. False otherwise."""
        return self._size == 0


    def push(self, element):
        """Insert element at the top of the stack."""

        self._top = _Node(element, self._top)
        self._size += 1


    def pop(self):
        """Delete and return the first element in the stack."""
        if self.is_empty():
            raise Empty("The stack is empty.")

        element = self._top.element()
        self._top = self._top.next()
        self._size -= 1
        return element


class Empty(Exception):
    """Return Empty exception."""


if __name__ == "__main__":

    stack = LinkedStack()

    print("testing empty.")
    try:
        stack.pop()
        stack.top()
    except Empty as err:
        print(err)

    print('-'*20)
    print("Testing push.")
    print("pushing number 1...")
    stack.push(1)
    print(f"top must be 1, is: {stack.top()}")
    print("pushing...")
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(f"top must be 5, is: {stack.top()}")
    print('-'*20)
    print("testing pop.")
    print("poping...")
    print(f"pop must be 5, is: {stack.pop()}")

    print(f"pop must be 4, is: {stack.pop()}")
    print(f"pop must be 3, is: {stack.pop()}")
    print(f"pop must be 2, is: {stack.pop()}")
    print(f"top must be 1. is: {stack.top()}")
    stack.push(4)
    print(f"len must be 2. is: {len(stack)}")
    print('-'*20)
    print("pushing untill empty...")
    while not stack.is_empty():
        stack.pop()

    print("testing empty.")
    print(f"The stack is empty? must be true. is: {stack.is_empty()}")
    print("All test passes.")
