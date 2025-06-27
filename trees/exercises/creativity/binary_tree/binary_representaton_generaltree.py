"""
We can define a binary tree representation T' for an ordered general tree T as follows:
* For each position p of T, there is an associated position p' of T'.
* If p is a leaf of T, the p' in T' does not have a left child; otherwise the left child of p' is q', where
  q is the first child of p in T.
* If p has a sibling q ordered immediately after it in T, then q' is the right child of p' in T'; otherwise
  p' does not have a right child.

Given such a representation T' of a general ordered tree T, answer each of the following questions:

a. Is a preorder traversal of T' equivalent to a preorder traversal of T?
b. Is a postorder traversal of T' equivalent to a postorder traversal of T?
c. Is an inorder traversal of T' equivalent to one of the standard traversals of T if so, which one?

T:                            T':

           (A)                              (A)
       -----------                      ------
       |    |    |                      |
      (B)  (C)  (D)                    (B)
     -----       -                   ---- - - 
     |   |       |                   |       |
    (E) (F)     (G)                 (E)     (C)
                                     - -      - - -
                                       |          |
                                      (F)        (D)
                                               --- 
                                               |
                                              (G)

answers:

a. Yes
b. No
c. Yes, equivalent to postorder of T                                              
""" 
