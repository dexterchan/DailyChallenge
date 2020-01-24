#You are given the root of a binary tree, along with two nodes, A and B. Find and return the lowest common ancestor of A and B.
# For this problem, you can assume that each node also has a pointer to its parent, along with its left and right child.

#Analysis
# Search for all ancestor node of a into a Set (S)
# start for b, iterate each ancestor and check if ancestor in S
# if match, it is the lowest common ancestor

class TreeNode:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.parent = None
    self.val = val


def lowestCommonAncestor(root, a, b):
    S = set()
    ancestor = a
    lca = None
    while ancestor is not None:
        S.add(ancestor)
        ancestor = ancestor.parent
    ancestor = b
    while ancestor is not None:
        if ancestor in S:
            lca = ancestor
            break
        ancestor = ancestor.parent

    return lca


if __name__ == "__main__":
    #   a
    #  / \
    # b   c
    #    / \
    #   d*  e*
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.left.parent = root
    root.right = TreeNode('c')
    root.right.parent = root
    a = root.right.left = TreeNode('d')
    root.right.left.parent = root.right
    b = root.right.right = TreeNode('e')
    root.right.right.parent = root.right

    print (lowestCommonAncestor(root, a, b).val)
    # c