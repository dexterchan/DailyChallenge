
#A k-ary tree is a tree with k-children,
# and a tree is symmetrical if the data of the left side of the tree is the same as the right side of the tree.

#Here's an example of a symmetrical k-ary tree.
#        4
#     /     \
#    3        3
#  / | \    / | \
#9   4  1  1  4  9
#Given a k-ary tree, figure out if the tree is symmetrical.

#Here is a starting point:

#Analysis
# Assumption: we check the symmetric at the root.... therefore we only have two substrees under the root
# For Symmetric, the right subtree should be the "mirror" image of the left substree
# therefore, left to right of right substree is a reverse order of the left
# Begin the work
# try problem with breath first search of each subtree
# we have queue in each left and right subtree
# left tree, we insert each element at each level from left to right fashion
# each insert , we have (node, lvl)
# right tree, we insert each element at each level from right to left fashion
# each insert , we have (node, lvl) also
# function : insertQueue(Q, node, lvl)
# after insertion, we pop each element from queue to compare from left queue and right queue
# check if left element value  = right element value and check left level = right level
# if false, return false
# if true, continue to insert their children with insertQueue(element, lvl+1)
# iterate all above step until left queue and right queue are blank
#Time cost : travse a tree : O(N) Space cost: O(N) for the queue

from enum import Enum
from collections import deque
class SIDE(Enum):
    LEFT = 1
    RIGHT = 2
class Node():
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children


class Solution:
    def is_symmetric(self, root):
        if len(root.children) != 2:
            return False
        leftTree = root.children[0]
        rightTree = root.children[1]

        return self.__subTreeCmp(leftTree, rightTree)

    def __subTreeCmp(self, leftTree, rightTree):
        leftQ = deque()
        rightQ = deque()
        leftQ.append((leftTree, 1, 0, 0))
        rightQ.append((rightTree, 1, 0, 0))

        while (len(leftQ)!=0) and (len(rightQ)!=0):
            leftEle, leftLvl, leftinx, leftpinx = leftQ.popleft()
            rightEle, rightLvl, rightinx, rightpinx = rightQ.popleft()

            if leftEle.value == rightEle.value and leftLvl==rightLvl and leftinx == rightinx and leftpinx == rightpinx:
                self.__insertElement(leftQ, leftEle, leftLvl+1, SIDE.LEFT, leftinx)
                self.__insertElement(rightQ, rightEle, rightLvl+1, SIDE.RIGHT, rightinx)
            else:
                return False
        if len(leftQ)!=0 or len(rightQ)!=0:
            return False

        return True

    def __insertElement(self, queue:deque, node, lvl, side: SIDE, pinx):
        l = len(node.children)

        for inx in range(l):
            iinx = inx if side == SIDE.LEFT else l-inx-1
            newNode = node.children[iinx]
            queue.append((newNode, lvl, inx, pinx))


def is_symmetric(root):
    # Fill this in.
    solu = Solution()
    return solu.is_symmetric(root)
if __name__ == "__main__":
    tree = Node(4)
    tree.children = [Node(3), Node(3)]
    tree.children[0].children = [Node(9), Node(4)]
    tree.children[1].children = [Node(4), Node(9)]
    tree.children[0].children[0].children = [Node(10)]
    tree.children[1].children[0].children = [Node(10)]
    print(is_symmetric(tree))
    # False

    tree = Node(4)
    tree.children = [Node(3), Node(3)]
    tree.children[0].children = [Node(9), Node(4)]
    tree.children[1].children = [Node(4), Node(9), Node(5)]
    tree.children[0].children[0].children = [Node(10)]
    tree.children[1].children[1].children = [Node(10)]
    print(is_symmetric(tree))
    # False

    tree = Node(4)
    tree.children = [Node(3), Node(3)]
    tree.children[0].children = [Node(9), Node(4)]
    tree.children[1].children = [Node(4), Node(9)]
    tree.children[0].children[0].children = [Node(10)]
    tree.children[1].children[1].children = [Node(10)]
    print(is_symmetric(tree))
    # True

    tree = Node(4)
    tree.children = [Node(3), Node(3)]
    tree.children[0].children = [Node(9), Node(4), Node(1)]
    tree.children[1].children = [Node(1), Node(4), Node(9)]
    print(is_symmetric(tree))
    # True

    tree = Node(4)
    tree.children = [Node(3), Node(3)]
    tree.children[0].children = [Node(9), Node(4), Node(1)]
    tree.children[1].children = [Node(1), Node(4), Node(9)]
    tree.children[0].children[0].children = [Node(10)]
    tree.children[1].children[2].children = [Node(10)]
    print(is_symmetric(tree))
    # True



    tree = Node(4)
    tree.children = [Node(3), Node(3)]
    tree.children[0].children = [Node(9), Node(4), Node(1)]
    tree.children[1].children = [Node(1), Node(4), Node(9)]
    tree.children[0].children[0].children = [Node(10)]
    print (is_symmetric(tree))
    # False

    tree = Node(4)
    tree.children = [Node(3), Node(3)]
    tree.children[0].children = [Node(9), Node(4), Node(1)]
    tree.children[1].children = [Node(1), Node(4), Node(4)]
    print(is_symmetric(tree))
    # False

