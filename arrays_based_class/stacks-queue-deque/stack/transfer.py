"""
Show how to use the transfer function, described in R6-3 and two temporary stacks, to replace the contents
of a given stack S with those same elements, but in reversed order.
    
"""

import ArrayStack as Stack

"""
implement a function with signature transfer(S, T) that transfers all elements from stack S onto stack T, so
that the element that starts at the top of S is the first to be inserted onto T, and the element at the bottom
of S ends up at the top of T
"""

def transfer(S: Stack.ArrayStack, T: Stack.ArrayStack) -> Stack.ArrayStack | None:
    """Transfer all elements from S to T, reversing their order. Stops if T becomes full."""
   
    if not isinstance(S, Stack.ArrayStack) or not isinstance(T, Stack.ArrayStack):
        raise TypeError("Invalid argument type. must be 'Stack'")

    if S.is_empty():
        print("The stack is empty.")
        return 
    
    try:
        while not S.is_empty():
            T.push(S.pop())

    except Stack.Full:
        pass



if __name__ == "__main__":

    s = Stack.ArrayStack(5)
    t = Stack.ArrayStack(5)
    
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    print("s top: ",s.top())
    s.p()
    transfer(s, t)
    t.p()
    print("t top",t.top())
    
