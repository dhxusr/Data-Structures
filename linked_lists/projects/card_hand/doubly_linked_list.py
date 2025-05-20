"""
Basic implementation of a Doubly Linked List
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
            

        
if __name__ == "__main__":
    
    lista = _DoublyLinkedBase()

    header = lista._header
    trailer = lista._trailer

    for i in range(5):
        lista._insert_between(i+1, trailer._prev, trailer)

    lista.reverse()
    current = header._next
    while current._next is not None:
        print(current._element)
        current = current._next

    
