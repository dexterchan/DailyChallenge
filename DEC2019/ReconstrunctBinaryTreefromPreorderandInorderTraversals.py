# Skill: tree traversal
#Difficulty : medium

#You are given the preorder and inorder traversals of a binary tree in the form of arrays. Write a function that reconstructs the tree represented by these traversals.

#Example:
#Preorder: [a, b, d, e, c, f, g]
#Inorder: [d, b, e, a, f, c, g]

#The tree that should be constructed from these traversals is:

#    a
#   / \
#  b   c
# / \ / \
#d  e f  g

#Here's a start:

from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    q = deque()
    q.append(self)
    result = ''
    while len(q):
      n = q.popleft()
      result += n.val
      if n.left:
        q.append(n.left)
      if n.right:
        q.append(n.right)

    return result

class InvalidNodeException (Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,*args,**kwargs)

class Solution:
    def reconstructTree(self, preorder, inorder):
        l = len(preorder)

        preOrderMap = {}
        inOrderMap = {}
        #Mark down preorder
        inx = 0
        for inx in range(l):
            preOrderMap[ preorder[inx]] = inx
            inOrderMap[inorder[inx]] = inx


        curHead = Node(inorder[0])


        for inx in range(1, l):
            ch = inorder[inx]
            chPreOrder = preOrderMap[ch]
            curHeadPreOrder = preOrderMap[curHead.val]
            if chPreOrder< curHeadPreOrder:
                newNode = Node(ch)
                newNode.left = curHead
                newNode.right = None
                curHead = newNode
                continue
            navNode = curHead
            inserted = False
            while not inserted:
                #Try insert to thr right
                if inOrderMap[ch] > inOrderMap[navNode.val]:
                    if navNode.right is None:
                        navNode.right = Node(ch)
                        inserted = True

                        if preOrderMap[ch] < preOrderMap[navNode.val]:
                            oldval = navNode.val
                            navNode.val = navNode.right.val
                            navNode.right.val = oldval
                            navNode.right.left = navNode.left
                            navNode.left = navNode.right
                            navNode.right=None
                        break
                    else:
                        navNode = navNode.right
                else:
                    raise InvalidNodeException("Invalid Node at %s"%(navNode.val))
        return curHead

class SolutionFailed:
    def reconstructTree(self, preorder, inorder):
        l = len(preorder)
        preOrderMap = {}
        inorderMap = {}

        headNode = Node(preorder[0])
        preOrderMap[preorder[0]] = headNode

        touchHead = False

        curInOrderNode = Node(inorder[0])
        curPreOrderNode = headNode

        preOrderMap[preorder[0]] = curPreOrderNode
        inorderMap[inorder[0]] = curInOrderNode
        for inx in range(1, l):
            curInOrderNode = self.__createInOrderNode(inx, curInOrderNode, inorder, preOrderMap, inorderMap)
            curPreOrderNode = self.__createOutOrderNode(inx, curPreOrderNode, preorder, preOrderMap, inorderMap)

        return headNode

    def __createInOrderNode(self, inx, curInOrderNode, inorder, preOrderMap, inorderMap):
        ich = inorder[inx]

        preOrderExist = False


        if curInOrderNode is None:
            curInOrderNode = Node(ich)
            inorderMap[ich] = curInOrderNode
        elif ich in preOrderMap:
            curInOrderNode = preOrderMap[ich]
            curInOrderNode = None
        elif curInOrderNode.left is None and curInOrderNode.right is None:
            newNode = Node(ich)
            newNode.left = curInOrderNode
            curInOrderNode = newNode
            inorderMap[ich] = curInOrderNode
        elif curInOrderNode.left is not None and curInOrderNode.right is None:
            curInOrderNode.right = Node(ich)
            inorderMap[ich] = curInOrderNode
        else:
            newNode = Node(ich)
            newNode.left = curInOrderNode
            curInOrderNode = newNode
            inorderMap[ich] = curInOrderNode

        return curInOrderNode

    def __createOutOrderNode(self, inx, curPreOrderNode, preorder, preOrderMap, inorderMap):
        ich = preorder[inx]
        existInOrderNode = None
        if ich in inorderMap:
            existInOrderNode = inorderMap[ich]
            self.__addAllInSet(existInOrderNode, preOrderMap)

        if curPreOrderNode is None:
            curPreOrderNode = Node (ich)
            preOrderMap[ich] = curPreOrderNode
        elif curPreOrderNode.left is None:
            if existInOrderNode:
                curPreOrderNode.left = existInOrderNode

            else:
                curPreOrderNode.left = Node(ich)
                curPreOrderNode = curPreOrderNode.left
                preOrderMap[ich] = curPreOrderNode
        elif curPreOrderNode.right is None:
            if existInOrderNode:
                curPreOrderNode.right = existInOrderNode

            else:
                curPreOrderNode.right = Node(ich)
                curPreOrderNode = curPreOrderNode.right
                preOrderMap[ich] = curPreOrderNode
        else:
            raise InvalidNodeException("Invalid Node at %s"%(ich))
        return curPreOrderNode

    def __addAllInSet(self, node, m):
        q = deque()
        q.append(node)

        while len(q) >0 :
            node = q.popleft()
            m[node.val] = node
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return




def reconstruct(preorder, inorder):
    solu = Solution()
    return solu.reconstructTree(preorder, inorder)


if __name__ == "__main__":
    tree = reconstruct(list('bdeij'), list('dbiej'))
    print(tree)

    tree = reconstruct(list('abdeijcfg'), list('dbiejafcg'))
    print(tree)

    tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'],
                       ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
    print (tree)
    # abcdefg

    tree = reconstruct(
                       ['a','c','d','b','h'],['d', 'c', 'b', 'a', 'h'])
    print(tree)

