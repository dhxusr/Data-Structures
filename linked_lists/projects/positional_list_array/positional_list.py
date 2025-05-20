"""
Although we have used a doubly linked list to implement he positional list ADT, it is possible to support      
the ADT with an array-based implementation. The key is to use the composition pattern and store a sequence
of position items, where each item stores an element as well as that element's current index in the array.
Whenever an element's place in the array is changed, the recorded index in the position must be updated to match
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


class PositionalList:

    @dataclass
    class Position:
        element: any
        index: int | None
        _list: Optional[PositionalList] = None 

        def __eq__(self, other):

            return (type(other) == type(self) and
                    self.element == other.get_element() and
                    self.index == other.get_index() and
                    self._list is other.get_list())

        def __ne__(self, other):
            return not (self == other)

        def change_element(self, new_element) -> None:
            self.element = new_element

        def change_index(self, new_index) -> None:
            self.index = new_index

        def get_element(self):
            return self.element

        def get_index(self) -> int:
            return self.index

        def get_list(self):
            return self._list

        def deprecate(self):
            self.element = None
            self.index = None
            self._list = None


    def __init__(self) -> None:

        self._data = []
        self._size = 0

    #---------- Magic methods ----------#
    def __iter__(self):

        for pos in self._data:
            yield pos.get_element()

    def __str__(self) -> str:

        data = " ".join(
            str(pos) for pos in self
        )
        return data


    #--------------- Utilities ---------------#

    def _validate_position(self, position) -> int:
        """Check if a given position is valid and return its index.
        if not return error."""

        if not isinstance(position, self.Position):
            raise TypeError("Invalid argument type.")

        if position.get_list() is not self:
            raise ValueError("Invalid given postion. is not from this list.")    

        return position.get_index()


    def _change_index_from(self, index, operator):
        """change the index of each position."""

        if operator == '+':
            for i in range(index, len(self._data)):
                pos_index = self._data[i].get_index()
                self._data[i].change_index(pos_index+1)
        else:
            for i in range(index, len(self._data)):
                pos_index = self._data[i].get_index()
                self._data[i].change_index(pos_index-1)
        

        
    #-------------------- Public Methods --------------------#

    def is_empty(self) -> bool:
        """Return True if empty."""

        return self._size == 0


    def first(self) -> Position | None:
        """Return the first position of the list.
        None if empty."""

        if self.is_empty():
            return None

        return self._data[0]


    def last(self) -> Position | None:
        """Return the last position of the list.
        return None if empty."""

        if self.is_empty():
            return None

        return self._data[-1]


    def after(self, position) -> Position | None:
        """Return the position just after the given position.
        return None if the given position is the last."""

        index = self._validate_position(position) + 1
        if position == self.last():
            return None

        return self._data[index]        


    def before(self, position) -> Position | None:
        """Return the position just before the given position .
        return None if the given position is the first."""

        index = self._validate_position(position) - 1
        if position == self._data[0]:
            return None

        return self._data[index]


    def add_first(self, element) -> Position:
        """Add an element at the front of the list."""

        new_position = self.Position(element, 0, self)
        self._data.insert(0, new_position)
        self._change_index_from(1, '+')
        self._size += 1

        return new_position


    def add_last(self, element) -> Position:
        """Add an element at the back of the list."""

        new_position = self.Position(element, self._size, self)
        self._data.append(new_position)
        self._size += 1

        return new_position


    def add_before(self, position, element) -> Position:
        """Add an element just before the given position."""

        index = self._validate_position(position)
        new_position = self.Position(element, index, self)
        self._data.insert(index, new_position)
        self._change_index_from(index+1, '+')
        self._size += 1

        return new_position


    def add_after(self, position, element) -> Position:
        """Add an element just after the given position."""

        index = self._validate_position(position)
        new_position = self.Position(element, index, self)
        self._data.insert(index+1, new_position)
        self._change_index_from(index+2, '+')
        self._size += 1

        return new_position


    def delete(self, position):
        """Delete and return the element at given position.
        return None if empty."""

        index = self._validate_position(position)
        element = position.get_element()
        self._data.pop(index)
        position.deprecate()
        self._change_index_from(index, '-')
        self._size -= 1

        return element


    def move_to_front(self, position):
        """Move the element of given position to the first position."""

        index = self._validate_position(position)
        self._data.insert(0, self._data.pop(index))
        self._change_index_from(1, '+')


if __name__ == "__main__":

    poslist = PositionalList()

    print("Testing adding elements.")

    print("adding at the front")
    p = poslist.add_first(5)
    poslist.add_first(8)
    poslist.add_first(10)
    print(poslist)
    print('\n')

    print("adding at the end.")
    poslist.add_last(1)
    p2 = poslist.add_last(2)
    poslist.add_last(3)
    print(poslist)

    print('\n')
    print("adding before and after.")
    print(f"adding 99 after index: {p.get_index()}")
    poslist.add_after(p, 99)
    print(poslist)
    print(f"adding 44 before index: {p2.get_index()}")
    p3 = poslist.add_before(p2, 44)

    print(f"adding 55 before index: {p3.get_index()}")
    p4 = poslist.add_after(p3, 55)
    print(poslist)


    print('\n')
    print("deleting elements")
    print("deleting first element.")
    poslist.delete(poslist.first())
    print(poslist)
    print("deleting last element.")
    poslist.delete(poslist.last())
    print(poslist)

    print(f"deleting at index {p.get_index()}")
    poslist.delete(p)
    print(poslist)

    print(f"deleting at index {p2.get_index()}")
    poslist.delete(p2)
    print(poslist)

    print(f"deleting at index {p3.get_index()}")
    poslist.delete(p3)
    print(poslist)

    print('\n')
    print(f"moving to front element at index: {p4.get_index()}")
    poslist.move_to_front(p4)
    print(poslist)
