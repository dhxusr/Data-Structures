"""
Design an ADT for a two-color, double-stack ADT that consists of two stacks-one "red" and one "blue" and has
as its operations color-coded versions of the regular stack ADT operations. For example, this ADT should support
both a red push operation and a blur push operation. Give an efficient implementation of this ADT using a single
array whose capacity is set at some value N that is assumed to always be larger tahn the sizes of the red and blue
stacks combined.
"""

class TwoColorStack:

    def __init__(self, N):

        self._array = [None] * N
        self._top_blue = N
        self._top_red = -1
        self._size = 0


    def __len__(self):
        return self._size

    
    def _push(self, element, side):
        
        if self._top_red + 1 == self._top_blue:
            raise Full("The stack is full.")

        top = self._top_blue-1 if side == "blue" else self._top_red+1
        self._array[top] = element
        self._size += 1
        
        if side == "blue":
            self._top_blue = top

        else:
            self._top_red = top
        

    def _pop(self, side):

        if self.is_empty():
            raise Empty("The stack is empty.")

        top = self._top_blue if side == "blue" else self._top_red

        element = self._array[top]
        self._array[top] = None
        self._size -= 1

        if side == "blue":
            self._top_blue += 1

        else:
            self._top_red -= 1

        return element


    def _top(self, side):
        top = self._top_blue if side == "blue" else self._top_red

        if top == -1 or top == len(self._array):
            print("There's no element in that stack.")

        return self._array[top]


    def push_blue(self, element):
        """insert an element in the blue stack."""   
        self._push(element, "blue")


    def push_red(self, element):
        """Insert an element in the red stack."""
        self._push(element, "red")

    def pop_blue(self):
        """Deletes and return the last value in the blue stack."""
        return self._pop("blue")

    def pop_red(self):
        """Delete and return the last value in the red stack."""
        return self._pop("red")

    def top_blue(self):
        """Return the value in the top of the blue stack."""
        return self._top("blue")

    def top_red(self):
        """Return the value in the top fo the red stack."""
        return self._top("red")

    def is_empty(self):
        """Return True if the stack is empty. False otherwise."""
        return self._size == 0


class Full(Exception):
    """Raise if the stack is full."""

class Empty(Exception):
    """Raise if the stack is empty."""

if __name__ == "__main__":

    stack = TwoColorStack(10)

    print("Testing both sides.")
    for i in range(6):
        stack.push_blue(i+5)

    for i in range(4):
        stack.push_red(i+1)

    print(f"top blue must be 10. is: {stack.top_blue()}")
    print(f"top red must be 4. is: {stack.top_red()}")

    print('-' * 20)
    print("Testing pop.")
    print(stack._array)
    print("poping blue side...")
    print(f"must be 10. is: {stack.pop_blue()}")
    print(f"top must be 9. is: {stack.top_blue()}")

    print("poping red side...")
    print(f"must be 4. is: {stack.pop_red()}")
    print(f"top must be 3. is: {stack.top_red()}")

    print("more poping...")    
    stack.pop_blue()
    stack.pop_red()
    stack.pop_blue()
    print(stack._array)
    print('-'* 20)
    print("testing full.")
    print("pushing in red side...")
    for i in range(5):
        stack.push_red(i)

    try:
        stack.push_blue(9)

    except Full as err:
        print(err)

    print(stack._array)    
    print('-'* 20)
    print("Testing full filled the stack by one side")
    print("pushing in the blue side...")

    stack = TwoColorStack(10)
    try:
        for i in range(11):
            stack.push_blue(i)

    except Full as err:
        print(err)
    stack.top_red()
    print(stack._array) 
    print("All test passes...")
