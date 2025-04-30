
"""
Give an array-based implementation of a double-ended queue supporting all of the public behaviors shown in
table 6.4 for the collections.deque class, including use of the maxlen optional parameter. When a length-limited
deque is full, provide semantics similar to the collections.deque class, whereby a call to insert an element on
one end of a deque causes an element to be lost from the opposite side.
"""

"""
Methods to implement:

- appendleft: add to the beginnig
- append: add to end
- popleft: remove from beginning.
- pop: remove from end
- D[0]: access first element
- D[-1]: access last element
- D[index]: access arbitraty entry by index
- D[index] = j: modify arbitrary entry by index.
- clear: clear all contents
- remove: remove first matching element.
- count: count number of matches for e
"""

from ArrayDeque import ArrayDeque 
from ArrayStack import Full, Empty

class CollectDeque(ArrayDeque):

    def __init__(self, maxlen: int | None = None):
        super().__init__(maxlen)
        

    def __len__(self):
        return len(self)


    def __getitem__(self, i):
        i = self._available_index(i)

        if i == False:
            raise IndexError

        return self._data[i]


    def __setitem__(self, i, value):

        i = self._available_index(i)
        if i == False:
            raise IndexError

        self._data[i] = value
        
    def appendleft(self, element):
        """add to the beginning."""
        try:
            self.add_first(element)

        except Full:
            self.delete_last()
            self.add_first(element)

    def append(self, element):
        """add to the end."""
        try:
            self.add_last(element)

        except Full:
            self.delete_first()
            self.add_last(element)

            
    def pop(self):
        """remove from the end."""
        return self.delete_last()


    def popleft(self):
        """remove from the beginning."""
        return self.delete_first()


    def rotate(self, k: int):
        """Circularly shift rightward k steps."""
        self._rotate(k)


    def clear(self):
        """Clear all contents."""
        self._data = [None] * len(self._data)
        self._size = 0
        self._first = 0


    def remove(self, element):
        """Remove the first matching element."""

        capacity = len(self._data)
        last = (self._first + self._size - 1) % capacity
        idx = self._first

        if element in self._data:
            while self._data[idx] != element:
                idx = (idx + 1) % capacity

            self._data[idx] = None
            self._size -= 1
    
            if idx == self._first:
                self._first = (self._first + 1) % capacity

            elif idx != last:
            # moving the elements after idx
                to_move = capacity - idx
                self._move_elements(idx, to_move)
                

    def count(self, element):
        """Count number of matches for element."""

        return self._data.count(element)


    def _available_index(self, i):

        # if i is a negative index, converting it in the corresponding positive index.
        if i < 0:
            i = i + self._size

        if 0 > i > self._size:
            return False

        return (self._first + i) % len(self._data)


    def _move_elements(self, idx, to_move):

        length = len(self._data)
        for _ in range(to_move):
            next = (idx + 1) % length
            self._data[idx] = self._data[next]
            self._data[next] = None
            idx = next
