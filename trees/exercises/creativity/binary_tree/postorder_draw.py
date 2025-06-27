"""
Algorithm postorder_draw draws a binary tree T by assigning x- and y- coordinates to each position p such that
x(p) is the number of nodes preceding p in the postorder traversal of T and y(p) is the depth of p in T.

a. Show that the drawing of T produced by postorder_draw has no pairs of crossing edges
b. Redraw the binary tree using preorder_draw.

                            (1)
                     ---------------
                    |               |
                   (2)             (3)
                  ----             ----
                 |    |           |    | 
                (4)  [5]         (6)  [7]
               ----             ----    
              |    |           |    |
             [8]  (9)         [10] [11]
                  ----
                 |    |
                [12] [13]



[] = external nodes
() = internal nodes


    y                                               (1)
    |
1 -                         (2)                 (3)
    |
2 -                 (4) [5]             (6) [7]
    |
3 - [8]         (9)             [10][11]  
    |
4 -    [12] [13]
    |
    x---|---|---|---|---|---|---|---|---|---|---|---|--- 
       1    2   3   4   5   6   7   8   9   10  11  12
"""
