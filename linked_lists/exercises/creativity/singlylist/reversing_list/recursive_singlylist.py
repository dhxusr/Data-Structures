"""
Give a recursive implementation of a singly list class, such that an instance of a nonempty list stores its
first element and a reference to a list of remaining elements.
"""

class recursiveList:

    def __init__(self):

        self._first = None
        self._remaining_elements = None
        

    def is_empty(self):
        return self._first is None


    def __len__(self):

        if self.is_empty():
            return 0

        return 1 + len(self._remaining_elements)
            
    def add_element(self, element):
        """Inser an element at the end of the list."""

        if self.is_empty():
            self._first = element
            self._remaining_elements = recursiveList()

        else:
            self._remaining_elements.add_element(element)


if __name__ == "__main__":

    rl = recursiveList()

    for i in range(5):
        rl.add_element(i+1)
    
    print(len(rl))




"""
What is this?
Is a singly list implemented recursively.

How it works?
Each list instance is like a node, keep the value and is connected to the rest of the elements.
This is recursive because each list think that is connected to the rest of the elements, but actually they
are connected to other lists that has only one element.

at the time we insert an element the list is like pass the tasks to the rest of the team until one has storage

What i learned?
I learned that we can connect nodes in a recursive way, not just traversing them
"""
