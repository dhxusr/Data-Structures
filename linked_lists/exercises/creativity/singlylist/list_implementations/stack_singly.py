"""
Give a complete implementation of the stack ADT using a singly linked list that includes a header sentinel.
"""


class Node:

    def __init__(self, element, next):

        self.element = element
        self.next = next

class SinglyList:

    def __init__(self):

        self._header = Node(None, None)
        self._size = 0


    def __len__(self):
        return self._size


    def insert(self, element):
        """Insert an element at the front of the list."""

        new_node = Node(element, None)
        new_node.next = self._header.next

        self._header.next = new_node
        self._size += 1

        return new_node


    def delete(self):
        """Delete and return the first element of the list. return None if the list is empty."""

        if self._size == 0:
            return None

        node_to_delete = self._header.next
        self._header.next = node_to_delete.next

        node_to_delete.next = None
        self._size -= 1

        return node_to_delete.element


class Stack:

    def __init__(self, maxlen=None):

        self._data = SinglyList()
        self._maxlen = maxlen
        self._top = None


    def __len__(self):
        return len(self._data)

    
    def is_empty(self):
        """Return True if the stack is empty."""        
        
        return len(self._data) == 0


    def top(self):
        """Return the element at the top of the list."""
        if self.is_empty():
            raise Empty("The stack is empty.")

        return self._top.element


    def push(self, element):
        """Insert an element in the stack."""
        if self._maxlen == len(self._data):
            raise Full("The stack is full of capacity.")
            
        self._top = self._data.insert(element)


    def pop(self):
        """Delete the element at the top of the stack. None if empty."""
        if self.is_empty():
            raise Empty("The stack is empty.")

        element = self._data.delete()
        self._top = self._data._header.next

        return element


class Empty(Exception):
    """Raise an empty exception."""

class Full(Exception):
    """Raise a Full exception."""

def test_stack():
    s = Stack(3)

    # Verifica que está vacío al inicio
    assert s.is_empty()
    assert len(s) == 0

    # Agrega elementos
    s.push(1)
    s.push(2)
    s.push(3)

    assert not s.is_empty()
    assert len(s) == 3
    assert s.top() == 3

    # Extrae elementos
    assert s.pop() == 3
    assert s.pop() == 2
    assert len(s) == 1

    # Elemento restante
    assert s.top() == 1

    # Vacía la pila
    assert s.pop() == 1
    assert s.is_empty()

    # Excepciones esperadas
    try:
        s.pop()
        assert False, "Expected EmptyStackError"
    except Empty:
        pass

    try:
        s.top()
        assert False, "Expected EmptyStackError"
    except Empty:
        pass

    try:
        s.push(1)
        s.push(2)
        s.push(3)
        s.push(4)
        assert False, "Expected FullStackError"
    except Full:
        pass

    print("All tests passed.")

if __name__ == "__main__":
    test_stack()
