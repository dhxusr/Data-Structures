"""
Implement a function that accpts a PositionalList of n integers sorted in nondecreasing order, and another
value V, and deterimines in O(n) time if there are two elements in L that sum precisly to V. The function
should return a pair of positions of such elements, if found, or None otherwise.
"""

def two_sum_in(plist, value):
    """"Determine in O(n) time if there are two elements in a
    sorted list that sum precisly the given value."""

    left_position = plist.first()
    right_position = plist.last()

    while True:

        sum = left_position.element() + right_position.element()

        if sum == value:
            return (left_position, right_position)

        if (plist.after(left_position) == right_position or
            plist.before(right_position) == left_position or
            left_position == right_position):
            return None

        if sum > value:
            right_position = plist.before(right_position)

        elif sum < value:
            left_position = plist.after(left_position)



"""
What is this?
Is a function that seach if there are two elements that sum precisely to value.

How does it works?
It has two pointers, because the list is in increase oreder, first element will be the lowest and the last
element will be the greatest.
we can approach this in the way that if the sum of the greatest and lowest values is greater than the given
value, we need a lower number than the last. so we move the right pointer to the left (lower value)
same in the lower side, if the sum of the greatest and lowest is lower than the given value, then we need
a greater value than the first element, so we move the left_pointer to the right and so on

Why did i chose this approach
i was thinking that the only way to do this was by eliminating the more possible options
because i need traverse the list only one time, then i realized that i can do it with the first
and last elements

What did i learned?
how to search a sum of two values in an ordered list/array
not to give up even if the problem seem too difficult, even if take too much time.
What would i improve?
"""
