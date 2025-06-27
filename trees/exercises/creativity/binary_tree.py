from collections.abc import Iterator
from mytree import Tree

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    #---------- Additional abstract methods ----------#
    def left(self, p):
        """Return a Position representing p's left child.
        Return None if p does not have a child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """Return a position representing p's right child.
        Return None if p does not have a child.            
        """
        raise NotImplementedError("must be implemented by subclass")

    #---------- Concrete methods implemented in this class ----------#
    def sibling(self, p):
        """Return a Position representing p's sibling.
        Return None if p does not have a sibling.
        """
        parent = self.parent(p)
        if parent is None:
            return None

        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        left = self.left(p)
        right = self.right(p)

        if left is not None:
            yield left

        if right is not None:
            yield right

    def inorder(self):
        """Generate an inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate an inorder iteration of positions in subtree rooted at p."""
        left_child = self.left(p)
        right_child = self.right(p)

        if left_child is not None:
            for other in self._subtree_inorder(left_child):
                yield other
        yield p
        if right_child is not None:
            for other in self._subtree_inorder(right_child):
                yield other
        
    def positions(self):
        """Generates an iterations of the tree's postions."""
        return self.inorder()

    def num_children(self, p) -> int:
        """Return the number of children of a given position."""

        if self.left(p):
            return 2

        return 0

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

  class LinkedBinaryTreeIter:
      """An iterator that return the values in the tree using preorder-traversal."""

      def __init__(self, tree) -> None:
        self._tree = tree
        self._node = self._tree.root()

      def __iter__(self):
        return self

      def __next__(self):

        if self._node is None:
         raise StopIteration

        next = self._node
        self._node = self.preorder_next(self._node)
        return next.element()

      def preorder_next(self, p):
          """Return the position visited after p in a preorder traversal of T.
          None if p is the last position."""

          left = self._tree.left(p)
          right = self._tree.right(p)
          # if internal node, the next is some of its children
          if left:
              return left

          elif right:
              return right

          # if is external node
          # if left child, the next is its brother if it has.
          # otherwise its an ancestor if it has.

          else:
              parent = self._tree.parent(p)
              if parent:
                  # getting brother if any.
                  sibling = self._tree.sibling(p)
                  if self._tree.left(parent) == p and sibling:
                          return sibling

                  else:
                      return self.find_uncle(p)

      def find_uncle(self, p):
        parent = self._tree.parent(p)
        while parent != self._tree.root():
            uncle = self._tree.right(self._tree.parent(parent))
            if uncle and uncle != parent:
                return uncle
            parent = self._tree.parent(parent)
        return None

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

  def __iter__(self):
    return self.LinkedBinaryTreeIter(self)

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

  def preorder(self):
    return iter(self)
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
  for c in tree.preorder():
    print(c)
