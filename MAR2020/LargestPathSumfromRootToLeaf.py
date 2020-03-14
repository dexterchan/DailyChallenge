
#Given a binary tree, find and return the largest path from root to leaf.

#Here's an example and some starter code:
#analysis
# dfs to the leaf.... leaf will put the path and cost into priority queue
# during traversal, node replicate a copy of path history to child rescursive function

import heapq
from typing import List
from copy import deepcopy

MAXVALUE = 1<<31

class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right
class Solution():
    def largest_path_sum(self, tree):
        res = None
        rankHistory = []
        history = []
        self.__dfsHelper(tree, history, 0, rankHistory)
        res = rankHistory[0][1]

        return res

    def __dfsHelper(self, tree:Node, history:List, pathCost:int, rankHistory:List ):
        newCost = pathCost + tree.value
        history.append(tree.value)
        if tree.left is None and tree.right is None:
            heapq.heappush(rankHistory, (MAXVALUE-newCost, history))
        if tree.left is not None:
            lhist = deepcopy(history)
            self.__dfsHelper(tree.left, lhist, newCost, rankHistory)
        if tree.right is not None:
            rlist = deepcopy(history)
            self.__dfsHelper(tree.right, rlist, newCost, rankHistory)


def largest_path_sum(tree):
    # Fill this in.
    solu = Solution()
    return solu.largest_path_sum(tree)


if __name__ == "__main__":
    tree = Node(1)
    tree.left = Node(3)
    tree.right = Node(2)
    tree.right.left = Node(4)
    tree.left.right = Node(5)
    #    1
    #  /   \
    # 3     2
    #  \   /
    #   5 4
    print(largest_path_sum(tree))
    # [1, 3, 5]

    tree = Node(1)
    tree.left = Node(3)
    tree.right = Node(2)
    tree.right.left = Node(4)
    tree.left.right = Node(5)
    tree.left.right.left = Node(6)
    tree.left.left = Node(20)
    print(largest_path_sum(tree))