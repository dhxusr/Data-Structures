"""
Let T be a tree with n positions. Define the lowest common ancestor (LCA) between two positions p and q as the
lowest position in T that has both p and q as descendants (where we allow a position to be a descendant of itself).
Given two positions p and q, describe an efficient algorithm for finding the LCA of p and q. what is the running
time of your algorithm?
"""

""""""
def lowest_common_ancestor(T, p, q):
    """Find the lowest common ancestor of p and q."""

    p_parent = T.parent(p)
    q_parent = T.parent(q)
    if  p_parent == q_parent:
        return p_parent

    elif p_parent == q:
        return q

    elif q_parent == p:
        return p
        
    else:

        p_d = T.depth(p)
        q_d = T.depth(q)
        # search from the uppest position to check if the other node is descendant.
        ancestor = p if p_d < q_d else q
        descendant = q if ancestor == p else p
        checked = None

        # this loop goes from the uppest between p or q, untill root in the worst case
        while not check_descendant(T, ancestor, descendant, checked):
            checked = ancestor
            ancestor = T.parent(ancestor)
            if ancestor == T.root():
                break
        return ancestor
    
def check_descendant(tree, root, descendant, checked_child=None):
    """Check if descendat is part of the subtree rooted at root.
    checked_child is a child of root that has been checked."""

    for c in tree.children(root):
        if checked_child and checked_child != c:
            for desc in tree._subtree_preorder(c):
                if desc == descendant:
                    return True


    return False

# better implementation
# parallel search
def lca(T, p, q):

    dp = T.depth(p)
    dq = T.depth(q)

    while dp > dq:
        p = T.parent(p)
        dp -= 1

    while dq > dp:
        q = T.parent(q)
        dq -= 1

    while p != q:
        p = T.parent(p)
        q = T.parent(q)

    return p

from mytree import MyTree
if __name__ == "__main__":
    tree = MyTree()

    root = tree.add_root(1)
    two = tree.add_children(root, 2)
    three = tree.add_children(root, 3)
    four = tree.add_children(two, 4)
    five = tree.add_children(two, 5)
    eight = tree.add_children(four, 8)
    nine = tree.add_children(four, 9)
    twelve = tree.add_children(nine, 12)
    thirdteen = tree.add_children(nine, 13)

    six = tree.add_children(three, 6)
    seven = tree.add_children(three, 7)
    ten = tree.add_children(six, 10)
    eleven = tree.add_children(six, 11)

    lca = lowest_common_ancestor(tree, five, thirdteen)
    print("lowest common ancestor:", lca.element())
