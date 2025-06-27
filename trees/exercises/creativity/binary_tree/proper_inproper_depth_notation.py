"""
Let T be a (not necessarily proper) binary tree with n nodes, and let D be the sum of the depths of all the
external nodes of T. Show that if T has the minimum number of external nodes possible, then D is O(n) and if T
has the maximum number of external nodes possible, the D is (n log n).

Answer:
if the tree has the minimum number of external nodes possible, D has to traverse all the internal nodes before
that make the time complexity O(n)

if the tree has all the possible nodes then the tree has two subtrees both equals, so D just has to calculate
one subtree and then mulitplied by 2, so it doesn't traverse all the tree. that makes the time complexity
O(n log n)
"""
