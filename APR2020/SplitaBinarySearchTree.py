
#Given a binary search tree (BST) and a value s, split the BST into 2 trees,
# where one tree has all values less than or equal to s,
# and the other tree has all values greater than s while maintaining
# the tree structure of the original BST.
# You can assume that s will be one of the node's value in the BST. Return both tree's root node as a tuple.

#Here's an example and some starting code:
#Algorithm
#search the tree for value s, record the path from root to s with a stack
#after finding s, backtrace the path for direction
# if parent of s > s, parent of s of s > parent of s... keep going until,
# we find parent of sss < parent ss... then we find the break point
# then we assign child to the break point


class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __repr__(self):
    if self.left and self.right:
      return f"({self.value}, {self.left}, {self.right})"
    if self.left:
      return f"({self.value}, {self.left})"
    if self.right:
      return f"({self.value}, None, {self.right})"
    return f"({self.value})"


class Solution:
  def split_bst(self, bst, s):
    backtrace = []
    self.__search_s(bst, s ,backtrace)
    node = backtrace[-1]
    pivot, pivotParent = self.__findPivot(backtrace)

    if pivotParent is None:
      return (pivot, None)

    cut = None
    if pivot.value < node.value:
      cut = node.right
      node.right = None
    else:
      cut = node.left
      node.left = None

    if pivotParent.left == pivot:
      pivotParent.left = cut
    else:
      pivotParent.right = cut

    return (pivot, pivotParent)
  def __findPivot(self, backTrace):
    v = backTrace.pop()
    if len(backTrace) == 0 :
      return v, None
    p = backTrace.pop()
    vLargerThanParent = v.value > p.value
    checkDirection = vLargerThanParent
    while (len(backTrace)>0 and checkDirection == vLargerThanParent):
      v = p
      p = backTrace.pop()
      checkDirection = v.value > p.value
    return v, p

  def __search_s(self, bst:Node , s, backTrace:list):
    if bst is None:
      raise Exception("s not found")
    backTrace.append(bst)
    if bst.value == s:
      return
    elif bst.value < s:
      return self.__search_s(bst.right, s, backTrace)
    elif bst.value > s:
      return self.__search_s(bst.left,s, backTrace)

def split_bst(bst, s):
  # Fill this in.
  solu = Solution()
  return solu.split_bst(bst, s)


if __name__ == "__main__":
  n2 = Node(2)
  n1 = Node(1, None, n2)

  n5 = Node(5)
  n4 = Node(4, None, n5)

  root = Node(3, n1, n4)

  print(root)
  # (3, (1, (2)), (4, None, (5)))
  # How the tree looks like
  #     3
  #   /   \
  #  1     4
  #   \     \
  #    2     5

  #print(split_bst(root, 2))
  tu = split_bst(root, 2)
  print ( list(map ( lambda x :str(x), tu )))

  # ((1, None, (2)), (3, None, (4, None, (5))))
  # Split into two trees
  # 1    And   3
  #  \          \
  #   2          4
  #               \
  #                5

  n3 = Node(3)
  n2 = Node(2, None, n3)
  n1 = Node(1, None, n2)

  n6 = Node(6)
  n5 = Node(5, None, n6)

  root = Node(4, n1, n5)
  print(root)
  print(split_bst(root, 2))