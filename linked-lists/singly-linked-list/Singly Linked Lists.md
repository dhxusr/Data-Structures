== Singly Linked Lists ==

A singly linked list, in its simplest form, is a collection of nodes that collectively form a linear sequence.
Each node stores a reference to an object that is an element of the sequence, as well as a reference to the next
node of the list.

        element
         +
         |
        -------
Node = | * | * |--> next node
        -------
	
	
Singli Linked Lists:


         LAX          MSP          ATL          BOS
	  +            +            +            +
          |            |            |            |
         -------      -------      -------      -------
head -> | * | * |--> | * | * |--> | * | * |--> | * | * |--> None
         -------      -------      -------      -------
	                                         ^
						 |
						tail
						

Example of a singly linked list whose elements are strings indicating airporst codes.

The list instance maintain a memeber named head that identifies the first node of the list, and in some applications
another memeber named tail that identifies the last node of the list.

The first and last node of a linked list are known as the head and tail of the list, respectively. By startin at
the head, and moving from on node to another by following each node's next reference, we can reach the tail of the
list.

A linked list's representation in memory relies on the collaboration of many objects. Each node is represented as
a unique object, with that instance storing a reference to its element and a reference to the next node (or Node).
Another object represents the linked list as a whole. Minimally, the linked list instance must keep a reference
to the head of the list. without an explicit reference to the head, there would be no way to lacete that node
(or inderectaly, any others).

* __Inserting an Element at the Head of a Singly Linked List__

An important property of a linked list is that it doesn't have a predetermined fixed size; it is proportionall to
it current numbers of elements. When using a singly linked list we can easily insert an element at the head of the
list by just creating a new node, set its element, and set its next reference to the current head of the list 
then changing the list's head reference to this new node.


           ---------      ---------      ---------
  HEAD -> | MSP | * |--> | ATL | * |--> | BOS | * |--> None
           ---------      ---------      ---------

                                HEAD  
               ---------      ---------      ---------      ---------  
  new node -> | LAX | * |--> | MSP | * |--> | ATL | * |--> | BOS | * |--> None
               ---------      ---------      ---------      ---------
	       
           ---------      ---------      ---------      ---------    
  HEAD -> | LAX | * |--> | MSP | * |--> | ATL | * |--> | BOS | * |--> None
           ---------      ---------      ---------      ---------
	   

* __Inserting an Element at the Tail of a Singly Linked List__
  
  We can easily insert an element at the end of the list, if we keep a reference to the tail node.
  we just create a new node, set its element, changing the last node next reference to this new node and then 
  change the tail reference of the list to the new node.
  
                                             TAIL
             ---------      ---------      ---------
    HEAD -> | MSP | * |--> | ATL | * |--> | BOS | * |--> None
             ---------      ---------      ---------
                                
                   HEAD                          TAIL          NEW NODE
                 ---------      ---------      ---------      ---------
    new node -> | MSP | * |--> | ATL | * |--> | BOS | * |--> | LAX | * |--> None
                 ---------      ---------      ---------      ---------
                 
                                                           TAIL
             ---------      ---------      ---------      ---------    
    HEAD -> | MSP | * |--> | ATL | * |--> | BOS | * |--> | LAX | * |--> None
             ---------      ---------      ---------      ---------


* __Removing an element from a Singly Linked List__
  
  Removing an element from the head of a singly linked list is essentially the reverse operation of inserting a
  new element at the head.
  
  changing the head reference of the list to the next node of the current head.
  
  
           ---------      ---------      ---------
  HEAD -> | MSP | * |--> | ATL | * |--> | BOS | * |--> None
           ---------      ---------      ---------
 
                    
    ---------             ---------      ---------
   | MSP | * |  HEAD --> | ATL | * |--> | BOS | * |--> None
    ---------             ---------      ---------



  Unfortunately, we cannot easily delete the last node of a singly linked list. Even if we maintain a tail reference
  directly to the last node of the list, we must be able to access the node before the last node in order to remove
  the last node. but we cannot reach the node before the tail by following next links from the tail. The only way
  to access this node is to start from the head of the list and search all the way through the list. But such a
  sequence of link-hopping operations could take a long time. If we want to support such an operation efficiently,
  we will need to make our list doubly linked.


  [[Singly Linked list Resume]]










































