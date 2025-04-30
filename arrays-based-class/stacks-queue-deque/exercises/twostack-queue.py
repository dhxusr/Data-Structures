"""
Describe how to implement the queue ADT using two stacks as instance variables, such that all queue operations
execute in amortized O(1) time. give a formal proof of the amortized bound.
"""

from ArrayStack import ArrayStack, Empty, Full

class TwoStackQueue:
    def __init__(self):

        self._enque_stack = ArrayStack(10)
        self._deque_stack = ArrayStack(10)

        self._size = 0
        self._first = None


    def __len__(self):
        return self._size


    def first(self):
        return self._first
    

    def is_empty(self):
        return self._size == 0


    def enqueue(self, element):
        """insert elements at the top of the stack, always constant time untill resize."""

        if self.is_empty():
            self._first = element
            
        try:
            self._enque_stack.push(element)

        except Full:
            capacity = self._size * 2
            self._resize(capacity)
            self._enque_stack.push(element)
            
        self._size += 1


    def dequeue(self):
        if self.is_empty():
            raise Empty("The queue is empty.")

        # reversed the stack to get the oldest element
        if self._deque_stack.is_empty():
            self._move_to("deque")
                        
        removed = self._deque_stack.pop() # removing the "first" element of the queue
        self._first = self._deque_stack.top() if not self._deque_stack.is_empty() else None
        self._size -= 1

        return removed


    def _resize(self, capacity):

        new_en = ArrayStack(capacity)
        new_de = ArrayStack(capacity)
        
        for _ in range(self._size):
            new_en.push(self._enque_stack.pop())
            new_de.push(self._deque_stack.pop())
    
        self._enque_stack = ArrayStack(capacity)
        self._deque_stack = ArrayStack(capacity)

        for _ in range(self._size):
            self._enque_stack.push(new_en.pop())
            self._deque_stack.push(new_de.pop())


    def _move_to(self, stack: str):
        """Move the elements in the enque/deque stack to the other stack."""

        if stack == "deque":
            while not self._enque_stack.is_empty():
                self._deque_stack.push(self._enque_stack.pop())

        else:
            while not self._deque_stack.is_empty():
                self._enque_stack.push(self._deque_stack.pop())

                
"""
Describe how to implement the double-ended queue ADT using two stacks as instance variables. What are the
running times of methods.
"""

class TwoStackDeque(TwoStackQueue):

    def __init__(self):

        super().__init__()
        self._last = None


    def last(self):
        """Return the first element from the back."""
        if self.is_empty():
            raise Empty("The deque is empty.")

        return self._last


    def add_first(self, element):
        """Insert an element in the front of the stack."""
        # deque stack is the "front" part of the queue

        if self.is_empty():
            self._last = element

        try:
            self._deque_stack.push(element)

        except Full:
            self._resize(2 * len(self._deque_stack))
            self._deque_stack.push(element)

        self._first = element
        self._size += 1


    def add_last(self, element):
        self.enqueue(element)
        self._last = element

    
    def delete_last(self):
        """Delete the last element from the back of the queue.
           Raise an Empty error if the stack is empty."""

        if self.is_empty():
            raise Empty("The Deque is empty.")

        if self._enque_stack.is_empty():
            self._move_to("enque") #moving from front to back stack

        removed = self._enque_stack.pop()
        self._last = self._enque_stack.top() if not self._enque_stack.is_empty() else None
        self._size -= 1
        return removed
        

    def delete_first(self):
        return self.dequeue()




def test_queue_with_two_stacks():
    print("Starting tests...")

    q = TwoStackDeque()  # usa el nombre de tu clase

    # Test insert in the front
    q.add_first(10)
    q.add_first(20)
    q.add_first(30)
    q.add_first(40)
    q.add_first(50)

    assert q.first() == 50, "First element should be 50"

    #test inserting in the back
    q.add_last(60)
    q.add_last(70)
    q.add_last(80)
    q.add_last(90)
    q.add_last(100)

    assert q.last() == 100, "Last element should be 100"


    # Test deleting from the front
    assert q.delete_first() == 50, "Should return 50"
    assert q.first() == 40, "First should now be 40"
    assert q.delete_first() == 40, "Should return 40"
    assert q.delete_first() == 30, "Should return 30"

    # Test empty resize
    for i in range(5):
        q.add_first(i)
        
    assert q.first() == 4, "First should be 4"
    # Test mix
    q.add_last(5)
    q.add_first(6)
    assert q.delete_last() == 5
    q.add_last(7)
    assert q.delete_first() == 6
    assert q.delete_first() == 4

    print("All tests passed!")

if __name__ == "__main__":
    test_queue_with_two_stacks()
