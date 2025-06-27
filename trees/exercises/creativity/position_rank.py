"""
Let the rank of a position p during a traversal be defined such that the first element visited has rank 1, the
second element visited has rank 2, and so on. For each position p in a tree T,
- let pre(p) be the rank of p in a preorder traversal of T.
- let post(p) be the rank of p in a postorder traversal of T.
- let depth(p) be the depth of p.
- let desc(p) be the number of descendants of p, including p itself.

Dervie a formula defining post(p) in terms of desc(p), depth(p), and pre(p), for each node p in T.

the formula is: post = pre - (depth + 1) + desc

post(p) = pre(p) − (depth(p) + 1) + desc(p)

Here's the reasoning:
- The term depth(p) + 1 represents the number of nodes from the root to p, including p itself — in other words,
  p and all its ancestors.

- In preorder traversal, we visit p before any of its descendants, so pre(p) includes all ancestors of p,
p itself, and any nodes visited earlier.

- Subtracting depth(p) + 1 from pre(p) gives the number of nodes visited before entering the subtree rooted at p.

- In postorder traversal, all descendants of p are visited before p itself. Since desc(p) includes both p and
its descendants, it accounts for all visits within the subtree rooted at p.

- Therefore, adding desc(p) to pre(p) - (depth(p) + 1) gives the position of p in postorder traversal.
This formula captures how preorder and postorder are related through the structure of the tree and the position of p."""


    
    
