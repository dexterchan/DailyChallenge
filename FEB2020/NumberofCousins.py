
#Given a binary tree and a given node value,
# return all of the node's cousins.
# Two nodes are considered cousins if they are on the same level of the tree with different parents.
# You can assume that all nodes will have their own unique value.

#Here's some starter code:

#Analysis
# a custom data struct of Map
# Map[node value]=ADDRESS
#ADDRESS Struct: Node, parent node value, lvl
# DFS (node, parentNode, lvl, Map[node value], defaultdict[list of node])
# O(N)
# for each node, fill MAP
# Also, Register lvl information
# defaultdict(list of Node)
#serach of cousin, O(1) to get MAP[node value]
# get ADDRESS struct to get parent node (PN) and lvl
#  from lvl information, get all parent,
# cousin = children of parent list except parent node (PN)
# O(2^(log(N)-1)) = O(N/2)
# Overall time complexity O(N) , space complexity O(N)

from collections import defaultdict
from typing import Dict, List

class Node(object):
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Address():
    def __init__(self, node:Node, parentNode:Node, level:int):
        self.node = node
        self.parentNode = parentNode
        self.level = level

class Solution(object):
    def list_cousins(self, tree, val):
        # Fill this in.
        nodeMap = defaultdict(Address)
        lvlMap = defaultdict(list)

        self.__dfs(tree, None, 0, nodeMap, lvlMap)

        address = nodeMap[val]
        parent, lvl = address.parentNode, address.level-1

        if lvl <= 0 or lvl not in lvlMap:
            return None
        parentList = lvlMap[lvl]
        result = []
        for p in parentList:
            if p == parent:
                continue
            if p.left is not None:
                result.append(p.left.value)
            if p.right is not None:
                result.append(p.right.value)
        return result


    def __dfs (self, node:Node, parentNode:Node , lvl: int, nodeMap:Dict, lvlMap:Dict ):
        if node is None:
            return

        nodeMap[node.value] = Address(node, parentNode, lvl)
        lvlMap[lvl].append(node)

        if node.left is not None:
            self.__dfs(node.left, node, lvl + 1, nodeMap, lvlMap)
        if node.right is not None:
            self.__dfs(node.right, node, lvl + 1, nodeMap, lvlMap)

        return


if __name__ =="__main__":
    #     1
    #    / \
    #   2   3
    #  / \   \
    # 4   6   5
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(5)

    print (Solution().list_cousins(root, 5))
    # [4, 6]

    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(5)
    root.right.left = Node(7)

    print(Solution().list_cousins(root, 5))