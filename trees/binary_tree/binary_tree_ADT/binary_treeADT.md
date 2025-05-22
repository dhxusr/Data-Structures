# The Binary Tree Abstract Data Type
As an abstract data type, a binary tree is a specialization of a tree that supports three additional accessor
methods:
- T.left(p): Return the position that represents the left child of p, or None if p has no left child.
- T.right(p): Return the position that represents the richt child of p, or None if p has no right child.
- T.sibling(p): Return the position that represents the sibling of p, or None if p has no sibling.

### The BinaryTree Abstract Base Class in Python
Just as Tree was defined as an abstract base class, we define a new BinaryTree class based upon the existing
Tree class. However, our BinaryTree class remains abstract, as we still do not provide complete specifications
for how such a structure will be represented internally, nor implementations for some necessary behaviors.

A binary tree supports all the functionality that was defined for general trees. In addition, the new class
provides declarations for new abstract methods left and right that should be supported by concrete subclasses
of BinaryTree.
The new class provides declarations for new abstract methods left and right that should be supported by concrete
subclasses of BinaryTree.
Our new class also provides two concrete implementations methods. The new sibling method is derived from the
combination of left, right, and parent. Typically, we indentify the sibling of a node as the other child of
node's parent. However, if node is the root, it has no parent, and thus no sibling. Also, the node may be the
only child of its parent, and thus does not have a sibling.
