"""
Describe how to clone a LinkedBinaryTree instance representing a proper binary tree, with use of the _attach
method.

for cloning the tree, we have to make a deep copy, making new nodes.
first make make a copy of the root node.
then clone the subtrees
attach them to the tree.

pseudo-code
clone(t):
 if t is empty
  return an empty tree

 esle
  copy the root node and set it as the root
  leftt = clone the left subtree 
  rightt = clone the rightsubtree
  attach them to the root

 return the tree 
"""

