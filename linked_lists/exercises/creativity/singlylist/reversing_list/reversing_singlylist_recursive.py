"""
Describe a fast recursive algorith for reversing a singly linked list.
"""


class SingleList:

    class Node:

        def __init__(self, element, next):

            self._element = element
            self._next = next    


    def __init__(self):

        self._head = None
        self._tail = None
        self._size = 0


    def __len__(self):
        return self._size


    def add_element(self, element):

        node = self.Node(element, None)

        if self._size == 0:
            self._head = node

        else:
            self._tail._next = node

        self._tail = node
        self._size += 1 


#first solution
def recursive_reversing(node):
    """Reverse a singly list recursively by its first node."""

    if node._next is None or node is None:
        return node

    new_head = recursive_reversing(node._next)
    node._next._next = node
    node._next = None

    return new_head


#second solution
def recursive_reverse(single_list):
    """Reverse a singly linked list recursiveley."""

    if single_list._head._next is None:
        return single_list._head

    new_last = single_list._head
    single_list._head = single_list._head._next

    reversed_nodes = recursive_reverse(single_list)
    reversed_nodes._next = new_last    

    return new_last 

if __name__ == "__main__":

    sl = SingleList()

    for i in range(5):
        sl.add_element(i+1)

    sl._tail = recursive_reverse(sl)


    current = sl._head
    while current:
        print(current._element, end=' ')

        current = current._next

    print(' ')



"""
What is this?
This is a function that reverse a singly list recursively.

How does it works?
The first solution is a solution for a list that has head and tail pointer because the function return the
new last element the first node of the list is given to the function and then the funtiction "iterates" until
the last element, this follow the approach of
list = [1, 2, 3, 4, 5] is reversed as [5, 4, 3, 2] + the first element 1, this way we can divide the problem
in same type subproblems.
each value returned by the function is the "new_last" element
and when the reverse is complete the user has to set the pointers head and tail to the new values.

but what if we have a list that just has the head pointer?
if the function returns the "new_last" element, how do i know which is the new head?
for that i did the second solution, which sove this problem, the function receives as an argument a singly list
object, then gets the current head as the new last is this case is 1 for add it to the rest of the nodes when
they are reversed, then move the pointer of the head forward, until it gest to the last element, and now we
have our head pointer pointing to the "new_head", the rest of the function is the same as the firrst solution.

Why did i chose this approach?
i chose this approach because it was the more "recursive" that i found, dividing the problem in subproblems
of the same type

What did i learned?
i learned that singly linked list with only the head pointer are hard to work with but funny.
i learned that one problem can has different ways to solve it
i learned that we have to remember the main porpuse of the recursivity that is divide some problem in subproblems
of the same type.

What would i improve?
maybe the solution, i think it could be more clean
"""
