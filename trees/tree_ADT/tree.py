from collections import deque

class Tree:
    """Abstract base class representing a tree structure."""

    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

    # ----------- Abstracts methods that concrete subclass must be support ----------#
            
    def root(self):
        """Return the Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError("must be implemented by subclass.")

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError("must be implemented by subclass.")

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError("must be implemented by subclass.")

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotADirectoryError("must be implemented by subclass.")

    #---------- Concrete methods implemented in this class -----------#
    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def _subtree_preorder(self, p):
        """generate a preorder iteration of positions in subtree rooted at p."""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of position in subtre rooted at p."""                
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield p
        yield p

    def preorder(self):
        """Generate a preorder iteration of postions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def postorder(self):
        """Generate postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p
    
    def breadthfirst(self):
        """Generate a breadth-first iteration of positions of the tree."""
        if not self.is_empty():
            fringe = deque()
            fringe.append(self.root())
            while len(fringe) != 0:
                p = fringe.popleft()
                yield p
                fringe.extend(
                    c for c in self.children(p)
                )                    

    def preorder_indent(self, p, d):
        """Print preorder representation of subtree of T rooted at p at depth d."""
        print(2*d*' ' + str(p.element()))
        for c in self.children(p):
            self.preorder_indent(c, d+1)
            
    def positions(self):
        return self.preorder()

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not ahve any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

