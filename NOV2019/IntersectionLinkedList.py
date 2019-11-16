#Skill hash
#You are given two singly linked lists. The lists intersect at some node. Find, and return the node. Note: the lists are non-cyclical.

#Example:

#A = 1 -> 2 -> 3 -> 4
#B = 6 -> 3 -> 4

#This should return 3 (you may assume that any nodes with the same value are the same node).


class Solution:
    def findlsintersection(self, la, lb):
        nodeA = la
        nodeB = lb
        sA = set()
        sB = set()
        while nodeA is not None or nodeB is not None:
            if nodeA is not None:
                if(nodeA in sB):
                    return nodeA
                sA.add(nodeA)
                nodeA = nodeA.next

            if nodeB is not None:
                if(nodeB in sA):
                    return nodeB
                sB.add(nodeB)
                nodeB = nodeB.next
        return None


def intersection(a, b):
  # fill this in.
    solu = Solution()
    return solu.findlsintersection(a,b )

class Node(object):
  def __init__(self, val):
    self.val = val
    self.next = None
  def prettyPrint(self):
    c = self
    while c:
      print (c.val, end=' ')
      c = c.next
  def toString (self):
      buffer = []
      c = self
      while c:
          buffer.append(c.val)
          c = c.next
      return "".join(str(buffer))

if __name__ == "__main__":
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next.next = Node(4)

    b = Node(6)
    b.next = a.next.next

    c = intersection(a, b)
    c.prettyPrint()
    # 3 4
    print()
    c = intersection(b, a)

    print (c.toString())