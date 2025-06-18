# Binary Trees
A binary tree is an ordered tree with the following properties:
- Every node has at most two children
- Each child node is labeled as being either left child or right child.
- A left child precedes a right child in the order of children of a node.

- The subtree rooted at a left or right child of an internal node v is called left subtree or right subtree,
  respectively, of v.

- A binary tree is proper if each node has either zero or two children. also refer as being full binary trees.
  in a proper binary tree, every internal node has exactly two children.

- A binary tree that is not proper is improper.


```

                        [1]
                       /   \
                      /     \
                     /       \
                   [2]       [3] 
                  /   \        
                 /     \        
               [4]     [5]

```

### A Recursive Binary Tree Definition
Incidentally, we can also define a binary tree in a recursvie way such that a binary tree is either empty or
consists of:
* A node r, called the root of T, that stores an element.
* A binary tree (possibly empty), called the left subtree of T.
* A binary tree (possibly empty), called the right subtree of T.

### Properties of Binary Trees
Binary trees have several interesting properties dealing with relationships between their heights and number of
nodes. We denote the set of all nodes of a tree T at the same depth d as level d of T. In a binary tree, level
0 has at most one node (the root), level 1 has at most two nodes (the children of the root), level 2 has at most
four nodes, and so on. In general, level d has at most 2^d nodes.

```
       level                                                Nodes
         0                      [ 1 ]                         1
                            /           \ 
                           /             \
                          /               \
         1            [ 2 ]               [ 3 ]               2
                     /     \             /     \
                    /       \           /       \
         2        [4]      [5]         [6]       [7]          4
                 /   \     /  \       /   \     /   \ 
                /     \   /    \     /     \   /     \ 
         3     [8]   [9] [10] [11]  [12]  [13][14]   [15]     8


                   
```
We can see that the maximum number of nodes on the levels of a binary tree grows exponentially as we go down the
tree. From this simple observation, we can derive the following properties relating the height of a binary tree
T with its number of nodes.

Let T be a nonempty binary tree, and let n, ne, ni and h denote the number of nodes, number of external nodes,
number of internal nodes, and height of T, repectively. Then T has the following properties:
- h+1 <= n <= 2^h+1 - 1
- 1 <= ne <= 2^h
- h <= ni <= 2^h - 1
- log(n+1)-1 <= h <= n-1

Also, if T is proper, then T has the following properties:
- 2h+1 <= n <= 2^h+1 - 1
- h+1 <= ne <= 2^h
- h <= ni <= 2^h-1
- log(n+1)-1 <= h <= (n-1)/2

### Relating Internal Nodes to External Nodes in a Proper Binary Tree
In addition to the earlier binary tree properties, the following relationship exists between the number of
internal nodes and external nodes in a proper binary tree.

* Proposition: In a nonempty binary tree T, with ne external nodes and ni internal nodes, we have ne = ni+1

* Justification: We justify this proposition by removing nodes from T and dividing them up into two "piles"
an internal-node pile and an external-node pile, until T becomes emtpy. The piles are initially empty.
by the end, we will show that the external-node pile has one more node than the internal-node pile. We consider
two cases:

Case 1: If T has only one node v, we remove v and place it on the external-node pile. thus, the external-node
pile has one node and the internal-node pile is empty.

Case 2: Otherwise (T has more than one node), we remove from T an (arbitrary) external node w and its parent v
which is an internal node. We place w on the external-node pile and v on the internal-node pile. If v has a parent u
then we reconnect u with the former sibling z of w. This operation, removes one internal node and one external
node, and leaves the tree being a proper binary tree.

```
                  (a)
                 [ u ]
                /     \
               /       \
             [v]       []
            /   \     /  \
          [z]   [w]  []  []
         /   \
        []   []

                 (b)
                [ u ]
               /     \
              /       \ 
                      []
           /         /  \
         [z]        []  []
        /   \
       []   []

                (c)
               [ u ]
              /     \
             /       \
           [z]       []
          /   \     /  \
         []   []   []  []
```
Operation that removes an external node and its parent node, used in the justification.

### Implementing Trees

