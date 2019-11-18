#Given a linked list of integers, remove all consecutive nodes that sum up to 0.

#Example:
#Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
#Output: 10

#The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that sequence should be removed.
# 4 -> -4 also sums up to 0 too so that sequence should also be removed.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Solution:
    def __removeNodesHelper(self, headRef, end):
        if headRef != None:
            headRef.next = end.next
        else:
            return end.next, None
        return headRef, headRef

    def removeConsecutiveSumTo0_BrutalForce(self, node):
        checkNode = node
        headRef = None
        while checkNode is not None:
            mysum = checkNode.value

            accmnode = checkNode.next
            while accmnode is not None:
                mysum = mysum + accmnode.value
                if mysum == 0:
                    checkNode, headRef = self.__removeNodesHelper(headRef, accmnode)
                    break
                accmnode = accmnode.next


            headRef = checkNode
            #else:
            #    headRef = None
            checkNode = checkNode.next
        return node



def removeConsecutiveSumTo0(node):
    solu = Solution()
    return solu.removeConsecutiveSumTo0_BrutalForce(node)




if __name__ == "__main__":
    node = Node(10)
    node.next = Node(5)
    node.next.next = Node(-3)
    node.next.next.next = Node(-3)
    node.next.next.next.next = Node(1)
    node.next.next.next.next.next = Node(4)
    node.next.next.next.next.next.next = Node(-4)
    node = removeConsecutiveSumTo0(node)
    while node:
        print (node.value, end=',')
        node = node.next
    # 10
