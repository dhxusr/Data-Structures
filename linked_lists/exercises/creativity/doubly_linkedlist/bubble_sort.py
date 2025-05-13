"""
Implement a bubble-sort function that takes a Positional list as a parameter. What is the running time of this
algorithm, assuming the positional list is implemented with a doubly linked list?.
"""

class _Node:
    """Lightweight, nonpublic class for storing a doubly linked node."""
    __slots__ = "_element", "_next", "_prev"

    def __init__(self, element, next, prev):

        self._element = element
        self._next = next
        self._prev = prev


class _DoublyLinkedBase:

    def __init__(self):

        self._header = _Node(None, None, None)
        self._trailer = _Node(None, None, None)
        self._size = 0

        #Conecting Sentinels
        self._header._next = self._trailer
        self._trailer._prev = self._header


    def __len__(self):
        return self._size


    def is_empty(self):
        """Return True if the list is empty. False otherwise."""
        return self._size == 0


    def _insert_between(self, element, predecessor, successor):
        """Add element between two existing nodes and return new node."""

        new_node = _Node(element, successor, predecessor)
        predecessor._next = new_node
        successor._prev = new_node

        self._size += 1
        return new_node


    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""

        # getting node's neighbors
        predecessor = node._prev
        successor = node._next

        # removing node from the list
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element

        # deprecating the node
        node._prev = node._next = node._element = None

        return element
        

    def _link_between(self, node, prev, next) -> None:
        """Link a given node between prev and next"""

        #prev
        prev._next = node
        node._prev = prev

        #next
        node._next = next
        next._prev = node

    def reverse(self):
        """Reverse the order of the list."""

        last_node = self._trailer._prev
        current_node = self._header._next

        
        while current_node is not last_node:

            current_node._next, current_node._prev = current_node._prev, current_node._next
            current_node = current_node._prev

        self._header, self._trailer = self._trailer, self._header


class Position:

    def __init__(self, node, lst):

        self._node = node
        self._list = lst


    def __eq__(self, other):
        return type(self) is type(other) and self._node is other._node


    def __ne__(self, other):
        return not (self == other)

    
    def element(self):
        """Return the element in this position."""

        return self._node._element


