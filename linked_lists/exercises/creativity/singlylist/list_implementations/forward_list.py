"""
Design a forward list ADT that abstracts the operations on a singly linked list.

"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
        element: any
        next: Optional[Node] = None

class SinglyList:

    def __init__(self) -> None:

        self._head = None
        self._tail = None
        self._size = 0


    def __len__(self) -> int:

        return self._size


    def insert_first(self, element) -> None:
        """Insert an element at front of the list."""

        node = Node(element, self._head)
        self._head = node            
        self._size += 1

        if self._size == 1:
            self._tail = node


    def insert_last(self, element) -> None:
        """Insert an element at the back of the list."""

        node = Node(element)

        if self._size == 0:
            self._head = node
        else:
            self._tail.next = node

        self._tail = node
        self._size += 1


    def delete(self):
        """Delete and return the first element."""

        if self._size == 0:
            return None

        node_to_delete = self._head
        self._head = self._head.next
        node_to_delete.next = None
        self._size -= 1

        return node_to_delete.element
        
            

class ForwardList:

    def __init__(self) -> None:

        self.__data = SinglyList()


    def __len__(self):

        return len(self.__data)


    def insert(self, element) -> None:
        """Insert an element at the front of the list."""

        self.__data.insert_first(element)


    def delete(self):
        """Delete and returns the first element in the stack."""

        return self.__data.delete()
    


if __name__ == "__main__":

    forward_list = ForwardList()

    for i in range(5):
        forward_list.insert(i)

    print(forward_list.delete())
    print(forward_list.delete())
    print("len", len(forward_list))
