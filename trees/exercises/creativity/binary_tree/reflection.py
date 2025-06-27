"""
Given a proper binary tree T, define the reflection of T to be the binary tree T' such that each node v in T
is also in T', but the left child of v in T is v's right child in T' and the right child of v in T is v's left
child in T'.
Show that a preorder traversal of a proper bianry tree T is the same as the postorder traversal of T's reflection
but in reverse order.
"""

from binary_tree import LinkedBinaryTree

def reflection_tree(T, root, rT=None, rR=None):

    if rT:
        rtree = rT
        rroot = rR

    else:
        rtree = LinkedBinaryTree()
        rroot = rtree._add_root(root.element())

    left = T.left(root)
    right = T.right(root)
    if left:
        rright = rtree._add_right(rroot, left.element())
        reflection_tree(T, left, rtree, rright)

    if right:
        rleft = rtree._add_left(rroot, right.element())
        reflection_tree(T, right, rtree, rleft)

    return rtree

if __name__ == "__main__":

    tree = LinkedBinaryTree()
    root = tree._add_root(1)
    two = tree._add_left(root, 2)
    three = tree._add_right(root, 3)
    four = tree._add_left(two, 4)
    five = tree._add_right(two, 5)
    tree._add_left(four, 8)
    tree._add_right(four, 9)
    tree._add_left(three, 6)
    tree._add_right(three, 7)

    rtree = reflection_tree(tree, root)

    preorder = ''.join(
         str(c.element()) for c in tree.preorder()
    )

    postorder = [
        str(c.element()) for c in rtree.postorder()
    ]
    postorder.reverse()
    postorder = ''.join(postorder)

    if preorder == postorder:
        print("is the same.")