class PositionalList(_DoublyLinkedBase):

    class PositionalIterator:

        def __init__(self, data) -> None:
            self._data = data
            self._current_position = data.first()


        def __next__(self):

            if self._current_position is None:
                raise StopIteration

            element = self._current_position.element()
            self._current_position = self._data.after(self._current_position)

            return element


        def __iter__(self):
            return self



    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""

        return self.PositionalIterator(self)

    def __reversed__(self):
        """Generate a backward iteration of the elements of the list."""    

        current = self.last()
        while current is not None:
            yield current.element()
            current = self.before(current)


    def is_empty(self):
        """Return True if the list does not contain any elements."""

        return self._size == 0


    def _validate_position(self, position):
        """Validate if the position is valid."""

        if position._list is not self:
            raise ValueError("This position is invalid for this list.")

        if not isinstance(position, Position):
            raise TypeError("must be proper Position type.")

        if position._node._next is None:
            raise ValueError("position is no longer valid.")
            
        return position._node


    def _meet(self, left_node, right_node):
        """Return True if the nodes are next or in the same position."""

        if (left_node is right_node or
            left_node._next is right_node or
            right_node._prev is left_node):
            return True

        return False


    def _unlink_node(self, node):
        """unlink the given node."""

        prev_node = node._prev
        next_node = node._next

        if (prev_node is None or
            next_node is None):
            raise ValueError(
                "The given node has no appropieate links."
            )
        
        prev_node._next = next_node
        next_node._prev = prev_node
        node._next = None
        node._prev = None


    def _link_node(self, node, prev=None, next=None):
        """links the given node with prev and next."""

        node._next = next
        node._prev = prev

        if prev is not None:
            prev._next = node

        if next is not None:
            next._prev = node


    def first(self):
        """Return the position of the first element of the list, or None if empty."""

        if self.is_empty():
            return None

        return Position(self._header._next, self)


    def last(self):
        """Return the position of the last element of the linst, or None if empty."""

        if self.is_empty():
            return None

        return Position(self._trailer._prev, self)


    def before(self, position: Position):
        """Return the position of the list immediatly before position, or None if position is the first position"""

        node = self._validate_position(position)
        
        if node._prev is self._header:
            return None
        
        return Position(node._prev, self)


    def after(self, position: Position):
        """Return the position of the list immediatly after position, or None if position is the last position."""

        node = self._validate_position(position)
        if node._next is self._trailer:
            return None

        return Position(node._next, self)


    def add_first(self, element):
        """Insert a new element at the front of the list, returning the position of the new element."""

        new_node = self._insert_between(element, self._header, self._header._next)
        return Position(new_node, self)


    def add_last(self, element):
        """Insert a new element at the back of the list, returning the position of the new element."""

        #new_node = self._insert_between(element, self._trailer._prev, self._trailer)
        #return Position(new_node, self)

        if self.is_empty():
            position = self.add_first(element)

        else:
            position = self.add_after(self.last(), element)

        return position

        
    def add_before(self, position, element):
        """Insert a new element just before position in the list, returning the position of the new element."""

        #check if the position is valid
        node = self._validate_position(position)
        #new_node = self._insert_between(element, node._prev, node)
        #return Position(new_node, self)

        if position == self.first():
            new_position = self.add_first(element)

        else:
            prev_position = Position(node._prev, self)
            new_position = self.add_after(prev_position, element)

        return new_position

    def add_after(self, position, element):
        """Insert a new element just after position in the list, returning the positin of the new element."""

        #check if the position is valid
        node = self._validate_position(position)

        new_node = self._insert_between(element, node, node._next)
        return Position(new_node, self)


    def replace(self, position, element):
        """Replace the element at position with element, returning the element formerly at position p."""

        # check if the position is valid
        node = self._validate_position(position)

        # replacing the Node
        old = node._element
        node._element = element
        return old


    def delete(self, position):
        """Remove and return the element at position from the list, invalidating the position."""

        #check if the position is valid
        node = self._validate_position(position)

        return self._delete_node(node)


    def max(self):
        """Return the maximun element in the list."""
        if self.is_empty():
            return None

        left = self.first()._node
        right = self.last()._node
        max = left._element if left._element > right._element else right._element
        
        while True:

            if left._element > max:
                max = left._element

            elif right._element > max:
                max = right._element

            elif self._meet(left, right):
                return max

            else:
                left = left._next
                right = right._prev


    def find(self, element):
        """Return the position of the (first occurrence of) element in the list (or None if not found)."""
        
        current_position = self.first()
        last_position = self.last()

        if current_position is None:
            return None

        while current_position.element() != element:

            if current_position == last_position:
                return None

            current_position = self.after(current_position)

        return current_position


    def find_recursive(self, element, position):
        """Return the position of the first occurrence of element in the list or None if not found."""

        if position is None:
            return None

        if position.element() == element:
            return position

        return self.find_recursive(element, self.after(position))
        

    def move_to_front(self, position):
        """Move the element at position to the first position"""

        node_to_move = self._validate_position(position)

        if self.is_empty():
            raise Exception("The list is empty.")
        
        if position == self.first():
            raise ValueError("The element is currently in the first position.")

        self._unlink_node(node_to_move)

        first = self.first()._node
        header = first._prev
        self._link_node(node_to_move, header, first)

        
    def swap(self, position1, position2) -> None:
        """exchange the node in position1 to position2 and
        node in position2 to position1"""

        node1 = self._validate_position(position1)
        node2 = self._validate_position(position2)

        if node1 is node2:
            raise ValueError("Positions are the same.")

        if (node1._next is node2 or
            node2._next is node1):

            left_node = node1 if node1._next is node2 else node2            
            right_node = node2 if left_node is node1 else node1
            prev_left = left_node._prev

            self._link_node(left_node, right_node, right_node._next)
            prev_left._next = right_node
            right_node._prev = prev_left            
        
        else:
            prev_node1 = node1._prev
            next_node1 = node1._next

            self._link_node(node1, node2._prev, node2._next)
            self._link_node(node2, prev_node1, next_node1)




def bubble_sort(positional_list) -> None:

    # any_change variable is like a flag that allow the computer to check if there have been
    # any change in the current iteration. if not, elements are sorted.
    
    any_change = False
    current = positional_list.first()
    while True:

        if current == positional_list.last():
            if not any_change:
                return 

            any_change = False
            current = positional_list.first()
        
        else:

            after = positional_list.after(current)

            if current.element() > after.element():
                positional_list.swap(current, after)
                any_change = True             

            else:
                current = positional_list.after(current)


def print_list(lst):
    for i in lst:
        print(i, end=' ')
    print(' ')                
            
if __name__ == "__main__":

    pl = PositionalList()

    for i in range(5):
        pl.add_first(i+1)

    print_list(pl)
    bubble_sort(pl)

    print("sorted")
    print_list(pl)
    
