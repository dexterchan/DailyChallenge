# Skill: array travesal, BTree, recursive function
# difficulty : medium
#You are given the root of a binary tree. You need to implement 2 functions:

#1. serialize(root) which serializes the tree into a string representation
#2. deserialize(s) which deserializes the string back to the original tree that it represents

#For this problem, often you will be asked to design your own serialization format.
# However, for simplicity, let's use the pre-order traversal of the tree. Here's your starting point:

#Analysis
#Serialization:
# apply depth first search
# when node is None, return ""
# when left is not None, prepare the output as "value" + call the same function for next node
# return of function is output string +"#"
# when right is not None, prepare the output as "value # " + call the same function for next node
#

#Deserialization
# array traversal of the list
# if current pos is not #, create a new node
# check if next two position are #, if yes, return node with the position number
# check if next position is a number, if yes, recurse the same function and assign output left node, update the position from function
# check if next position is #, if yes, recurse the same function and assign output to right node, update the position from function

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    # pre-order printing of the tree.
    result = ''
    result += str(self.val)
    if self.left:
      result += str(self.left)
    if self.right:
      result += str(self.right)
    return result

class InvalidStateException (Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class SerializeSolution:
    def serialize(self, root):
        return self.__recursive(root)+" # #"

    def __recursive(self, node):
        if node is None:
            return ""

        tmpValue = str(node.val)
        if node.left is not None:
            tmpValue = tmpValue + " " + self.__recursive(node.left)+" #"
        if node.right is not None:
            tmpValue = tmpValue + " # " + self.__recursive(node.right)
        return tmpValue

class DeSerializeSolution:
    def deserialize(self, data):
        l = data.split(' ')
        node, inx= self.__recursive( l, 0)
        return node

    def __recursive(self, lst, inx):
        if inx >= len(lst) - 2:
            return None, inx
        if lst[inx] != "#":
            node = Node(lst[inx])
        else:
            raise InvalidStateException("Invalid State at {}".format(inx))

        if lst[inx + 1] == "#" and lst[inx+2] == "#":
            return node, inx+ 1

        if lst[inx + 1] != "#":
            node.left, inx = self.__recursive(lst, inx + 1)

        if lst[inx + 1] == "#":
            node.right, inx = self.__recursive(lst, inx + 2)

        return node, inx


def serialize(root):
    solu = SerializeSolution()
    return solu.serialize(root)


def deserialize(data):
    solu = DeSerializeSolution()
    return solu.deserialize(data)

if __name__ == "__main__":
#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
    tree = Node(1)
    tree.left = Node(3)
    tree.left.left = Node(2)
    tree.left.right = Node(5)
    tree.right = Node(4)
    tree.right.right = Node(7)

    print (serialize(tree))
    # 1 3 2 # # 5 # # 4 # 7 # #
    print (deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
    # 132547