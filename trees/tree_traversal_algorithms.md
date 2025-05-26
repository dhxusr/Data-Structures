# Tree Traversal Algorithms
A traversal of a tree T is a systematic way of accessing of "visiting," all the
positions of T. The specific action associated with the "visit" of a position
p depends on the application of this traversal, and could involve anything from
incrementing a counter to performing some complex computation for p.

## Preorder and Postorder Traversals of General Trees
### Preorder Traversal
In a preorder traversal of a tree T, the root of T is visited first and then
the subtrees at its children are traversed recursively. If the tree is ordered
then the subtrees are traversed according to the order of the children.

pseudo code of the preorder algorithm:
Algorithm preorder(T, p):
  perform the "visit" action for position p
  for each child c in T.children(p) do
    preorder(T, c)

### Postorder Traversal
Another important tree traversal algorithm is the postorder traversal. In some
sense, this algorithm can be viewed as the opposite of the preoreder traversal
because it recursively traverses the subtrees rooted at the children of the root
first, and then visits the root.

pseudo code for postorder traversal algorithm:
Algorithm postorder(T, p):
  for each child c in T.children(p) do
    postorder(T, c)
  perform the "visit" action for position p

### Running-Time Analysis
Both preorder and postorder traversal algorithms are efficient ways to access
all the positions of a tree. At each position p, the nonrecursive part of the
traversal algorithm requires time O(cp + 1), where cp is the number of children
of p, under the assumption that the "visit" itself takes O(1) time.
The overall running time for the traversal of tree T is O(n), where n is the
number of positions in the tree. This running time is asymptotically optimal
sice the traversal must visit all the n positions of the tree.

## Breadth-First Tree Traversal
Although the preorder and postorder traversals are common ways of visiting the
positions of a tree, another common approach is to traverse a tree so that we
visit all the positions at depth d before we visit the positions at depth d+1.
Such an algorithm is known as a breadth-first traversal.
A breadth-first traversal is a common approach used in software for playing
games. A game tree represents the possible choices of moves that might be made
by a player (or computer) during a game.

Pseudo-code for a breadth-first traversal:
The process is not recursive, since we are not traversing entire subtrees at once.
We use a queue to produce a FIFO (first-in first-out) semantics for the order in
which we visit the nodes. The overall running time is O(n), due to the n calls
to enqueue and n calls to dequeue.

Algorithm bredthfirst(T):
  Initialize queue Q to contain T.root()
  while Q not empty do
    p = Q.dequeue()
    perform the visit action for position p
    for each child c in T.children(p) do
      Q.enqueue(c)

## Inorder Traversal of a Binary Tree
The standard preorder, postorder, and breadth-first traversals that were
introduced for general trees, can be directly applied to binary trees. In this
section, we introduce another common traversal algorithm specifically for a
binary tree.
During an inorder traversal, we visit a position between the recursive traversal
of its left and right subtrees. The inorder traversal of a binary tree T can be
informally viewed as visiting the nodes of T "from left to right." Indeed, for
every position p, the inorder traversal visits p after all the positions in the
left subtree of p and before all the positions in the right subtree of p.

Pseudo-code for the inorder traversal algorithm:
Algorithm inorder(p):
  if p has a left child lc then
    inorder(lc)
  perform the "visit" action for position p
  if p has a right child rc then
    inorder(rc)

The inorder traversal algorithm has several important applications. Whe using
a binary tree to represent an arithmetic expression, the inorder traversal
visits positions in a consistent order with the standard representation of the
expression

### Binary Search Trees
An important application of the inorder traversal algorithm arises when we store
an ordered sequence of elements in a binary tree, defining a structure we call
a binary search tree. Let S be a set whose unique elements have an order relation.
For example, S could be a set of integers. A binary search tree for S is a binary
tree T such that, for each position p of T:
  * Position p stores an element of S, denoted as e(p).
  * Elements stored in the left subtree of p (if any) are less than e(p).
  * Elements stored in the right subtree of p (if any) are greater than e(p).
An example of a binary search tree. The above properties assure that an inorder
traversal of a binary search tree T visits the elements in nondecreasing order

```
                ----------(58)- - - - -
                |                      |
         - - -(31)------         - - -(90)
        |              |         |
   - -(25)        ----(42)       (63) - -
  |               |                     |
(12)            (36)                  (75)
```
A Binary search tree storing integers. the solid path is traversed when searching
(successfully) for 36. The dashed path is traversed when searching (unsuccessfully)
for 70.

We can use a binary search tree T for set S to find whether a given search value
v is in S, by traversing a path down the tree T, starting at the root. At each
internal position p encountered, we compare our search value v with the element
e(p) stored at p. If v < e(p), then the search continues in the left subtree of p.
if v = e(p), then the search terminates successfully. If v > e(p), then the
search continues in the right subtree of p. Finally, if we reach an empty subtree,
the search terminates unsuccessfully. In other words, a binary search tree can be
viewed as a binary decision tree, where the question asked at each internal node
is whether the element at that node is less than, equal to, or larger than the
element being searched for.
Note that the running time of serching in a binary search tree T is proportional
to the height of T. Recall that the height of a binary tree with n nodes can be
as small as log(n+1) - 1 or as large as n-1. Thus, binary search trees are most
efficient when they have small height.
