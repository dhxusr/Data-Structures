"""
Let T be a binary tree with n positions, and for any position p in T, let dp denote the depth of p in T.
The distance between two positions p and q in T is dp + dq - 2da, where a is the lowest common ancestor(LCA)
of p and q. The diameter of T is the maximum distance between two positions in T. Describe an efficient algorithm
for finding the diameter of T. What is the running time of your algorithm?
"""

def diameter_of_tree(T, root):
    """Return the diameter of T."""

    if root is None:
        return (0, 0)

    if T.is_leaf(root):
        return (0, 1)

    left_diameter, left_height = diameter_of_tree(T, T.left(root))
    right_diameter, right_height = diameter_of_tree(T, T.right(root))
    diameter = max(right_diameter, left_diameter, left_height + right_height)
    height = max(right_height, left_height)
    
    return (diameter, height+1)


from binary_tree import LinkedBinaryTree

if __name__ == "__main__":

    tree = LinkedBinaryTree()
    root = tree._add_root(1)
    left = tree._add_left(root, 2)
    right = tree._add_right(root, 3)
    tree._add_right(right, 6)

    right = tree._add_right(left, 5)
    tree._add_right(right, 22)
    left = tree._add_left(left, 4)
    tree._add_right(left, 8)
    left = tree._add_left(left, 7)
    right = tree._add_right(left, 12)
    tree._add_left(left, 11)
    tree._add_left(right, 20)
    right = tree._add_right(right, 99)
    tree._add_right(right, 77)

    diameter, _ = diameter_of_tree(tree, root)
    print("diameter of tree:", diameter)
