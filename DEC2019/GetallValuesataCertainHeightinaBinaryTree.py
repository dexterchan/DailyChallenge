
#Given a binary tree, return all values given a certain height h.

#Here's a starting point:

from collections import deque

class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class InvalidNodeException (Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

#Cost: O(N) Space O(N)
class Solution:

    def valuesAtHeight(self, root, height):
        res = []

        #self.__valuesAtHeightRecursive(root, height, res, 1)
        self.__valuesAtHeightIterative(root, height, res)

        return res

    def __valuesAtHeightRecursive(self, node, height, resultLst, curHeight):
        if node == None:
            raise InvalidNodeException("Invalid node as None")
        if curHeight == height:
            resultLst.append(node.value)
            return
        if curHeight < height:
            if node.left is not None:
                self.__valuesAtHeightRecursive(node.left, height, resultLst, curHeight + 1)
            if node.right is not None:
                self.__valuesAtHeightRecursive(node.right, height, resultLst, curHeight + 1)
            return
        if curHeight > height:
            return
    def __valuesAtHeightIterative(self, root, height, resultLst ):
        node = root
        queue = deque()
        queue.append(node)

        heightMap={}
        heightMap[node] = 1

        while len(queue)>0:
            node = queue.popleft()
            if node not in heightMap:
                raise  InvalidNodeException("Failed to find height of node %d" % (node.value))

            myHeight = heightMap[node]
            if  myHeight == height:
                resultLst.append(node.value)
                continue
            elif myHeight < height:
                if node.left is not None:
                    heightMap[node.left] = myHeight + 1
                    queue.append(node.left)
                if node.right is not None:
                    heightMap[node.right] = myHeight + 1
                    queue.append(node.right)
            else:
                continue
        return




def valuesAtHeight(root, height):
    solu = Solution()
    return solu.valuesAtHeight(root, height)

#     1
#    / \
#   2   3
#  / \   \
# 4   5   7
if __name__ == "__main__":
    a = Node(1)
    a.left = Node(2)
    a.right = Node(3)
    a.left.left = Node(4)
    a.left.right = Node(5)
    a.right.right = Node(7)
    print (valuesAtHeight(a, 3))
    # [4, 5, 7]

    a = Node(1)
    a.left = Node(2)
    a.right = Node(3)
    a.left.left = Node(4)
    a.left.right = Node(5)
    a.right.right = Node(7)
    print (valuesAtHeight(a, 2))
