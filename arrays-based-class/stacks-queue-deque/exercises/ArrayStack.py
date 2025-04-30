"""
Modify the ArrayStack implementation so that the stack's capacity is limited to maxlen elements, where maxlen
is an optional parameter to the constructor (that defaults to None). If push is called when the stack is at
full capacity, throw a Full exception.
    
"""

class ArrayStack:
    def __init__(self, maxlen=None):

        self._maxlen = maxlen
        self._data = [None] * maxlen if maxlen != None else []
        self._top = -1
        
    def __len__(self):
        return len(self._data)

    def push(self, value):
        if self._maxlen == self._top + 1:
            raise Full("The stack is full.")

        self._top += 1
        if self._maxlen:
            self._data[self._top] = value

        else:
            self._data.append(value)
            
    def pop(self):
        if self.is_empty():
            raise Empty("The stack is empty.")

        item = self._data[self._top]
        if self._maxlen:
            self._data[self._top] = None
        else:
            self._data.pop()
            
        self._top -= 1
        return item

    def top(self):
        if self.is_empty():
            raise Empty("The stack is empty.")
        return self._data[self._top]
    
    def is_empty(self):
        return self._top == -1

    def p(self):
        print(self._data[:self._top + 1])
        
class Empty(Exception):
    """Raise if a container is empty."""

class Full(Exception):
    """Raise if a container is full."""
