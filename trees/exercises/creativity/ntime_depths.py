"""
Give an O(n)-time algorith for computing the depths of all positions of a tree T, where n is the number of nodes
"""

def each_node_depth(T, root, depth=0) -> None:
    """An O(n)-time algorithm for computing the depths of all positions of a tree T,
    where n is the number of nodes of T."""

    print(root.element(),':', depth)
    for c in T.children(root):
        each_node_depth(T, c, depth+1)


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

    print("eacho node depth")
    each_node_depth(tree, root)        
    
