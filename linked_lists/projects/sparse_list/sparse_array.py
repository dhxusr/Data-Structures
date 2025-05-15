"""
An array A is sparse if most of its entries are emtpy. A list cab used to implement such an array efficiently.
In particular, for each nonempty cell A[i], we can store an entry (i, e) in L, where e is the element stored
at A[i]. This approach allows us to represent A using O(m) storage, where m is the number of nonempty entries
i A.

Provide such a SparseArray class that minimally supports methods __getitem__(i) and __setitem__(i, e) to
provide standard indexing operations. Analyze the effiency of these methods.
"""

from singly_list import SinglyList


class SparseArray(SinglyList):



    def __str__(self) -> str:

        string = " ".join(
            str(data[1]) for data in self
        )

        return string


    def __getitem__(self, idx):
        """Get the value of Array at index idx."""

        node = self._find_node_at(idx)
        if node:
            return node.element[1]

        return None


    def __setitem__(self, idx, element):
        """Set or add an element at Array[idx]."""

        if idx < 0:
            idx += self._size
            if idx < 0:
                raise ValueError("invalid index.")

        if self.is_empty():
            self.add_first([idx, element])

        else:

            prev = self._find_lower_than(idx)
            node = prev.next

            if node:
                if element is None:
                    self.delete(node)
                else:
                    node.element[1] = element

            elif element is not None:

                element = [idx, element]

                if idx < self._head.element[0]:
                    self.add_first(element)

                elif idx > self._tail.element[0]:
                    self.add_last(element)

                else:
                    self.add_after(element, prev)
                


    def _find_node_at(self, idx):
        """Search and return the node at index idx.
        return None if doesn't exists."""

        current = self._head

        while current is not None:
            current_index = current.element[0]

            if current_index == idx:
                return current

            if current_index > idx:
                return None

            current = current.next


    def _find_lower_than(self, idx):
        """search for an index lower than idx and return the node."""

        current = self._head
        prev = None

        while current is not None:

            if current.element[0] > idx:
                break

            prev = current
            current = current.next  

        return prev

    
    def is_empty(self):
        """Return True if the array is empty."""

        return self._size == 0



from random import randint
if __name__ == "__main__":

    array = SparseArray()

    print("Testing. :33333333")
    print("Testing set item")

    for i in range(1, 6):

        array[i] = i+1

    print(array)
    print('-'*20)
    print("testing set item at arbitrary index.")
    idx = randint(1, 20)
    print(f"setting 44 at index: {idx}")
    array[idx] = 44
    
    idx = randint(1, 20)
    print(f"setting 99 at index: {idx}")
    array[idx] = 99

    idx = randint(1, 20)
    print(f"setting 66 at index: {idx}")
    array[idx] = 66

    print(array)
    print('-'*20)
    print("Testing deleting some elements. hihihhih")

    idx = randint(1, 5)
    print(f"deleting at index: {idx}")
    array[idx] = None

    idx = randint(1, 5)
    print(f"deleting at index: {idx}")
    array[idx] = None

    print(array)
    print('-'*20)
    print("Testing adding some values at the beginning and at the end.")
    print("setting 55 at the beginning.")
    array[0] = 55
    print("setting 22 at the end.")
    array[21] = 22
    print(array)

    print('-'*20)
    print("Testing get item.")
    print(array)
    print(f"item at index 0. must be: 55. is: {array[0]}")
    idx = randint(1, 20)
    print(f"item at index {idx}. is: {array[idx]}")
    idx = randint(1, 20)
    print(f"item at index {idx}. is: {array[idx]}")
    
    
