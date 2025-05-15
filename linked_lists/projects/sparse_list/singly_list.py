"""
Implementation of a Singly Linked List ADT

methods:

- add_first: add an element at the front of the list.
- add_last: add an element at the back of the list.
- add_between: add an element between two other nodes.
- delete: delete a given node.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


class SinglyList:

    @dataclass
    class _Node:
        element: any
        next: Optional[_Node] = None 


    class ListIter:

        def __init__(self, first) -> None:
            self._first = first


        def __iter__(self):
            return self


        def __next__(self):

            if self._first is None:
                raise StopIteration

            element = self._first.element
            self._first = self._first.next
            return element


    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0


    def __len__(self) -> int:
        return self._size


    def __iter__(self):
        return self.ListIter(self._head)

    
    def __str__(self) -> str:

        data = " ".join(
            e for e in self
        )

        return data


    def _find_prev(self, node) -> _Node | None:
        """search and return the prev node of node.
        return None if not exists."""

        if not node is self._head:
            current_node = self._head
            while current_node is not None:

                if current_node.next is node:
                    return current_node

                current_node = current_node.next

        return None
            

    def add_after(self, element, node) -> _Node:
        """insert an element just after the given node."""

        if not isinstance(node, self._Node):
            raise TypeError("Invalid type argument. must be a node")

        new_node = self._Node(element, node.next)
        node.next = new_node
        self._size += 1

        if node is self._tail:
            self._tail = new_node

        return new_node

    
    def add_first(self, element) -> _Node:
        """Insert an element at the front of the list."""
        
        new_node = self._Node(element, self._head)
        self._head = new_node
        self._size += 1

        if self._size == 1:
            self._tail = new_node

        return new_node


    def add_last(self, element) -> _Node:
        """Insert an element at the back of the list."""

        if self._size == 0:
            new_node = self._Node(element)
            self._head = new_node
            self._tail = new_node        
            self._size += 1

        else:
            new_node = self.add_after(element, self._tail)

        return new_node

            
    def delete(self, node):
        """Delete and return the element at the given node."""

        if self._size == 0:
            return None

        prev_node = self._find_prev(node)

        if node is self._head:
            self._head = node.next

        if node is self._tail:
            self._tail = prev_node

        if prev_node is not None:
            prev_node.next = node.next

        node.next = None
        return node.element            

        
