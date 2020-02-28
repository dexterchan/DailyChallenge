
#Given a postorder traversal for a binary search tree, reconstruct the tree.
# A postorder traversal is a traversal order where the left child always comes before the right child,
# and the right child always comes before the parent for all nodes.

#Here's some starter code:

#Analysis
#find the length of the array
#take the last element as the root
#Left(0..(N-1)/2] as left child of root
#right((N-1)/2 .. N) as right child of root
# rescursive call same function for left(0..(N-1)/2)
# rescursive call same function for right ((N-1)/2..N)

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.value) + ", " + self.left.__repr__() + ", " + self.right.__repr__() + ")"

class Solution():

    def create_tree(self, postOrder):
        l = len(postOrder)
        if l == 0:
            return None
        if l == 1:
            return Node(postOrder[0])
        childLength = l-1
        newNode = Node(postOrder[childLength])
        lChildLength = int(childLength/2)
        rChildLength = childLength - lChildLength
        newNode.left = create_tree(postOrder[:lChildLength])
        newNode.right = create_tree(postOrder[lChildLength:childLength])

        return newNode

def create_tree(postorder):
    # Fill this in.
    solu = Solution()
    return solu.create_tree(postorder)



if __name__ == "__main__":
    print(create_tree([1, 3, 2, 10]))

    # 2 is the root node, with 1 as the left child and 3 as the right child
    print(create_tree([1, 3, 2]))

