
#You are given the root of a binary tree. Find the level for the binary tree with the minimum sum, and return that value.

#For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7. So, the answer here should be 7.

#Analysis
#Depth first search
# enter a node DFS(node, d, MAP)
# find the depth (d), increment node.value with MAP[d] = MAP[d] + node.value
# if there is children, navigate to next level, DBS (node.child, d + 1)

#Navigate all keys of MAP to find min sum
from collections import defaultdict
class Node:
  def __init__(self, value, left=None, right=None):
    self.val = value
    self.left = left
    self.right = right

class Solution():
    def minimum_level_sum(self, root):
        MAP = defaultdict(int)
        self.__dfs(root, 0, MAP)
        minValue = (1<<31)-1

        for k in MAP.keys():
            if MAP[k] < minValue:
                minValue = MAP[k]
        return minValue

    def __dfs(self, node, d, MAP):
        if node is None:
            return
        v = MAP[d]
        MAP[d] = v + node.val
        if node.left is not None:
            self.__dfs(node.left, d+1, MAP)
        if node.right is not None:
            self.__dfs(node.right, d+1, MAP)
        return

def minimum_level_sum(root):
    solu = Solution()
    return solu.minimum_level_sum(root)

if __name__ == "__main__":
    #     10
    #    /  \
    #   2    8
    #  / \    \
    # 4   1    2
    node = Node(10)
    node.left = Node(2)
    node.right = Node(8)
    node.left.left = Node(4)
    node.left.right = Node(1)
    node.right.right = Node(2)

    print (minimum_level_sum(node))