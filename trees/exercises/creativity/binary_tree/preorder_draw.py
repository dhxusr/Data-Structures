"""
Algorithm preorder_draw draws a binary tree T by assigning x- and y- coordinates to each position p such that
x(p) is the number of nodes preceding p in the preorder traversal of T and y(p) is the depth of p in T.

a. Show that the drawing of T produced by preorder_draw has no pairs of crossing edges
b. Redraw the binary tree using preorder_draw.

                            ()
                     ---------------
                    |               |
                   ()               ()
                  ----             ----
                 |    |           |    | 
                ()    ()         ()    ()
               ----             ----    
              |    |           |    |
             ()    ()         ()    ()
                  ----
                 |    |
                ()    ()




 *
  \
   *                   *
    \                 / \
     *               *   *       *
      \             /     \     /
       * - *       /       * - *
            \     /
             * - *
"""

