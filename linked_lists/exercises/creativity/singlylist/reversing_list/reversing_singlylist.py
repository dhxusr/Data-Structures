"""
Describe in  detail an algorithm for reversing a singly linked list L using only a constant amount of additional
space and not using any recursion.
"""

def reverse_list(node):
    """Reverse a list given its first node. return the new head of the list."""

    prev_node = None

    while node is not None:

        # keep the next value for traversing
        next_node = node._next 

        # connecting with prev node
        node._next = prev_node 

        prev_node = node
        node = next_node

    return prev_node


from reversing_singlylist_recursive import SingleList

#test
if __name__ == "__main__":

    lst = SingleList()
    empty_list = SingleList()

    for i in range(5):
        lst.add_element(i+1)

    lst._head = reverse_list(lst._head)    
    empty_list._head = reverse_list(empty_list._head)

    current = lst._head
    for _ in range(len(lst)):

        print(current._element, end=' ')
        current = current._next

    print(' ')
    print("empty list", empty_list._head)
        


"""
What is this?
Is a function that reverse a single linked list

How does it works?
it "simulates" the behavior of reversing a stack. if you can see the list its like a stack so for reverse it
we just have to flip the "stack". the function its traversing the list, and each node it "pushing" to the stack
that pushed node is going to be the top element in the stack, if a new node is pushed it will be connected to
the top node at that moment.
when the list its traversed we have all nodes in reverse order in the "stack" and just have to take the top.

Why did i chose this approach
this is an easy way to reverse a sequence of elements. and it allows me to use a constant amount of space.
because i dont create any new instance of any object, just pointers.

What did i learned?
At the beginning of the problem solve, i didn't see the solution, i didn't remember that you can reverse a
sequence by simulating the reversing of a stack. i learned that we have to see beyond that just the structure
that we have in front of us, one thing can be other thing 

What would i improve?
honestly, nothing its just really beautifull.
"""
