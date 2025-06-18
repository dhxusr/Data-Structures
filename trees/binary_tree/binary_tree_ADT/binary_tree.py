from tree_ADT.tree import Tree

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
