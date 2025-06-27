"""
The balance factor of an internal position p of a proper binary tree is the difference between the heights of
the right and left subtrees of p. show how to specialize the euler tour traversal to print the balance factors
of all the internal nodes o a proper binary tree.
"""


class EulerTour:
    """Abstract base class for performing Euler tour of a tree.
    _hook_previsti and _hook_postvisit may be overrideen by subclasses.
    """

    def __init__(self, tree):
        """Prepare an Euler tour template for given tree."""
        self._tree = tree

    def tree(self):
        """Return reference to the tree being traversed."""
        return self._tree

    def execute(self):
        """Perform the tour and return any result from post visit of root."""
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """Perform tour of subtree rooted at Position p.

        p     Position of current node being visited
        d     depth of p in the tree
        path  list of indices of children on path from root to p
        """

        self._hook_previsit(p, d, path)
        results = []
        path.append(0) # add new index to end of path before recursion
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        if self._tree.num_children(p) == 0:
            return 0
        
        print(p.element(), "balance:", results[0] - results[1])
        return max(results) + 1

class BinaryEulerTour(EulerTour):
    """Abstract base class for performing Euler tour of a binary tree.

    This version includes an additional _hook_invisit that is called after the tour
    of the left subtree (if any), yet before the tour of the right subtree (if any).

    Note: Right child is always assigned index 1 in path, even if no left sibling.
    """

    def _tour(self, p, d, path):
        results = [None, None]
        self._hook_previsit(p, d, path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d+1, path)
            path.pop()
        self._hook_invisit(p, d, path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tour(self._tree.right(p), d+1, path)
            path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_invisit(self, p, d, path):
        pass

from binary_tree import LinkedBinaryTree
if __name__ == "__main__":
  tree = LinkedBinaryTree()
  root = tree._add_root(1)
  two = tree._add_left(root, 2)
  three = tree._add_right(root, 3) 
  four = tree._add_left(two, 4)
  five = tree._add_right(two, 5)
  six = tree._add_left(three, 6)
  tree._add_right(three, 7)
  tree._add_right(four, 8)
  tree._add_left(four, 7)

  euler = BinaryEulerTour(tree)
  euler._tour(root, 0, [])
