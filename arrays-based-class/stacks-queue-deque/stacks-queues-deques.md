== Stacks, Queues and Deques in python ==

- __Stacks__
  
  A stack is a collection of objects that can be inserted and removed following the principle LIFO
  (last-in, first-out) that means that we access only to the last element inserted in the stack, this data structure
  follows the metaphor of a stack of plates in a cafeteria plate dispenser.
  
  fundamental operations in this data structure.
  
  push: insert an object at the end of the stack.
  pop: return the top object of the stack and remove it.
                            
			                      -
                          - -
  inserting plates ->   - - -
                      - - - -

                   -
	                 - -
  poping plates -> - - -
                   - - - -

  the stack is the simplest of the data structures but they are also among the most important.
  
  - Reversing Data using a stack.
    
    As a consequence of the LIFO protocol, a stack can be used as a general tool for reverse a data sequence.
    
  - Matching parentheses and html tags
    An algorithm for matching delimiters
    
    left = "{[("
    right = "}])"
    
    we assume that the input is a sequence of characters, such as '[(5+x)-(y+z)]'.
    we perform a left to right scan of the original sequence and then check if the current character is in the 
    left delimiters if its in, we push that delimitir into a stack, else if the current character is in the 
    right delimiters we check if the top of the stack is equal to this delimiter so they make a pair.
    if we reach the end of the expression and the stack is empty, the expression is properly matched. otherwise
    there must be an open delimiter on the stack without a matching symbol.

- __Queues__
  a queue is a collection of objects that its behavior follows the principle FIFO (First-in, First-out).
  that is, elements are inserted in any time, but only the element that has been in the queue the longest can be
  next removed.
  
  * elements are inserted at the back and removed from the front.
  * elements access and deletions are restricted to the first element of the collection.
  * elements insertion is restricted to the back of the sequence.

  The queue abstract data type supports the following two fundamentals methods for a queue:
  
  Q.enqueue(e): insert an element at the back
  Q.dequeue(): remove and return the first element; an error occurs if the queue is empty.
  Q.first(): return a refference to the first element in the queue. error if empty.
  Q.is_empty(): return if the queue is empty or not.
  len(Q): return the number of elements in the queue. 
  
  

- __Deque__
  Double-ended Queue is a Queue-like collection of objects that supports insertion and deletion at both the front
  and the back of the queue
  
  so we can insert a object at the back and then remove it from the back, same in the front.
  
  supported methods:
  D.add_first(e): Add element e to the front of the deque.
  D.add_last(e): Add element e to the back of the deque.
  D.delete_first(): Remove and return the first element from deque; error if empty.
  D.delete_last(): Remove and return the last element from deque; error if empty.
  D.first(): Return a refference of the first element in the deque; error if empty.
  D.last(): Return a refference of the last element in the deque; error if emtpy.
  D.is_empty(): Return True if the deque is emtpy.
  len(D): Return the number of elements in the deque.
