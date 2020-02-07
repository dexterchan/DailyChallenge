
#You are given a tree, and your job is to print it level-by-level with linebreaks.

#    a
#   / \
#  b   c
# / \ / \
#d  e f  g

#The output should be
#a
#bc
#defg
#Here's a starting point:

#Analysis


# keep a variable level, (init = 0)
# insert first (node, 0) into dequeue
# if node, lvl pop from dequeue, lvl!=level, print("\n")
# print value to console
# level = lvl
# put its (child, lvl+1) into dequeue
# until dequeue is empty
# Time complexity O(N), space complexity O(N)


from collections import deque

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
      level = 0
      queue = deque()
      queue.append((self, 0))
      result=""
      while len(queue) > 0:
          node, lvl = queue.popleft()
          if lvl != level:
              result = result + "\n"
              level = lvl
          result = result + node.val
          if node.left is not None:
              queue.append((node.left, lvl + 1))
          if node.right is not None:
              queue.append((node.right, lvl + 1))
      return result


if __name__ == "__main__":
    tree = Node('a')
    tree.left = Node('b')
    tree.right = Node('c')
    tree.left.left = Node('d')
    tree.left.right = Node('e')
    tree.right.left = Node('f')
    tree.right.right = Node('g')

    print (tree)
    # a
    # bc
    # defg