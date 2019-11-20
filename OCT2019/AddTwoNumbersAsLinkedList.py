#You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:

  def getNumberFromNodes(self,ll):
      l = ll
      lNumber = 0
      while (l != None):
          lNumber = l.val + lNumber * 10
          l = l.next
      return lNumber

  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    #Get left number
    lNumber = self.getNumberFromNodes(l1)

    rNumber = self.getNumberFromNodes(l2)

    calNumber = lNumber + rNumber

    #Parse result
    remainNumber = calNumber
    result = None
    currentNode = None
    while remainNumber != 0  :
        digit = remainNumber % 10
        if result == None :
            result = ListNode(digit)
            currentNode = result
        else:
            currentNode.next = ListNode (digit)
            currentNode = currentNode.next
        remainNumber = remainNumber // 10
    return result




l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print (result.val, end='')
  result = result.next
# 7 0 8