"""
For linked binary trees, a reasonable set of update methods to supports for general usage are the following.

- T.add_root(e): Create a root for an empty tree, storing e as the element, and return the position of that root
  an error occurs if the tree is not empty.

- T.add_left(p, e): Create a new node storing element e, link the node as the left child of position p, and
  return the resulting position; an error occurs if p already has a left child.

- T.add_right(p, e): Create a new node storing element e, link the node as the right child of position p, and
  return the resulting position; an error occurs if p already has a right child.

- T.replace(p, e): Replace the element stored at position p with element e, and return the previously stored
  element.

- T.delete(p): Remove the node at position p, replacing it with its child, if any, and return the element that
  had been stored at p; an error occurs if p has two children.

- T.attach(p, T1, T2): Attach the internal structure of trees T1 and T2, respectively, as the left and right
  subtrees of leaf position p of T, and reset T1 and T2 to empty trees; an error condition occurs if p is not a
  leaf.
"""

from binary_tree.binary_tree_ADT.binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
  """Linked representation of a binary tree structure."""

  class _Node:
    __slots__ = "_element", "_parent", "_left", "_right"

    def __init__(self, element, parent=None, left=None, right=None) -> None:
      self._element = element
      self._parent = parent
      self._left = left
      self._right = right

  class Position(BinaryTree.Position):
    """An abstraction representing the location of a single element."""

    def __init__(self, container, node) -> None:
      self._container = container
      self._node = node

    def element(self):
      return self._node._element

    def __eq__(self, other) -> bool:
      """Return True if other is a Position representing the same location."""
      return type(other) is type(self) and other._node is self._node

  def _validate(self, p) -> _Node:
    """Return associated node, if position is valid."""
    if not isinstance(p, self.Position):
      raise TypeError("position must be proper Position type")

    if p._container is not self:
      raise ValueError("position does not belong to this container")

    if p._node._parent is p._node:
      raise ValueError("position is no longer valid")

    return p._node

  def _make_position(self, node) -> Position | None:
    """Return Position instance for given node (or None if no node)."""
    return self.Position(self, node) if node is not None else None

  #-------------------- binary tree constructor --------------------#
  def __init__(self) -> None:
    self._root = None
    self._size = 0
    self._sentinel = self._Node(None, left=self._root)

  #-------------------- public accessors --------------------#
  def __len__(self) -> int:
    return self._size

  def root(self) -> Position | None:
    """Return the root position of the tree (or None if tree is empty)."""
    return self._make_position(self._root)

  def parent(self, p) -> Position | None:
    """Return the Position of p's parent (or None if p is root)."""
    node = self._validate(p)
    return self._make_position(node._parent) 

  def left(self, p) -> Position | None:
    """Return the Position of p's left child (or None if no left child)."""
    node = self._validate(p)
    return self._make_position(node._left)

  def right(self, p) -> Position | None:
    """Return the Position of p's right child (or None if no right child)."""
    node = self._validate(p)
    return self._make_position(node._right)

  def num_children(self, p) -> int:
    """Return the number of children of Position p."""
    node = self._validate(p)
    count = 0
    if node._left is not None:
      count += 1
    if node._right is not None:
      count += 1
    return count

  def _add_root(self, e) -> Position:
    """Place element e at the root of an empty tree and return new Position.
    Raise ValueError if tree is nonempty.
    """
    if self._root is not None:
      raise ValueError("Root exists.")

    self._size = 1
    self._root = self._Node(e, self._sentinel)
    return self._make_position(self._root)

  def _add_left(self, p, e) -> Position:
    """Create a new left child for position p, storing element e.

    Return the Position of new node.
    Raise ValueError if Position p is invalid or p already has a left child."""

    node = self._validate(p)
    if node._left is not None:
      raise ValueError("Left child exists")

    self._size += 1
    node._left = self._Node(e, node)
    return self._make_position(node._left)

  def _add_right(self, p, e) -> Position:
    """Create a new right child for position p, storing element e.

    Return the Position of new node.
    Raise ValueError if Position p is invalid or p already has a right child."""

    node = self._validate(p)
    if node._right is not None:
      raise ValueError("Right child exists")

    self._size += 1
    node._right = self._Node(e, node)
    return self._make_position(node._right)

  def _replace(self, p, e):
    """Replace the element at position p with e, and return old element."""
    node = self._validate(p)
    old = node._element
    node._element = e
    return old

  def _delete(self, p):
    """Delete the node at Position p, and replace it with its child, if any.

    Return the element that had been stored at position p.
    Raise ValueError if Position p is invalid or p has two children.
    """
    node = self._validate(p)
    if self.num_children(p) == 2:
      raise ValueError("Position has two children")

    child = node._left if node._left is not self._sentinel else node._right
    if child is not self._sentinel:
      child._parent = node._parent
    if node is self._root:
      self._root = child
    else:
      parent = node._parent
      if node is parent._left:
        parent._left = child
      else:
        parent._right = child

    self._size -= 1
    node._parent = node
    return node._element

  def _attach(self, p, t1, t2) -> None:
    """Attach trees t1 and t2 as left and right subtrees of external p."""
    node = self._validate(p)
    if not self.is_leaf(p):
      raise ValueError("position must be leaf")

    if not type(self) is type(t1) is type(t2):
      raise TypeError("Tree types must be match")

    self._size += len(t1) + len(t2)
    if not t1.is_empty():
      t1._root._parent = node
      node._left = t1._root
      t1._root = None
      t1._size = 0
    if not t2.is_empty():
      t2._root._parent = node
      node._right = t2._root
      t2._root = None
      # t2._size = 0

  def _delete_subtree(self, p):
    """Removes the entire subtree rooted at position p."""

    self._validate(p)
    parent = self.parent(p)
    number_of_nodes = 0
    for _ in self._subtree_inorder(p):
      number_of_nodes += 1

    parent_node = self._validate(parent)
    if self.left(parent) == p:
      parent_node._left = None
    elif self.right(parent) == p:
      parent_node._right = None

    self._size -= number_of_nodes

  def _swap(self, p, q):
    """Restructures the tree so that the node referenced by p takes the place of the node referenced by q
    and vice versa.
    """    
    p = self._validate(p)
    q = self._validate(q)
    if p is self._root:
      self._root = q
    elif q is self._root:
      self._root = p

    if p._parent is q._parent:
      if p is p._parent._left:
        p._parent._left = q
        p._parent._right = p
      else:
        p._parent._left = p
        p._parent._right = q

    elif p._parent is q or q._parent is p:
      parent = q if p._parent is q else p
      children = p if parent is q else q

      if parent._parent:
        if parent is parent._parent._left:
          parent._parent._left = children
        else:
          parent._parent._right = children
      children._parent = parent._parent

      if children is parent._left:
        parent._left = parent
      else:
        parent._right = parent
      parent._parent = children      

    else:
      if p._parent:
        if p is p._parent._left:
          p._parent._left = q
        else:
          p._parent._right = q

      if q._parent:
        if q is q._parent._left:
          q._parent._left = p
        else:
          q._parent._right = p

      p._parent, q._parent = q._parent, p._parent

    p._left, p._right, q._left, q._right = q._left, q._right, p._left, p._right

    if p._left:
      p._left._parent = p
    if p._right:
      p._right._parent = p

    if q._left:
      q._left._parent = q
    if q._right:
      q._right._parent = q

    
if __name__ == "__main__":
  tree = LinkedBinaryTree()
  tree2 = LinkedBinaryTree()
  root2 = tree2._add_root(10)
  root = tree._add_root(1)
  two = tree._add_left(root, 2)
  three = tree._add_right(root, 3) 
  four = tree._add_left(two, 4)
  five = tree._add_right(two, 5)
  six = tree._add_left(three, 6)
  tree._add_right(three, 7)

  tree._attach(two, tree, tree2)
