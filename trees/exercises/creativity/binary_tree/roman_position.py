"""
Let T be a binary tree with n positions. Define a Roman position to be a position p in T, such that the number
of descendants in p's left subtree differ from the number of descendants in p's right subtree by at most 5.
Describe a linear-time method for finding each position p of T, such that p is not a Roman position, but
all of p's descendants are Roman.
"""

def all_descendants_roman(T, p, result):
    """Find each position p of T, such that p is not Roman, but
    all of p's descendants are Roman.
    return a tuple with the result if all descendants are roman
    and the number of descendants.
    """

    if T.is_leaf(p):
        return (True, 1)

    left_child = T.left(p)
    right_child = T.right(p)

    if left_child:
        left_result = all_descendants_roman(T, left_child, result) 
    else:
        left_result = (True, 0)

    if right_child is not None:
        right_result = all_descendants_roman(T, right_child, result)
    else:
        right_result = (True, 0)

    difference = abs(left_result[1] - right_result[1])
    number_of_descendants = left_result[1] + right_result[1] + 1

    roman = True if difference <= 5 else False
    if not roman and left_result[0] and right_result[0]:
        result.append(p)

    return (roman, number_of_descendants) 


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

    result = []
    all_descendants_roman(tree, root, result)
    for p in result:
        print(p.element(), "is valid.")
