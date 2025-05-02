== Linked lists ==

disadventange of python's list class

1- The length of a dynamic array might be longer than the actual number of elements that it stores.

2- Amortized bounds for operations may be unacceptable in real-time systems.

3- Insertions and deletions at interior positions of an array are expensive.


A data structure known as linked list, which provides an alternative to an array-based sequence. Both array-based
 sequences and linked lists keep elements in a certain order, but using a very different style. An array provides
 the more centralized representation, with one large chunk of memory capable of accomoditing references to many 
 elements. A linked list, in contrast, relies on a more distributed representation in which a lighweight object,
 known as a node, is allocated for each element. Each node maintains a reference to its element and a one or more
 references to neighboring nodes in order to collectively represent the linear order of the sequence.
 
 Disadventages when contrasting array-based sequences and linked lists. 
 - Elements of a linked list cannot be efficiently accessed by a numeric index k, and we cannot tell just by
   examinning a node if it is the second, fifth, or twentieth node in the list. However, linked lists avoid the
   three disadventages noted above for array-based sequences.
 
 
 * [[Singly Linked Lists]]
