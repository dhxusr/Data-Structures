"""
To better model a FIFO queue in which entries may be deleted before reaching the front, disgn a PositionalQueue
class that supports the complete queue ADT, yet with enqueue returning a position instance and suport for a new
method, delete(p), that removes the element associated with position p from the queue.
"""

from bubble_sort import _DoublyLinkedBase, _Node, Position, PositionalList

class Empty(Exception):
    """Return an empty exception."""

class PositionalQueue:

    def __init__(self):

        self.__data = PositionalList()


    def __len__(self):

        return len(self.__data)


    def __str__(self):

        data = "["
    
        for pos in self.__data:

            if pos != self.__data.last().element():
                data += f"{pos}, "
                
            else:
                data += f"{pos}]"

        return data 

    
    def is_empty(self):

        return self.__data.is_empty()


    def first(self):
        """Return the first element of the queue."""

        if self.is_empty():
            return Empty("The Queue is empty.")

        return self.__data.first().element()


    def enqueue(self, element):
        """Insert an elenent in the queue.
            return the position of the new element."""

        return self.__data.add_last(element)


    def dequeue(self):
        """Delete and return the first element of the queue."""

        if self.is_empty():
            raise Empty("The Queue is empty.")

        first_position = self.__data.first()
        return self.__data.delete(first_position)


    def delete(self, position):
        """Delete and return the element at the given position."""

        if self.is_empty():
            raise Empty("The Queue is empty.")

        return self.__data.delete(position)


    def rotate(self):
        """Move the first element of the queue to the end of the queue."""    

        if self.is_empty():
            raise Empty("The Queue is empty.")

        if len(self.__data) > 1:
            
            first_node = self.__data.first()._node
            last_node = self.__data.last()._node

            self.__data._unlink_node(first_node)
            self.__data._link_between(first_node, last_node, self.__data._trailer)

        

        
        
def test_enqueue():

    queue = PositionalQueue()
    print("Testing enqueue.")
    print("enqueueing...")

    p = None
    for i in range(10):
        pos = queue.enqueue(i+1)

        if i+1 == 6:
            p = pos

    print(p.element())
    print("First element:", queue.first())
    queue.enqueue(p)
    print("printing queue. :)")
    print(queue)

    
def test_dequeue():

    queue = PositionalQueue()
    print('-'*20)
    print("Testing dequeue.")
    for i in range(5):
        queue.enqueue(i)
    print("queue: ", queue)
    
    print("dequeueing...")
    try:
        for _ in range(len(queue)+1):
            print("element:", queue.dequeue()," deleted.")

    except Empty as err:
        print(err)


def test_delete():

    queue = PositionalQueue()
    print('-'*20)
    print("Testing deleting the element at position pos.")
    pos = None
    for i in range(5):
        p = queue.enqueue(i+1)

        if p.element() == 4:
            pos = p
    print("queue:", queue)    
    print("deleting...")
    print(queue.delete(pos))
    print("printing queue. >:)")
    print(queue)


def test_rotate():

    queue = PositionalQueue()
    emptyq = PositionalQueue()

    for i in range(5):
        queue.enqueue(i+1)
    print('-'*20)
    print("Testing rotate.")
    print("queue:", queue)
    print("rotating")
    queue.rotate()
    print("queue after rotate:", queue)
    print("Testing rotate empty.")

    try:
        emptyq.rotate()

    except Empty as err:
        print(err)


def test():
    test_enqueue()
    test_dequeue()
    test_delete()
    test_rotate()

if __name__ == "__main__":

    test()    


        
