#Skill: Breath first search
#You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

#Example:

#    a
#   / \
#  b   c
# /
#d

#The deepest node in this tree is d at depth 3.

#Here's a starting point:

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __repr__(self):
        # string representation
        return self.val

class Solution:
    def findDeepest(self, node):

        #return self.recusiveDeepest(node, 1)
        return self.iterativeDeepest(node)

    #Cost O(N), space O(N)
    def recusiveDeepest(self, node, level):
        if node is None:
            return None, level-1
        leftlvl = level
        rightlvl = level

        leftval, leftlvl = self.recusiveDeepest(node.left, leftlvl+1)
        if leftlvl == level:
            leftval = node.val
        rightval, rightlvl = self.recusiveDeepest(node.right, rightlvl+1)
        if rightlvl == level:
            rightval = node.val

        if leftlvl > rightlvl:
            #print ("left %d: %s"%(leftlvl, node.val))
            return (leftval, leftlvl)
        else:
            #print("right %d: %s" % (rightlvl, node.val))
            return (rightval, rightlvl)

    # Cost O(N), space O(N)
    def iterativeDeepest(self, node):
        curr = node
        stack = []
        stack.append((curr,1))
        deepestlvl = 0
        deepestVal = None
        while len(stack)>0:
            tNode, lvl = stack.pop()
            if lvl > deepestlvl:
                deepestlvl = lvl
                deepestVal = tNode.val
            if tNode.left is not None:
                stack.append((tNode.left, lvl + 1))
            if tNode.right is not None:
                stack.append((tNode.right, lvl + 1))
        return deepestVal, deepestlvl





def deepest(node):
    solu = Solution()
    return solu.findDeepest(node)

if __name__ == "__main__":
    root = Node('a')
    root.left = Node('b')
    root.left.left = Node('d')
    root.right = Node('c')

    print (deepest(root))
    # (d, 3)

    root = Node('a')
    root.left = Node('b')
    root.left.left = Node('d')
    root.right = Node('c')
    root.right.left = Node('e')
    root.right.left.right = Node('f')
    root.right.left.right.left = Node('g')

    print(deepest(root))