# Positional List array-based implementation

## Description
Although we have used a doubly linked list to implement he positional list ADT, it is possible to support
the ADT with an array-based implementation. The key is to use the composition pattern and store a sequence
of position items, where each item stores an element as well as that element's current index in the array.
Whenever an element's place in the array is changed, the recorded index in the position must be updated to match.

What is the efficiency of the various operations?
