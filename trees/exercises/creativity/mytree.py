
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
        raise NotImplementedError("must be implemented by subclass.")

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
                yield other
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


class MyTree(Tree):

    class _Node:
        def __init__(self, element, parent=None):
            self.element = element
            self.parent = parent
            self.children = []
    
    class MyPosition:
        def __init__(self, node=None, container=None):
            self.node = node
            self.container = container

        def element(self):
            return self.node.element 

        def __eq__(self, other):
            return type(other) == type(self) and self.node is other.node

    def __init__(self, root=None):

        self._root = root
        self.size = 0 if not root else 1

    def root(self):
         return self._root           

    def parent(self, p):
        node = p.node
        return self.MyPosition(node.parent, self)     

    def num_children(self, p):
        node = p.node
        return len(node.children)

    def children(self, p):
        node = p.node
        for c in node.children:
            yield c

    def add_children(self, p, element) -> MyPosition:
        parent_node = p.node
        new_node = self.MyPosition(self._Node(element, parent_node), self)
        parent_node.children.append(new_node)
        self.size += 1
        return new_node

    def add_root(self, element):
        if self._root is None:
            new_node = self._Node(element)
            self._root = self.MyPosition(new_node, self)
            self.size += 1
            return self._root

    def __len__(self) -> int:
        return self.size

    def depth(self, p):
        depth = 0
        while p != self.root():        
            depth += 1
            p = self.parent(p)
        return depth
