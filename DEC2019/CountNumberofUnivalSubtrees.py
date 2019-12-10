
#A unival tree is a tree where all the nodes have the same value. Given a binary tree, return the number of unival subtrees in the tree.

#For example, the following tree should return 5:

#   0
#  / \
# 1   0
#    / \
#   1   0
#  / \
# 1   1

#The 5 trees are:
#- The three single '1' leaf nodes. (+3)
#- The single '0' leaf node. (+1)
#- The [1, 1, 1] tree at the bottom. (+1)

#Here's a starting point:

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    def __str__(self):
        node = self
        stack = []
        stack.append(node)
        string = []
        while len(stack)!=0:
            node = stack.pop()
            string.append("%d,"%(node.val))
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
        return "".join(string)

class InvalidStateException (Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self,*args,**kwargs)

class Solution:
    def count_unival_subtrees(self, root):
        subtreeSet = set()
        subNode = self.__dfsHelper(root, subtreeSet)
        return len(subtreeSet)

    def __dfsHelper(self, node, subtreeSet):

        if node.left is None and node.right is None:
            return node


        if node.left is not None and node.right is not None:
            lnode = self.__dfsHelper(node.left, subtreeSet)
            rnode = self.__dfsHelper(node.right, subtreeSet)
            if lnode is not None:
                subtreeSet.add(lnode)
            if rnode is not None:
                subtreeSet.add(rnode)
            if lnode is not None and rnode is not None and (lnode.val == rnode.val == node.val):
                subtreeSet.add(node)
                return node
            else:
                return None
        if node.left is not None:
            lnode = self.__dfsHelper(node.left, subtreeSet)
            if lnode is not None:
                subtreeSet.add(lnode)
            if lnode.val == node.val:
                subtreeSet.add(node)
                return node
            else:
                return None
        if node.right is not None:
            rnode = self.__dfsHelper(node.right, subtreeSet)
            if rnode is not None:
                subtreeSet.add(rnode)
            if rnode.val == node.val:
                subtreeSet.add(node)
                return node
            else:
                return None
        raise InvalidStateException("Invalid state at:" + node)


def count_unival_subtrees(root):
    solu = Solution()
    return solu.count_unival_subtrees(root)


if __name__ == "__main__":
    a = Node(0)
    a.left = Node(1)
    a.right = Node(1)
    a.right.left = Node(1)
    a.right.left.left = Node(1)
    a.right.left.right = Node(1)
    #   0
    #  / \
    # 1   1
    #    /
    #   1
    #  / \
    # 1   1
    print(count_unival_subtrees(a))
    # 5

    a = Node(0)
    a.left = Node(1)
    a.right = Node(1)
    a.right.left = Node(1)
    a.right.right = Node(0)
    a.right.left.left = Node(1)
    a.right.left.right = Node(1)
    #   0
    #  / \
    # 1   1
    #    / \
    #   1   0
    #  / \
    # 1   1
    print(count_unival_subtrees(a))
    # 5


    a = Node(0)
    a.left = Node(1)
    a.right = Node(0)
    a.right.left = Node(1)
    a.right.right = Node(0)
    a.right.left.left = Node(1)
    a.right.left.right = Node(1)

    #   0
    #  / \
    # 1   0
    #    / \
    #   1   0
    #  / \
    # 1   1
    print (count_unival_subtrees(a))
    # 5

    a = Node(0)
    a.left = Node(1)
    a.right = Node(1)
    a.right.left = Node(1)
    a.right.right = Node(1)
    a.right.left.left = Node(1)
    a.right.left.right = Node(1)

    #   0
    #  / \
    # 1   1
    #    / \
    #   1   1
    #  / \
    # 1   1
    print(count_unival_subtrees(a))
    # 6