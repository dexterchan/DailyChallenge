#Skill: Breath First Search tree travesal, Stack
#Given a binary tree, return the list of node values in zigzag order traversal. Here's an example

# Input:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#
# Output: [1, 3, 2, 4, 5, 6, 7]

#Here's some starter code

#Analysis BFS
# by iterative run, we have two double linked queue
# Q1 : queue
# Q2 : stack
# if keep level number,
# if level is even number, we insert the double Sided queue as stack
# if level is odd number, we insert the double sided queue as stack

# if level number is odd, we pop Q1
    # until Q1 exhaust, we keep dequeue from Q1, and append child into Q2
    # if Q1 exhaust, increment level,
# else if level number is even, we pop Q2
    # until Q2 exhaust, we keep pop Q2 and append child into Q1 in reverse order
    # if Q2 exhaust, increment level
# Time complexity : O(N) Space complexity: O(N)
from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution():
    def zigzag_order(self, node):
        result = []
        level = 1
        q1 = deque()
        q2 = deque()
        q1.append(node)

        while (len(q1) > 0) or (len(q2) > 0):
            isOdd = level % 2

            if not isOdd:
                if len(q2) == 0:
                    level += 1
                    continue
                n = q2.pop()
                result.append(n.value)
                if n.right is not None:
                    q1.append(n.right)
                if n.left is not None:
                    q1.append(n.left)

            else:
                if len(q1) == 0:
                    level += 1
                    continue
                n = q1.pop()
                result.append(n.value)
                if n.left is not None:
                    q2.append(n.left)
                if n.right is not None:
                    q2.append(n.right)
        return result





def zigzag_order(tree):
    # Fill this in.
    solu = Solution()
    return solu.zigzag_order(tree)




if __name__ == "__main__":
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)
    n1 = Node(1, n2, n3)

    print(zigzag_order(n1))
    # [1, 3, 2, 4, 5, 6, 7]

    n15 = Node(15)
    n14 = Node(14)
    n13 = Node(13)
    n12 = Node(12)
    n11 = Node(11)
    n10 = Node(10)
    n9 = Node(9)
    n8 = Node(8)
    n4 = Node(4, n8, n9)
    n5 = Node(5, n10, n11)
    n6 = Node(6, n12, n13)
    n7 = Node(7, n14, n15)
    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)
    n1 = Node(1, n2, n3)

    print(zigzag_order(n1))
    # [1, 3, 2, 4, 5, 6, 7]