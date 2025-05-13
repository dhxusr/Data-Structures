"""
Design a circular positional list ADT that abstracts a circularly linked list in the same way that the
positional list ADT abstracts a doubly linked list, with a notion of a designated "cursor" position within
the list. 

methods:
add_first: add element at the fron of the list.
add_last: add element at the back of the list.
before: return the position before the given position.
after: return the position after the given position.
add_after: add an element after the given position.
add_before: add an element before the given position.
first: return the position of the first element in the list.
last: return the position of the last element in the list.
replace: Replace the element at a given position returning the elemnt at position p
delete: remove and return the element at position p
move to front: the element at position to the front.
reversed
iter
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    element: any
    next: Optional[Node] = None


class CircularList:


    def __init__(self) -> None:

        self._tail = None
        self._size = 0


    def __len__(self) -> int:

        return self._size


    #----------------------------- Utilities ------------------------------#

    def _link_node_between(self, node, prev, next) -> None:
        """Insert a Node between two other nodes."""

        prev.next = node
        node.next = next
                

    def _find_prev(self, node) -> Node:
        """Search and return the prev node of the given node."""

        if node.next is node:
            return node

        start = node.next
        while start.next is not node:
            start = start.next

        return start


    def _unlink_node_between(self, node1, node2) -> Node:
        """Unlink and return the node between node1 and node2."""

        unlinked_node = node1.next
        unlinked_node.next = None

        node1.next = node2

        return unlinked_node
        

    #---------------------------- Public methods -----------------------------#
    

    def insert_first(self, element) -> Node:
        """Insert an element at the front of the list.
        return the new node."""

        node = Node(element)

        if self._size == 0:
            node.next = node
            self._tail = node

        else:
            self._link_node_between(node, self._tail, self._tail.next)

        self._size += 1
        return node


    def insert_last(self, element) -> Node:
        """Insert an element at the back of the list.
        return the new node."""

        node = Node(element)

        if self._size == 0:
            node.next = node

        else:
            self._link_node_between(node, self._tail, self._tail.next)

        self._tail = node
        self._size += 1
        return node


    def delete_first(self):
        """Delete and return the first element of the list."""

        if self._size == 0:
            return None

        first = self._tail.next
        first = self._unlink_node_between(self._tail, first.next)

        self._size -= 1
        return first.element
            
            
    def delete_last(self):
        """Delete and returns the last element of the list."""

        if self._size == 0:
            return None

        prev_last = self._find_prev(self._tail)
        last_node = self._unlink_node_between(prev_last, self._tail.next)
        return last_node.element

    
class Position:

    def __init__(self, node, lst) -> None:
        
        self._node = node
        self._lst = lst


    def __eq__(self, other):

        return (type(other) == type(self) and
                self._node is other._node)


    def __ne__(self, other):
        return not (self == other)    

    
    def element(self):
        return self._node.element        



class CircularPositionalList(CircularList):

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""

        current = self.first()
        while current is not None:
            yield current.element()
            current = self.after(current)


    def __len__(self) -> int:
        return self._size

    
    #----------------------  Utilities  -----------------------#

    def _validate_position(self, position) -> Node:

        if position._lst is not self:
            raise ValueError("Invalid Position. is not from this list.")

        if not isinstance(position, Position):
            raise TypeError("must be proper Position type.")

        if position._node.next is None:
            raise ValueError("position is no longer valid.")

        return position._node

    
    #-------------------- Public methods ---------------------#

    def is_empty(self) -> bool:
        """Return True if the list is empty."""

        return self._size == 0


    def first(self) -> Position | None:
        """Return the position of the first element.
        return None if empty."""

        if self.is_empty():
            return None

        return Position(self._tail.next, self)


    def last(self) -> Position | None:
        """Return the position of the last element.
        return None if empty."""

        if self.is_empty():
            return None

        return Position(self._tail, self)


    def before(self, position) -> Position | None:
        """Return the Position emmidiatly before position.
        return None if position is the first position."""

        position_node = self._validate_position(position)
        
        if position == self.first():
            return None

        prev_node = self._find_prev(position_node)    
        return Position(prev_node, self)
        

    def after(self, position) -> Position | None:
        """Return the Position emmidiatly after position.
        return None if position is the last position."""

        position_node = self._validate_position(position)

        if position == self.last():
            return None

        return Position(position_node.next, self)


    def add_first(self, element) -> Position:
        """Insert a new element at the front of the list.
        return the position of the new element."""

        new_node = self.insert_first(element)
        return Position(new_node, self)


    def add_last(self, element) -> Position:
        """Insert a new element at the back of the list.
        return the position of the new element."""

        new_node = self.insert_last(element)
        return Position(new_node, self)


    def add_before(self, element, position) -> Position:
        """Insert a new element just before position.
           return the position of the new element."""

        position_node = self._validate_position(position)

        prev_node = self._find_prev(position_node)
        new_node = Node(element)
        self._link_node_between(new_node, prev_node, position_node)
        self._size += 1

        return Position(new_node, self)


    def add_after(self, element, position) -> Position:
        """Insert a new element just after position.
        return the position of the new element."""

        position_node = self._validate_position(position)

        new_node = Node(element)
        self._link_node_between(new_node, position_node, position_node.next)
        self._size += 1

        return Position(new_node, self)


    def replace(self, element, position) -> Position:
        """Replace the element at position with an element.
        return the element formerly at position."""

        position_node = self._validate_position(position)

        old_element = position_node.element
        position_node.element = element

        return old_element


    def delete(self, position):
        """Remove and return the element at position."""

        position_node = self._validate_position(position)

        if position == self.first():
            element = self.delete_first()

        elif position == self.last():
            element = self.delete_last()

        else:
            prev_node = self._find_prev(position_node)
            self._unlink_node_between(prev_node, position_node.next)

            element = position_node.element
            position_node.element = None
            self._size -= 1

        #deprecating the position
        position._node = None
        position._lst = None

        return element


    def move_to_front(self, position):
        """"Move the element at position given to the first position."""

        # prev node to conect prev node with the next node of the position_node
        # also if position is the last, move the pointer of tail to the prev node.
        position_node = self._validate_position(position)
        prev_node = self._find_prev(position_node)

        first_position = self.first()
        last_position = self.last()

        if position == first_position:
            raise ValueError("The given position is currently the first position.")

        elif position == last_position:
            self._tail = prev_node

        else:
            self._unlink_node_between(prev_node, position_node.next)
            self._link_node_between(position_node, last_position._node, first_position._node)


if __name__ == "__main__":

    pl = CircularPositionalList()

    p = None

    for i in range(5):
        p = pl.add_last(i)
    
    pl.move_to_front(pl.last())

    for i in pl:
        print(i)

    print("first", pl.first().element())



















"""
What is this?

How does it works?

Why did i chose this approach

What did i learned?

What would i improve?
"""
