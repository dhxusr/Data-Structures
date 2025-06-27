"""
Give an efficient algorithm that computes and prints, for every position p of a tree T, the element of p followed
by the height of p's subtree
"""

from mytree import MyTree

def subtree_height(T, root) -> int:
    """prints for every position p of a tree, the element of p followed by the
    height of p's subtree."""

    element = root.element()
    if T.is_leaf(root):
        print(element,':', 0)
        return 0

    child_heights = [subtree_height(T, c) for c in T.children(root)]
    height = max(child_heights) + 1
    print(element,':', height)
    return height
    

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

    print("hegiht of subtree")
    subtree_height(tree, root)
            
