#Skill: Depth First Search
#Difficulty: EASY
#You are given a binary tree representation of an arithmetic expression. In this tree, each leaf is an integer value,, and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.

#Write a function that takes this tree and evaluates the expression.

#Example:

#    *
#   / \
#  +    +
# / \  / \
#3  2  4  5

#This is a representation of the expression (3 + 2) * (4 + 5), and should return 45.

#Here's a starting point:

from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

class InvalidStateException (Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class Solution:
    def evaluateBTree(self, root):
        return self.__dfs_recursive(root)

    def __dfs_recursive(self, node)->int:
        if node.left is None and node.right is None:
            return node.val

        loperand = 0
        roperand = 0
        if node.left is not None:
            loperand = self.__dfs_recursive(node.left)
        else:
            raise InvalidStateException("Left node is null in a non leaf node")

        if node.right is not None:
            roperand = self.__dfs_recursive(node.right)
        else:
            raise InvalidStateException("Right node is null is a non leaft node")

        if node.val == PLUS:
            return loperand + roperand
        elif node.val == MINUS:
            return loperand - roperand
        elif node.val == TIMES:
            return loperand * roperand
        elif node.val == DIVIDE:
            return loperand / roperand
        else:
            raise InvalidStateException("Unsupported operator:{}".format(node.val))

def evaluate(root):
    # Fill this in.
    solu = Solution()
    return solu.evaluateBTree(root)


if __name__ == "__main__":
    tree = Node(TIMES)
    tree.left = Node(PLUS)
    tree.left.left = Node(3)
    tree.left.right = Node(2)
    tree.right = Node(PLUS)
    tree.right.left = Node(4)
    tree.right.right = Node(5)
    print (evaluate(tree))
    # 45