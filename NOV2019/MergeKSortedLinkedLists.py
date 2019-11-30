#Skll: Linked list, heap
#You are given an array of k sorted singly linked lists. Merge the linked lists into a single sorted linked list and return it.

#Here's your starting point:
import heapq
class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

class Solution:
    #Cost: k is number of linked list, N is longest linked list, M is number of element
    #Cost: O[logk] * M
    def merge_multi_linkedList(self, lists):
        h = []
        res = None
        endNode = None
        for nodes in lists:
            heapq.heappush(h, (nodes.val, nodes))

        while len(h) > 0:
            v, smallNode = heapq.heappop(h)
            if smallNode.next is not None:
                heapq.heappush(h, (smallNode.next.val, smallNode.next))
            smallNode.next = None
            if res is None:
                res = smallNode
                endNode = smallNode
            else:
                endNode.next = smallNode
                endNode = endNode.next
        return res



def merge(lists):
    sol = Solution()
    return sol.merge_multi_linkedList(lists)

if __name__ == "__main__":
    a = Node(1, Node(3, Node(5)))
    b = Node(2, Node(4, Node(6)))
    print (merge([a, b]))
    # 123456

    a = Node(1, Node(4, Node(5)))
    b = Node(3, Node(7, Node(9)))
    c = Node(2, Node(6, Node(8)))
    print(merge([a, b, c]))
    # 123456789