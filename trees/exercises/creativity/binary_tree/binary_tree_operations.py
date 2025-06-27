"""
Design algorithms for the following operations for a binary tree T:
* preorder_next(p): Return the position visited after p in a preorder traversal of T (or None if p is the last node visited).
* inorder_next(p): Return the position visited after p in an inorder traversal of T (or None if p is the last node visited).
* postorder_next(p): Return the position visited after p in a postorder traversal of T (or None if p is the last node visited).
What are the worst-case running time of your algorithms?
"""
from binary_tree import LinkedBinaryTree

def preorder_next(T, p):
    """Return the position visited after p in a preorder traversal of T.
    None if p is the last position."""

    left = T.left(p)
    right = T.right(p)
    # if internal node, the next is some of its children
    if left:
        return left.element()

    elif right:
        return right.element()

    # if is external node
    # if left child, the next is its brother if it has.
    # otherwise its an ancestor if it has.

    else:
        parent = T.parent(p)
        if parent:
            # getting brother if any.
            sibling = T.sibling(p)
            if T.left(parent) == p and sibling:
                    return sibling.element()

            else:
                uncle = find_uncle(T, p)
                return uncle.element() if uncle else None

def inorder_next(T, p):
    """Return the position visited after p in an inorder traversal of T.
    None if p is the last position."""

    # if internal node, the right child leftmost descendant or a parent with only a right child.
    right = T.right(p)
    if right:
        return leftmostchild(T, right).element()

    # if left child, next is its father. otherwise next is the acenstor that has a right child.
    parent = T.parent(p)
    if parent:
        if T.left(parent) == p:
            return parent.element()

        else:
            next = right_subtree_ancestor(T, p)
            return next.element() if next else None

    return None

def postorder_next(T, p):
    """Return the position visited after p in a postorder traversal of T.
    None if p is the last position."""

    # in postorder, next of every left node is its sibling or one of its descendants, if any.
    # otherwise its father
    parent = T.parent(p)
    if parent and T.left(parent) == p:
        next = T.right(parent)            
        if next:
            return first_leaf_of(T, next).element()

    return parent.element() if parent else None



#----------------- Sup methods --------------------------#
def leftmostchild(T, p):
    """Return the mostleft child of p in a tree T."""

    while T.left(p):
        p = T.left(p)                        
    return p

def find_uncle(T, p):
    parent = T.parent(p)
    while parent != T.root():
        uncle = T.right(T.parent(parent))
        if uncle and uncle != parent:
            return uncle
        parent = T.parent(parent)
    return None

def right_subtree_ancestor(T, p):
    """Return the ancestor of p that has a right subtree.
    None if not any."""

    parent = T.parent(p)
    ancestor = T.parent(parent)
    while ancestor and T.right(ancestor) == parent:
        parent = ancestor
        ancestor = T.parent(ancestor)
    return ancestor

def first_leaf_of(T, p):
    """Return the first leaf found in the subtree p."""

    while T.num_children(p) > 0:
        left_child = T.left(p)            
        right_child = T.right(p)
        if left_child:
            p = left_child
        else:
            p = right_child

    return p

