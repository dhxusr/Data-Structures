"""
Suppose each position p of a binary tree T is labeled with its value f(p) in a level numbering of T.
Design a fast method for determining f(a) for the lowest common ancestor (LCA), a, of two positions p and q in T,
given f(p) and f(q). You don't need to find position a, just value f(a).
"""

def value_of_lca(f, dp, dq):

    """
    f: level function → value of p
    dp: depth of p
    dq: depth of q
    return: f(a) where a is the LCA of p and q
    """

    while dp > dq:
        dp -= 1
    while dq > dp:
        dq -= 1
    
    while dp != dq:
        dp -= 1
        dq -= 1

    return f(dp)
