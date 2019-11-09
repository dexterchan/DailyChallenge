#Skill : binary tree, recursive
#You are given the root of a binary tree. Invert the binary tree in place.
# That is, all left children should become right children, and all right children should become left children.

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
  def preorder(self):
    print (self.value, end=' ')
    if self.left: self.left.preorder()
    if self.right: self.right.preorder()
  def preorderOut(self, lst):
    lst.append(self.value)
    if self.left: self.left.preorderOut(lst)
    if self.right: self.right.preorderOut(lst)


def invert(node):
    # Fill this in.
    if (node == None):
        return node
    tmp = node.left
    node.left = invert(node.right)
    node.right = invert (tmp)
    return node


if __name__ == "__main__":
    root = Node('a')
    root.left = Node('b')
    root.right = Node('c')
    root.left.left = Node('d')
    root.left.right = Node('e')
    root.right.left = Node('f')


    outPutlst = []
    root.preorderOut(outPutlst)
    print (outPutlst)
    # a b d e c f
    outPutlst.clear()
    invert(root)
    root.preorderOut(outPutlst)
    # a c f b e d
    print(outPutlst)