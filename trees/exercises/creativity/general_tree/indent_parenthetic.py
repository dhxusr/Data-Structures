"""
The idented parenthetic representation of a tree T is a variation of the parenthetic representation of T' that
uses indentation and line breaks as in Figure.
Give an algorithm that prints this representation of a tree.

T':
def parenthesize(T, p, indent=0):
  Print parenthesized representation of subtree of T rooted at p.
  print('\t'*indent, p.element(), end='')
  if not T.is_leaf(p):
    first_time = True
    for c in T.children(p):
      sep = ' (' if first_time else '\n'
      print(sep, end='')
      first_time = False
      parenthesize(T, c, indent+1)
    print('\t'*indent, ')', end='')


Figure:

                   (sales)
                      |
            --------------------
           |                    |
       (Domestic)          (international)
                                  |
                     ---------------------------
                    |             |             |
                (Canada)      (S.Ameria)    (Overseas)
                                                |
                                    --------------------------
                                   |        |        |        |
                                (Africa) (Europe) (Asia) (Australia)



Sales (
    Domestic
    International(
        Canada
        America
        Overseas (
            Africa
            Europe
            Asia
            Australia
        )
    )
)
"""

def parenthesize(T, p, indent=0):
  """Print parenthesized representation of subtree of T rooted at p."""
  print(' '*indent*2, p.element(), end='')
  if not T.is_leaf(p):
    first_time = True
    c = None
    for c in T.children(p):
        sep = ' (' if first_time else None
        print(sep)
        first_time = False
        parenthesize(T, c, indent+1)
    if T.is_leaf(c):
        print('')
    print(' '*indent*2, ')')


from mytree import MyTree

if __name__ == "__main__":

    tree = MyTree()
    root = tree.add_root("Sales")
    tree.add_children(root, "Domestic")
    inter = tree.add_children(root, "International")
    tree.add_children(inter, "Canada")
    tree.add_children(inter, "S.America")
    over = tree.add_children(inter, "Overseas")
    tree.add_children(over, "Africa")
    tree.add_children(over, "Europe")
    tree.add_children(over, "Asia")
    tree.add_children(over, "Australia")

    parenthesize(tree, root)
