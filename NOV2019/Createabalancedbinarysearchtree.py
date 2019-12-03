#Skills : BST
#Given a sorted list of numbers, change it into a balanced binary search tree. You can assume there will be no duplicate numbers in the list.

#Here's a starting point:

from collections import deque

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    # level-by-level pretty-printer
    nodes = deque([self])
    answer = ''
    while len(nodes):
      node = nodes.popleft()
      if not node:
        continue
      answer += str(node.value)
      nodes.append(node.left)
      nodes.append(node.right)
    return answer



class Solution():
    def createBalanceBSTFromSortedNumsArray(self, sortedNum):
        start = 0
        end = len(sortedNum)
        return self.__bsthelper(sortedNum, start, end)

    def __bsthelper(self, nums, start, end):
        if start>=end-1:
            return Node(nums[start])
        elif start>end:
            return None
        mid = int ((start + end)/2 )

        leftNode = None
        rightNode = None
        leftNode = self.__bsthelper(nums, start, mid)
        if mid+1!=end:
            rightNode = self.__bsthelper(nums, mid+1, end)

        n = Node(nums[mid], leftNode, rightNode)
        return n

def createBalancedBST(nums):
    solu = Solution()
    return solu.createBalanceBSTFromSortedNumsArray(nums)

if __name__ == "__main__":
    print ( createBalancedBST([1, 2, 3, 4, 5, 6, 7]) )
    print(createBalancedBST([1, 2, 3, 4, 5]))
# 4261357
#   4
#  / \
# 2   6
#/ \ / \
#1 3 5 7