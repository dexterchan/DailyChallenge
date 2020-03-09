#Hi, here's your problem today. This problem was recently asked by Twitter:

#Given a binary tree and an integer k, filter the binary tree such that its leaves don't contain the value k. Here are the rules:

#- If a leaf node has a value of k, remove it.
#- If a parent node has a value of k, and all of its children are removed, remove it.

#Here's an example and some starter code:
#Analysis
#dfs to the leaf with recursive function: func(node) -> boolean
# if leaf value is k, return true else false
#  if non leaf node
#  check return value of recursive function.... if yes, remove that child
#  if all children removed, and its value is k,
#  return true to its caller
#  else return false
# Time complexity O(N) Space complexity O(N) --- memory stack usage when doing recursion
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"value: {self.value}, left: ({self.left.__repr__()}), right: ({self.right.__repr__()})"

class Solution():
    def filter_recursive(self, node:Node,k:int)->bool:
        if node.left is None and node.right is None:
            return  node.value == k

        leftRet = True
        rightRet = True
        if node.left is not None:
            leftRet = self.filter_recursive(node.left, k)
        if node.right is not None:
            rightRet = self.filter_recursive(node.right, k)

        if leftRet:
            node.left = None
        if rightRet:
            node.right = None
        return leftRet and rightRet and node.value==k


def filter(tree, k):
    # Fill this in.
    solu = Solution()
    solu.filter_recursive(tree, k)
    return tree



if __name__ == "__main__":
    #     1
    #    / \
    #   1   1
    #  /   /
    # 2   1
    n5 = Node(2)
    n4 = Node(1)
    n3 = Node(1, n4)
    n2 = Node(1, n5)
    n1 = Node(1, n2, n3)

    print(str(filter(n1, 1)))
    #     1
    #    /
    #   1
    #  /
    # 2
    # value: 1, left: (value: 1, left: (value: 2, left: (None), right: (None)), right: (None)), right: (None)