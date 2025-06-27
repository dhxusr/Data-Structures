"""
Design an algorithm for drawing general trees, using a style similar to the inorder traversal approach for
drawing binary trees.
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
        pass


class GeneralLayout(EulerTour):
    """Class for computing (x, y) coordinates for each node of a tree."""

    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0

    def _hook_previsit(self, p, d, path):
        p.element().setX(self._count)
        p.element().setY(d)
        self._count += 1

    def _hook_postvisit(self, p, d, path, results):
        number = p.element()
        print('n:', number._value, "coords:", number.coords())    
class NumberWithCords:
    """A simple object to layout values of a tree in terms of X and Y coords."""

    def __init__(self, value, x=0, y=0):
        self._value = value
        self._x = x
        self._y = y

    def setX(self, coord: int):
        """Set a new value to coord X"""

        if not isinstance(coord, int):
            raise TypeError("The new value is not valid.")

        self._x = coord

    def setY(self, coord: int):
        """Set a new value to coord Y"""

        if not isinstance(coord, int):
            raise TypeError("The new value is not valid.")

        self._y = coord

    def coords(self):
        """Return a tuple with the x, y values."""
        return (self._x, self._y)

from mytree import MyTree

if __name__ == "__main__":

    tree = MyTree()

    one = tree.add_root(NumberWithCords(1))
    two = tree.add_children(one, NumberWithCords(2))
    three = tree.add_children(one, NumberWithCords(3))
    four = tree.add_children(two, NumberWithCords(4))
    five = tree.add_children(two, NumberWithCords(5))
    six = tree.add_children(three, NumberWithCords(6))
    seven = tree.add_children(three, NumberWithCords(7))
    eight = tree.add_children(four, NumberWithCords(8))
    nine  = tree.add_children(four, NumberWithCords(9))
    ten = tree.add_children(six, NumberWithCords(10))
    eleven = tree.add_children(six, NumberWithCords(11))
    twelve = tree.add_children(nine, NumberWithCords(12))
    thirdteen = tree.add_children(nine, NumberWithCords(13))

    layout = GeneralLayout(tree)
    layout._tour(tree.root(), 0, [])
    
