# Skill: tree travsal
# difficulty: medium
#Given a number n, generate all binary search trees that can be constructed with nodes 1 to n.

#Here's some code to start with:
#ANalysis
#From N=1, iteratively grow BST from 1 to n
# For each N, create a template set of BST
# Each template, pick a pivot 1..K

#Time complexity : O(N^2) space complexity : O(N)
from typing import List
import copy

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    result = str(self.value)
    if self.left:
      result = result + str(self.left)
    if self.right:
      result = result + str(self.right)
    return result




class Solution():
  def generate_bst(self, n):
    templateMap = {}

    for i in range(1,n+1):
      newLst = self.__createTemplate(i, templateMap)
      templateMap[i] = newLst

    return templateMap[n]

  def __createTemplate(self, n, templateMap)->List[Node]:
    if n == 0:
      return []
    res = []
    if n in templateMap:
      return templateMap[n]
    for p in range(1, n+1):
      left = p-1
      right = n-p
      leftNodeLst = self.__createTemplate(left,templateMap)
      rightNodeLst = self.__createTemplate(right,templateMap)

      tempRes = []
      #LeftLst cross rightLst
      for leftNode in leftNodeLst:
        node = Node(p)
        lchild = copy.deepcopy(leftNode)
        node.left = lchild
        tempRes.append(node)

      if len(tempRes)==0:
        tempRes.append(Node(p))
      tempRes2 = []
      for leftNode in tempRes:
        for rightNode in rightNodeLst:
          rNode = copy.deepcopy(leftNode)
          node = copy.deepcopy(rightNode)
          self.__dfsadd(node, p)
          rNode.right = node
          tempRes2.append(rNode)

      if len(tempRes2)==0:
        res.extend(tempRes)
      else:
        res.extend(tempRes2)

    return res
  def __dfsadd(self, node, p):
    if node is None:
      return
    node.value += p
    if node.left is not None:
      self.__dfsadd(node.left, p)
    if node.right is not None:
      self.__dfsadd(node.right, p)




def generate_bst(n):
  # Fill this in.
  solu = Solution()
  return solu.generate_bst(n)

if __name__ == "__main__":


  for tree in generate_bst(3):
    print (tree)

  # Pre-order traversals of binary trees from 1 to n.
  # 123
  # 132
  # 213
  # 312
  # 321

#   1      1      2      3      3
#    \      \    / \    /      /
#     2      3  1   3  1      2
#      \    /           \    /
#       3  2             2  1
  for tree in generate_bst(5):
    print (tree)