- Linked Structure for Binary Trees:
  A natural way to realize a binary tree is to use a linked structure, with a node that maintains references to
  the stored at a position p and to the nodes associated with the children and parent of p. if p is the root,
  then the parent field of p is None. Likewise, if p does not have a left or right child, the associated field
  is None. The tree itself maintains an instance variable storing a reference to the root node (if any), and
  a variable, called size, that represents the overall number of nodes.

  ``` 
  (a)
            parent
              +
              |
             [ ]
  left +--[ ][ ][ ]--+ right
              |
              +
           element

                                         None
                                          +
  (b)                                     |
  [root]---------------------------->    [p]
  [size: 5]                 -----[l][providence][r]------
                            |                           |
                            +                           +
                           [p]                         [p]
              -----+ [l][Chicago][r] +---        [l][Seattle][r]
              |                         |     
              |                         |
              +                         +
             [p]                       [p]
      [l][Baltimore][r]          [l][New York][r]

          
  ```
  A linked structure for representing: (a) a single node; (b) a binary tree.

- Array-Based Binary Tree
  An alternative representation of a binary tree T is based on a way of numbering the positions of T. For every
  position p of T, lef f(p) be the integer defined as follows.

  * if p is the root, the f(p) = 0.
  * if p is the left child of position q, then f(p) = 2f(q) + 1
  * if p is the right child of position q, then f(p) = 2f(q) + 2

  The numbering function f is known as a level numbering of the positions in a binary tree T, for it numbers
  the positions on each level of T in increasing order from left to right. Note well that the level numbering
  is based on potential positions within the tree, not actual positions of a given tree, so they are not
  necessarily consecutive. for example, in figure (b) there are no nodes with level numbering 13 or 14, because the node
  with level numbering 6 has no children.

  ```  
  (a)                   
                        0
                      [   ]                         
                  /           \ 
                 /             \
              1 /               \ 2
            [   ]               [   ]               
           /     \             /     \
         3/       \4         5/       \6
        [ ]       [ ]       [ ]       [ ]          
       /   \     /  \       /   \     /   \ 
     7/     \8 9/    \10 11/     \12 /     \ 
     [ ]   [ ] [  ]  [ ] [ ]    [ ] [ ]   [ ]     
                                    13     14
            
  (b)
             
                        0
                      [ - ]                         
                  /           \ 
                 /             \
              1 /               \ 2
            [ / ]               [ + ]               
           /     \             /     \
         3/       \4         5/       \6
        [x]       [+]       [x]       [6]          
       /   \     /  \       /   \        
     7/     \8 9/    \10 11/     \12       
     [+]   [3] [-]  [2] [3]      [-]          
    /   \     /   \             /   \              
   /     \   [9]  [5]        25/     \26 
  [3]    [1] 19   20         [7]    [4]
  15     16
  ```
  The level numbering function f suggests a representation of a binary tree T by means of an array-based
  structure A (such as a python list), with the element at position p of T stored at index f(p) of the array.
  example: 
  ```
                        0
                      [ / ]                         
                  /           \ 
                 /             \
              1 /               \ 2
            [ x ]               [ + ]               
           /     \             /     \
         3/       \4         5/       \6
        [+]       [4]       [-]       [2]          
       /   \               /   \        
     7/     \8          11/     \12       
    [3]     [1]         [9]     [5]          

  [/][x][+][+][4][-][2][3][1][ ][ ][9][5][ ][ ]
   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
  ```
  One advantage of an array-based representation of a binary tree is that a position p can be represented by
  the single integer f(p), and that position-based methods such as root, parent, left, and right can be
  implemented using simple arithmetic operations on the number f(p). Based on our formula for the level numbering
  the left child of p has index 2f(p)+1, the right child of p has index 2f(p) + 2, and the parent of p has index
  (f(p)-1)/2.

  The space usage of an array-based representation depends greatly on the shape of the tree. Let n be the number
  of nodes of T, and let fm be the maximum value of f(p) over all the nodes of T. The array A requires length
  N = 1 + fm, since elements range from A[0] to A[fm]. Note that A may have a number of empty cells that do not
  refer to existing nodes of T. In fact, in the worst case, N = 2^n -1.
   
