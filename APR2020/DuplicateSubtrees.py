
#Given a binary tree, find all duplicate subtrees (subtrees with the same value and same structure)
# and return them as a list of list [subtree1, subtree2, ...] where subtree1 is a duplicate of subtree2 etc.

#Here's an example and some starter code:
#Algorithm
#encode each node with DFS,
#each node is encoded as
# Code = (value, left child, right child, height)
# left child and right child is also in structure Code
# height defined by max(left child, right child) + 1
#Code can be represented by a label
# each label registered into Map (List of ( Node) )
# in the each, iterate the map to find list length > 1

from collections import defaultdict
from typing import List

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

class Code:
    def __init__(self, value:int, leftChild, rightChild ):
        self.value = value
        self.leftChild = leftChild
        self.rightChild = rightChild
        if leftChild is None and rightChild is None:
            self.height = 0
        elif leftChild is None:
            self.height = rightChild.height + 1
        elif rightChild is None:
            self.height = leftChild.height + 1
        else:
            self.height = max(leftChild.height, rightChild.height) + 1

    def __str__(self):
        return f"({self.value},{self.height},{str(self.leftChild)},{str(self.rightChild)})"

class Solution():
    def dup_trees(self, root):
        CodeMap = defaultdict(list)
        self.__dfs(root, CodeMap)
        res = []
        for _, listNodes in CodeMap.items():
            if len(listNodes) > 1:
                ll = []
                for node in listNodes:
                    ll.append(str(node))
                res.append(ll)
        return res


    def __dfs(self, root, CodeMap)->Code:
        if root.left is None and root.right is None:
            code = Code(root.value, None, None)
            key = str(code)
            CodeMap[key].append(root)
            return code

        leftcode=rightcode=None
        if root.left is not None:
            leftcode = self.__dfs(root.left, CodeMap)
        if root.right is not None:
            rightcode = self.__dfs(root.right, CodeMap)

        code = Code(root.value, leftcode, rightcode)
        key = str(code)
        CodeMap[key].append(root)
        return code



def dup_trees(root):
    # Fill this in.
    solu = Solution()
    return solu.dup_trees(root)


if __name__ == "__main__":
    n3_1 = Node(3)
    n2_1 = Node(2, n3_1)
    n3_2 = Node(3)
    n2_2 = Node(2, n3_2)
    n1 = Node(1, n2_1, n2_2)
    # Looks like
    #     1
    #    / \
    #   2   2
    #  /   /
    # 3   3

    print(dup_trees(n1))
    # [[(3), (3)], [(2, (3)), (2, (3))]]
    # There are two duplicate trees
    #
    #     2
    #    /
    #   3
    # and just the leaf
    #
    # 3