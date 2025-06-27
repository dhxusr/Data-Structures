"""
The path length of a tree T is the sum of the depths of all positions in T.
Describe a linear-time method for computing the path length of a tree T.
"""

def path_length(T, root, depth=0) -> int:
    """linear-time method for computing the path lenght of a tree T."""

    if T.is_leaf(root):
        return depth

    path_lengths = [path_length(T, c, depth+1) for c in T.children(root)]
    return sum(path_lengths)

from mytree import MyTree

if __name__ == "__main__":
    tree = MyTree()
    root = tree.add_root(1)
    one_three = [
        tree.add_children(root, i) for i in range(2, 5)
    ]
    five = tree.add_children(one_three[0], 5)
    six = tree.add_children(one_three[0], 6)
    tree.add_children(five, 11)
    for i in range(12, 15):
        tree.add_children(six, i)

    tree.add_children(one_three[1], 7)
    nine = None
    for i in range(8, 11):
        p = tree.add_children(one_three[2], i)
        if i == 9:
            nine = p

    tree.add_children(nine, 15)
    tree.add_children(nine, 16)

    print("path length of tree")
    print(path_length(tree, root))
