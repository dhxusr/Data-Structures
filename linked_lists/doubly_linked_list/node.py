"""
A node class for a doubly linked list
"""

class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__= "_element", "_next", "_prev"

    def __init__(self, element, next, prev):

        self._element = element
        self._next = next
        self._prev = prev