if __name__ == "__main__":
    tree = LinkedBinaryTree()
    tree2 = LinkedBinaryTree()
    tree3 = LinkedBinaryTree()
    tree4 = LinkedBinaryTree()

    # tree 1
    root1 = tree._add_root(1)
    two1 = tree._add_left(root1, 2)
    three1 = tree._add_right(root1, 3)
    four1 = tree._add_left(two1, 4)
    five1 = tree._add_right(two1, 5)
    seven1 = tree._add_left(five1, 7)
    eight = tree._add_right(five1, 8)
    nine = tree._add_left(eight, 9)

    #tree 2
    root2 = tree2._add_root(1)
    two2 = tree2._add_left(root2, 2)
    three2 = tree2._add_left(two2, 3)
    four2 = tree2._add_left(three2, 4)
    five2 = tree2._add_right(two2, 5)

    #tree 3
    root3 = tree3._add_root(1)
    two3 = tree3._add_right(root3, 2)
    three3 = tree3._add_left(two3, 3)
    four3 = tree3._add_right(two3, 4)
    five3 = tree3._add_right(three3, 5)
    six3 = tree3._add_right(four3, 6)
    tree3._add_left(five3, 9)
    tree3._add_right(five3, 8)

    #tree 4
    root4 = tree4._add_root(1)
    two4 = tree4._add_left(root4, 2)
    three4 = tree4._add_right(root4, 3)
    four4 = tree4._add_left(two4, 4)
    five4 = tree4._add_right(two4, 5)
    six4 = tree4._add_left(three4, 6)
    seven4 = tree4._add_right(three4, 7)
    tree4._add_left(four4, 8)
    tree4._add_right(four4, 9)
    tree4._add_left(five4, 10)
    tree4._add_right(five4, 11)

    print("preorder")
    print("tree 1")
    #print(f"testing 2, next must be: 4. is {preorder_next(tree, two1)}")
    #print(f"testing 3, next must be: N. is {preorder_next(tree, three1)}")
    #print(f"testing 5, next must be: 3. is {preorder_next(tree, five1)}")
    for c in tree.preorder():
        print(f"{c.element()}, next is: {preorder_next(tree, c)}")
    print('\n')
    print("tree 2")
    #print(f"testing 4, next must be: N. is {preorder_next(tree2, four2)}")
    #print(f"testing 1, next must be: 2. is {preorder_next(tree2, root2)}")
    #print(f"testing 3, next must be: 4. is {preorder_next(tree2, three2)}")
    for c in tree2.preorder():
        print(f"{c.element()}, next is: {preorder_next(tree2, c)}")
    print('\n')
    print("tree 3")
    #print(f"testing 1, next must be: 2. is {preorder_next(tree3, root3)}")
    #print(f"testing 4, next must be: 6. is {preorder_next(tree3, four3)}")
    #print(f"testing 2, next must be: 3. is {preorder_next(tree3, two3)}")
    for c in tree3.preorder():
        print(f"{c.element()}, next is: {preorder_next(tree3, c)}")
    print('\n')
    print("tree 4")
    #print(f"testing 6, next must be: 7. is {preorder_next(tree4, six4)}")
    #print(f"testing 3, next must be: 6. is {preorder_next(tree4, three4)}")
    #print(f"testing 2, next must be: 4. is {preorder_next(tree4, two4)}")
    for c in tree4.preorder():
        print(f"{c.element()}, next is: {preorder_next(tree4, c)}")
    print('-'*20)

    print("inorder")
    print("tree 1")
    #print(f"testing 2, next must be: 5. is {inorder_next(tree, two1)}")
    #print(f"testing 3, next must be: N. is {inorder_next(tree, three1)}")
    #print(f"testing 5, next must be: 1. is {inorder_next(tree, five1)}")
    for c in tree.inorder():
        print(f"{c.element()}, next is: {inorder_next(tree, c)}")
    print('\n')
    print("tree 2")
    #print(f"testing 4, next must be: 3. is {inorder_next(tree2, four2)}")
    #print(f"testing 3, next must be: 2. is {inorder_next(tree2, three2)}")
    #print(f"testing 2, next must be: 1. is {inorder_next(tree2, two2)}")
    for c in tree2.inorder():
        print(f"{c.element()}, next is: {inorder_next(tree2, c)}")
    print('\n')
    print("tree 3")
    #print(f"testing 5, next must be: 2. is {inorder_next(tree3, five3)}")
    #print(f"testing 6, next must be: N. is {inorder_next(tree3, six3)}")
    #print(f"testing 2, next must be: 4. is {inorder_next(tree3, two3)}")
    for c in tree3.inorder():
        print(f"{c.element()}, next is: {inorder_next(tree3, c)}")
    print('\n')
    print("tree 4")
    #print(f"testing 6, next must be: 3. is {inorder_next(tree4, six4)}")
    #print(f"testing 3, next must be: 7. is {inorder_next(tree4, three4)}")
    #print(f"testing 7, next must be: N. is {inorder_next(tree4, seven4)}")
    for c in tree4.inorder():
        print(f"{c.element()}, next is: {inorder_next(tree4, c)}")
    print('-'*20)

    print("postorder")
    print("tree 1")
    #print(f"testing 2, next must be: 3. is {postorder_next(tree, two1)}")
    #print(f"testing 3, next must be: 1. is {postorder_next(tree, three1)}")
    #print(f"testing 5, next must be: 2. is {postorder_next(tree, five1)}")
    for c in tree.postorder():
        print(f"{c.element()}, next is: {postorder_next(tree, c)}")
    print('\n')
    print("tree 2")
    #print(f"testing 1, next must be: N. is {postorder_next(tree2, root2)}")
    #print(f"testing 3, next must be: 2. is {postorder_next(tree2, three2)}")
    #print(f"testing 2, next must be: 1. is {postorder_next(tree2, two2)}")
    for c in tree2.postorder():
        print(f"{c.element()}, next is: {postorder_next(tree2, c)}")
    print('\n')
    print("tree 3")
    #print(f"testing 3, next must be: 4. is {postorder_next(tree3, three3)}")
    #print(f"testing 4, next must be: 2. is {postorder_next(tree3, four3)}")
    #print(f"testing 2, next must be: 1. is {postorder_next(tree3, two3)}")
    for c in tree3.postorder():
        print(f"{c.element()}, next is: {postorder_next(tree3, c)}")
    print('\n')
    print("tree 4")
    #print(f"testing 6, next must be: 7. is {postorder_next(tree4, six4)}")
    #print(f"testing 3, next must be: 1. is {postorder_next(tree4, three4)}")
    #print(f"testing 2, next must be: 3. is {postorder_next(tree4, two4)}")
    for c in tree4.postorder():
        print(f"{c.element()}, next is: {postorder_next(tree4, c)}")
    
