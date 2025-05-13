### Linked lists ###

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
 
 
 * __Singly Linked Lists__
 
 
 Link-Based vs Array-Based Sequences
 
 __Advantages of Array-Based Sequences__
 
 * Arrays provides O(1)-time access to an element based on an integer index.
   The ability to access the kth element for any k in O(1) time is a hallmark advantage of arrays. In contrast,
   locating the kth element in a linked list requires O(k) time to traverse the list from the beginning, or 
   possibly O(n-k) time, if traversing backward from the end of a doubly linked list.
   
 * Operations with equivalent asymptotic bounds typically run a constant factor more efficiently with an array-based
   structure versus a linked structure. As an example, consider the typical enqueue operation for a queue. Ignoring
   the issue of resizing an array, this operation for the ArrayQueue class involves an arithmetic calculation of
   the new index, an increment of an integer, and storing a reference to the element in the array.
   In contrast, the process for a LinkedQueue requires the instantiation of a node, appropiate linking of nodes, 
   and an increment of an integer. While this operation completes in O(1) time in either model, the actual number
   of CPU operations will be more in the linked version, especially given the instantiation of the new node.
   
 * Array-based representation typically use proportionally less memory than linked structures. This advantage may
   seen counterintuitive, especially given that the length of a dynamic array may be longer than the number of 
   elements that it stores. Both array-based lists and linked lists are referential structures, so the primary
   memory for storing the actual objects that are elements is the same for either structure. What differs is the 
   auxiliary amounts of memory that are used by the two structures. For an array-based container of n elements, a
   typical worst case may be that a recently resized dynamic array has allocated memory for 2n object references.
   With linked lists, memory must be devoted not only to store a reference to each contained object, but also 
   explicit references that link the nodes. So a singly linked list of length n already requires 2n references
   (an elemente reference and next reference for each node). With a doubly linked list, there are 3n referenes.
 
 
 __Advantages of Link-Based Sequences__
 
 * Link-based structures provide worst-case time bounds for their operations.
   This is in contrast to the amortized bounds associated with the expansion or contraction of a dynamic array.
   
   When many individual operations are part of a larger computation, and we only care about the total time of that
   computation, an amortized bound is as good as a worst-case bound precisely because it gives a guarantee on the
   sum ot the time spent on the individual operations.
   
   However, if data structure operations are used in a real-time system that is designed to provide more immediate
   responses (e.g, an operating system, Web server, air traffic control system), a long delay caused by a single
   (amortized) operation may have an adverse effect.
   
 * Link-based structures support O(1)-time insertions and deletions at arbitrary positions. The ability to perform
   a constant-time insertion or deletion with the PositionalList class, by ussing a Position to efficiently describe
   the location of the operation, is perhaps the most significant advantage of the linked list.
