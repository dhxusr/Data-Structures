# The tree Abstract Data Type
As we did with positional lists, we define a tree ADT using the concept of a position as an abstraction for a
node of a tree. An element is stored at each position, and positions satisfy parent-child relationships that
define the tree structure.

The tree ADT supports the following accessor methods, allowing user to navigate the varios positions of a tree:

- T.root(): Return the position of the root of tree T, or None if emtpy.
- T.is_root(p): Return True if position p is the root of Tree T.
- T.parent(p): Return the position of the parent of position p, or None if p is the root of T.
- T.num_children(p): Return the number of children of position p.
- T.children(p): Generate an iteration of the children of position p.
- T.is_leaf(p): Return True if position p does not have any children.
- len(T): Return the number of positions (and hence elemnts) that are contained in tree T.
- T.is_empty(): Return True if tree T does not contain any positions.
- T.positions(): Generate an iteration of all positions of tree T.
- iter(T): Generate an iteration of all elements stored within tree T.

Any of the above methods that accepts a position as an argument should generate a ValueError if that position
is invalid for T.

If a tree T is ordered, then T.children(p) reports the children of p in the natural order. If p is a leaf, then
T.children(p) generates an empty iteration. In similar regard, if tree T is empty, then both T.positions() and
iter(T) generate empty iterations. 
