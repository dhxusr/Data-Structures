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
    self._root = self._Node(e)
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

    child = node._left if node._left else node._right
    if child is not None:
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
      t2._size = 0


if __name__ == "__main__":
  tree = LinkedBinaryTree()

  root = tree._add_root(1)
  two = tree._add_left(root, 2)
  three = tree._add_right(root, 3) 
  tree._add_left(two, 4)
  tree._add_right(two, 5)
  print(tree.root().element())
  print(tree.left(two).element())
