"""
Two ordered trees T' and T'' are said to be isomorphic if one of the following holds:
* both T' and T'' are empty.
* The roots of T' and T'' have the same number k >= 0 of subtrees, and the ith such subtree of T' is isomorphic
to the ith such subtree of T'' for i=1,...,k.

Design an algorithm that tests whether two given ordered trees are isomorphic. What is the running time of your
algorithm?

two trees are isomorphic if both have the same structure.
"""

from mytree import MyTree

def are_isomorphic(T, T2) -> bool:
    """Return True if tree T and tree T2 are isomorphic."""

    if T.is_empty() and T2.is_empty():
        return True    

    else:
        root1 = T.root()
        root2 = T2.root()
        num_children = T.num_children(root1)
        if num_children == T2.num_children(root2):
            children1 = T.children(root1)
            children2 = T2.children(root2)
            for _ in range(num_children):
                t = MyTree(next(children1))
                t2 = MyTree(next(children2))
                if not are_isomorphic(t, t2):
                    return False

            return True

        else:
            return False

if __name__ == "__main__":

    T = MyTree()
    one = T.add_root(1)
    two = T.add_children(one, 2)
    T.add_children(one, 3)
    T.add_children(two, 4)
    #T.add_children(two, 5)

    T2 = MyTree()
    six = T2.add_root(6)
    seven = T2.add_children(six, 7)
    T2.add_children(six, 8)
    T2.add_children(seven, 9)
    T2.add_children(seven, 10)

    print("are isomorphic: ", are_isomorphic(T, T2))
