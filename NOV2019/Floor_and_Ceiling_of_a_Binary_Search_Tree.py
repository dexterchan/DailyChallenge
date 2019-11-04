#Given an integer k and a binary search tree, find the floor (less than or equal to) of k,
#and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def findFloorIteratively (root_node, k):
    if( k < root_node.value):
        if(root_node.left != None and root_node.left.value < k):
            return findFloorIteratively(root_node.left, k)
        else:
            return None
    elif (root_node.right != None and root_node.right.value < k):
        return root_node.right.value
    elif (root_node.right != None and root_node.right.left != None):
        return findFloorIteratively(root_node.right, k)
    else:
        return root_node.value

def findCeilIteratively (root_node, k):
    if( k >= root_node.value):
        if(root_node.right != None and k <= root_node.right.value ):
            return findCeilIteratively(root_node.right, k)
        else:
            return None
    elif (root_node.left != None and k <= root_node.left.value ):
        return root_node.left.value
    elif (root_node.left != None and root_node.left.right != None):
        return findCeilIteratively(root_node.left, k)
    else:
        return root_node.value


def findCeilingFloor(root_node, k, floor=None, ceil=None):
    myfloor = None
    myCeil = None
    currentNode = root_node

    myfloor = findFloorIteratively (root_node, k)

    myCeil = findCeilIteratively( root_node, k)

    return myfloor, myCeil



# Fill this in.
if __name__ == "__main__":
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)

    root.left.left = Node(2)
    root.left.right = Node(6)

    root.right.left = Node(10)
    root.right.right = Node(14)

    print (findCeilingFloor(root, 5))
    # (4, 6)

    print(findCeilingFloor(root, 11))