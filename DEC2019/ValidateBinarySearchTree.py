#Skill: Binary Search Tree, Depth First Search
#You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise. Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root, and all values in the right subtree are greater than or equal to the root.

#Here's a starting point:

class TreeNode:
  def __init__(self, key):
      self.left = None
      self.right = None
      self.key = key

#Cost: O(N) Space O(1)
class Solution:
    def __init__(self, isDebug = True):
        self.debug = isDebug
    def is_bst(self, root):
        try:
            low, high = self.__depthFirstSearchRecursive(root)
        except Exception as ex:
            if self.debug:
                print (ex)
            return False
        return True

    def is_betHelper(self, root):
        isIterative = True
        if isIterative:
            try:
                self.__depthFirstSearchIterative(root)
            except Exception as ex:
                if self.debug:
                    print(ex)
                return False
        else:
            try:
                low, high = self.__depthFirstSearchRecursive(root)
            except Exception as ex:
                if self.debug:
                    print(ex)
                return False

        return True

    def __depthFirstSearchRecursive(self, node):
        if node is None:
            raise Exception("Node is None")

        if node.left is not None:
            leftLow, leftHigh = self.__depthFirstSearchRecursive( node.left)
        else:
            leftLow = leftHigh = node.key

        if node.right is not None:
            rightLow, rightHigh = self.__depthFirstSearchRecursive( node.right)
        else:
            rightLow = rightHigh = node.key

        if leftHigh > node.key:
            raise Exception ("at (%d), left subtree highest value (%d) is greater than node value" % (node.key, leftHigh))
        if rightLow < node.key:
            raise Exception ("at (%d), right subtree lowest value (%d) is smaller than node value" % (node.key, rightLow))
        return leftLow, rightHigh

    def __depthFirstSearchIterative(self, root):
        cacheresult = {}
        stack = []
        stack.append(root)

        while len(stack) > 0:
            node = stack[-1]

            if node.left is None and node.right is None:
                cacheresult[node] = (node.key, node.key)
                stack.pop()
                continue
            leftLow = None
            leftHigh = None
            rightLow = None
            rightHigh = None
            if node.left is not None and node.left not in cacheresult:
                stack.append(node.left)
                continue
            elif node.left is not None and node.left in cacheresult:
                leftLow, leftHigh = cacheresult[node.left]
            else:
                leftLow = leftHigh = node.key

            if node.right is not None and node.right not in cacheresult:
                stack.append(node.right)
                continue
            elif node.left not in cacheresult and node.right not in cacheresult:
                rightLow, rightHigh = cacheresult[node.right]
            else:
                rightLow = rightHigh = node.key

            if leftHigh > node.key:
                raise Exception(
                    "at (%d), left subtree highest value (%d) is greater than node value" % (node.key, leftHigh))
            if rightLow < node.key:
                raise Exception(
                    "at (%d), right subtree lowest value (%d) is smaller than node value" % (node.key, rightLow))
            cacheresult[node]= (leftLow, rightHigh)
            stack.pop()
        return True



#Wrong!!!
class ValidateBst:

    def is_bst(self, root):

        try:
            childNodes, isok = self.__validateEachNodes(root)

            if not isok:
                return False
        except Exception as ex:
            print (ex)
            return False


        for n in childNodes:
            try:
                isFound = self.__checkIfReachChildNode(root, n.key)
                if not isFound:
                    return False
            except Exception as ex:
                print (ex)
                return False
        return True

    def __validateEachNodes(self, root):
        childNodes = set()
        isok = False
        stack = []
        stack.append (root)
        while len(stack) > 0:
            node = stack.pop()
            if node.left is not None:
                if node.left.key > node.key:
                    raise Exception("at %d, left child (%d) is larger "%(node.key, node.left.key))
                stack.append(node.left)
            if node.right is not None:
                if node.right.key < node.key:
                    raise Exception("at %d, right child (%d) is smaller"%(node.key, node.right.key))
                stack.append(node.right)
            if node.left is None and node.right is None:
                childNodes.add(node)

        isok = True

        return childNodes, isok

    def __checkIfReachChildNode(self, root, value):

        curNode = root

        while curNode!=None:
            if curNode.left==None and curNode.right==None:
                return curNode.key == value

            if curNode.key >= value:
                curNode = curNode.left
            elif curNode.key <value:
                curNode = curNode.right
        return False


def is_bst(root, isDEBUG=True):
    # Fill this in.
    #solu = ValidateBst()
    solu = Solution(isDEBUG)
    return solu.is_bst(root)


if __name__ == "__main__":
    a = TreeNode(5)
    a.left = TreeNode(3)
    a.right = TreeNode(7)
    a.left.left = TreeNode(1)
    a.left.right = TreeNode(10)
    a.right.left = TreeNode(6)
    print(is_bst(a))

    a = TreeNode(5)
    a.left = TreeNode(3)
    a.right = TreeNode(7)
    a.left.left = TreeNode(1)
    a.left.right = TreeNode(2)
    a.right.left = TreeNode(6)
    print(is_bst(a))



    a = TreeNode(5)
    a.left = TreeNode(3)
    a.right = TreeNode(7)
    a.left.left = TreeNode(1)
    a.left.right = TreeNode(4)
    a.right.left = TreeNode(6)
    print (is_bst(a))

    a = TreeNode(5)
    a.left = TreeNode(3)
    a.right = TreeNode(7)
    a.left.left = TreeNode(1)
    a.left.right = TreeNode(10)
    a.right.left = TreeNode(6)
    a.left.right.left = TreeNode(4)
    print(is_bst(a))
#    5
#   / \
#  3   7
# / \ /
#1  4 6
