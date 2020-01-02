
#Given a binary tree, remove the nodes in which there is only 1 child, so that the binary tree is a full binary tree.

#So leaf nodes with no children should be kept, and nodes with 2 children should be kept as well.

#Here's a starting point:

#Analysis
#Start from depth first search
#Beginning from the head node
# insert tuple (node, parent) into stack, for head node, parent is None
#
# if no child, skip
#  next , check if node exist in memory (set), if no, insert all child into stack and insert into set and skip
# if yes, run below filter logic:
# check if node has only one child
# if yes, find parent node and replace the node with that only child (by comparing parent left and right)
# if no, append (left child, node), (right child, node) into stack
# pop of stack for next item

from collections import deque

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.left = left
    self.right = right
    self.value = value
  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      num = len(q)
      while num > 0:
        n = q.popleft()
        result += str(n.value)
        if n.left:
          q.append(n.left)
        if n.right:
          q.append(n.right)
        num = num - 1
      if len(q):
        result += "\n"

    return result

class Solution:
    def fullBinaryTree(self, node):
        q = []
        q.append((node, None))
        s = set()
        while len(q) > 0:
            cur, parent = q[-1]
            if cur.left is None and cur.right is None:
                q.pop()
                continue
            if cur not in s:
                if cur.left is not None:
                    q.append((cur.left, cur))
                if cur.right is not None:
                    q.append((cur.right, cur))
                s.add(cur)
                continue
            self.__filterNode(cur, parent)
            q.pop()
        return node

    def __filterNode(self, cur, parent):
        if cur.left is not None and cur.right is not None:
            return
        if parent is None:
            return
        child = None
        if cur.left is not None:
            child = cur.left
        if cur.right is not None:
            child = cur.right

        if parent.left == cur:
            parent.left = child
        if parent.right == cur:
            parent.right = child
        return



def fullBinaryTree(node):
    # Fill this in.
    solu = Solution()
    return solu.fullBinaryTree(node)

# Given this tree:
#     1
#    / \
#   2   3
#  /   / \
# 0   9   4

# We want a tree like:
#     1
#    / \
#   0   3
#      / \
#     9   4

if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.right.right = Node(4)
    tree.right.left = Node(9)
    tree.left.left = Node(0)
    print (fullBinaryTree(tree))
    # 1
    # 03
    # 94

    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.right.left = Node(9)
    tree.left.left = Node(0)
    print(fullBinaryTree(tree))
    # 1
    # 03
    # 94