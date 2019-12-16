#Skill: Binary Search Tree

#You are given the root of a binary tree. Find and return the largest subtree of that tree, which is a valid binary search tree.

#Assume a BST is defined as follows:

#    The left subtree of a node contains only nodes with keys less than the node's key.
#    The right subtree of a node contains only nodes with keys greater than the node's key.
#    Both the left and right subtrees must also be binary search trees.

#Tasks:
# Define BST
# Find size of BST
# get largest BST

# Here's a starting point:

from heapq import heappush, heappop

class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.key = key

  def __str__(self):
    # preorder traversal
    answer = str(self.key)
    if self.left:
      answer += str(self.left)
    if self.right:
      answer += str(self.right)
    return answer

class HeapTreeNode(TreeNode):
    def __init__(self, treeNode, size=0):
        super().__init__(treeNode.key)
        self.left = treeNode.left
        self.right = treeNode.right
        self.size = size

    def setSize(self, size):
        self.size = size

    def __lt__(self, other):
        return self.size < other.size


class Solution:
    def __init__(self):
        self.__LARGE = 1<<32
    def largest_bst_subtree(self, root):

        heap = []

        self.__isbst_and_size_rescursive(root, heap)
        largest = heappop(heap)
        return largest

    def __isbst_and_size_rescursive(self, root, heap):
        if root is None:
            return True, 0

        isLeftBst = True
        isRightBst = True
        leftSize = 0
        rightSize = 0
        if root.left is not None:

            if root.left.key > root.key:
                isLeftBst = False
            isLeftSubBst, leftSize = self.__isbst_and_size_rescursive(root.left, heap)
            if not isLeftSubBst or not isLeftSubBst:
                isLeftBst = False
                leftSize = 0

        if root.right is not None:
            if root.right.key < root.key:
                isRightBst = False
            isRightSubBst, rightSize = self.__isbst_and_size_rescursive(root.right, heap)
            if not isRightBst or not isRightSubBst:
                isRightBst = False
                rightSize = 0

        if isRightBst and isLeftBst:
            s = 1 + leftSize + rightSize
            #print("Found BST %s with size: %d" % (str(root), s))
            heappush(heap, HeapTreeNode(root, self.__LARGE - s))
            return True, 1 + leftSize + rightSize
        else:
            return False, 1 + leftSize + rightSize


def largest_bst_subtree(root):
    solu = Solution()
    return solu.largest_bst_subtree(root)



if __name__ == "__main__":
    #     5
    #    / \
    #   6   7
    node = TreeNode(5)
    node.left = TreeNode(6)
    node.right = TreeNode(7)
    t = largest_bst_subtree(node)
    print(str(t))
    # 749

    #     5
    #    / \
    #   6   7
    #  /   / \
    # 2   4   9
    node = TreeNode(5)
    node.left = TreeNode(6)
    node.right = TreeNode(7)
    node.left.left = TreeNode(2)
    node.right.left = TreeNode(4)
    node.right.right = TreeNode(9)
    t = largest_bst_subtree(node)
    print (str(t))
    #749


