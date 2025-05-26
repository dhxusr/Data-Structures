# General Trees
A tree is an abstract data type that stores elements hierarchically. With the exception of the top element,
each element in a tree has a parent element and zero or more children elements. A tree is usually visualized by
placing elements inside ovals or rectangles, and by drawing the connections between parents and children with
straight lines. We typically call the top element the root of the tree, but it is drawn as the highest element,
with the other elements being connected below.

### Formal definition
Formally, we define a tree T as a set of nodes storing elements such that the nodes have a parent-child relationship
that satisfies the following properties:
* If T is nonempty, it has a special node, called the root of T, that has no parent.
* Each node v of T different from the root has a unique parent node w; every node with parent w is a child of w.

Note that according to the definition, a tree can be emptyl, meaning that it does not have any nodes. This convention
also allows us to define a tree recursively such that a tree T is either empty or consists of a node r, called the
root of T, and a (possible empty) set of subtrees whose roots are the children of r.

### Other Node Relationship
Two nodes that are children of the same parent are siblings. A node v is external if v has no children. A node v
is internal if it has one or more children. External nodes are also known as leaves.

A node u is an ancestor of a node v if u is the parent of the parent of v. Conversely, we say that a node v is
descendant of a node u if u is an ancestor of v.
The subtree of T rooted at a node v is the tree consisting of all the descendant of v in T (including v itself).

### Edges and Paths in Trees
* Edge: An edge of tree T is a pair of nodes (u, v) such that u is the parent of v, or viceversa. 
* Path: A path of T is a sequence of nodes such that any two consecutive nodes in the sequence form and edge.

```

                                         ROOT
                   --------------- [/user/rt/courses/]---------------
                   |                                                |
                   | PARENT/ANCESTOR                                |
      ----------[cs016]------------                         -----[cs252/]-----
      |            |              |                         |                |
      |            |              |CHILD                    |                |
  [grades]   [homeworks/]      [programs/]           ----[projects/]----    [grades]
             |     |    |      |    |    |           |                 |
             |     |    |      |    |    |           |                 |
           [hw1] [hw2] [hw3] [pr1] [pr2] [pr3]   [papers/]         [demos/]
                              DECENDANTS         |       |             |
                                                 |       |             |
                                            [buylow] [sellhigh]     [market]

```

### Ordered Trees
A tree is ordered if there is a meningful linear order among the children of each node; that is, we purposefully
identify the children of a node as being first, second, third, and so on. Such an order is usually visualized
by arranging siblings left to right, according to their order

### Dept
The depth of a node is the number of ancestors of the node, excluding the node itself.
* if p is the root, then the depth is 0.
* otherwise, the depth is one plus the depth of the parent of p.

### Height
The height of a tree if the maximum of the dephts of its leaf position.
* the height of a leaf is 0.
* the height of a node is one more than the maximum of the heights of its children.
