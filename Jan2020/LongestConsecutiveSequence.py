#You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.

#For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.

#Can you do this in linear time?
#Anaysis
#Sorting costs O(NlogN) , no good
# to archieve linear time, we need a linked list. creating double linked list on-the-fly of sorted number when scanning the array
# iterate the array
# create prev dict and next dict
# for each element, create a double linked node, say number 100
# insert 99->(node 100) into next dict
# insert 101 -> (node 100) into pre dict
# for next element, say 99 , find (node 100) in next dict,
#  (node 99).next = (node 100), (node 99).prev = (node 100).prev, (node 99).prev.next = (node 99) , assign (node 100).prev to (node 99)
# also check 98 in prev dict, if not found , insert 98 -> (node 99) into prev dict



# in the end, we iterate double linked list, to find the longest consecutive sequence by O(N)

class dbNode:
    def __init__(self, val=None, prev=None, next=None ):
        self.val = val
        self.prev = prev
        self.next = next

    def insert(self, node1, node2):
        tmpNode = node1.next
        node1.next = node2
        node2.prev = node1
        if tmpNode is not None:
            tmpNode.prev = node2
            node2.next = tmpNode

    def __str__(self):
        s = ""
        n = self
        while n is not None:
            s = s + "," + str(n.val)
            n = n.next
        return str

class Solution:
    def longest_consecutive(self, nums):
        prevDict = {}
        nextDict = {}
        anchor = []

        for n in nums:
            node = dbNode(n)
            if n in prevDict:
                pNode = prevDict[n]
                dbNode().insert(pNode, node)
            else:
                dummy = dbNode(None)
                dbNode().insert(dummy, node)
                anchor.append(dummy)
                self.__insertNextDict(nextDict, node)
            if n in nextDict:
                nNode = nextDict[n]
                if nNode.prev.val != None:
                    dbNode().insert(nNode.prev, node)
                else:
                    dbNode().insert(node, nNode)
            else:
                self.__insertPrevDict(prevDict, node)

        maxLength = 0
        maxSeq = None
        for lt in anchor:
            ptr = lt.next
            l = 0
            s = []
            while ptr is not None:
                l += 1
                s.append(str(ptr.val))
                ptr = ptr.next
            if l > maxLength:
                maxLength = l
                maxSeq = ",".join(s)

        return maxLength, maxSeq

    def __insertPrevDict(self, prevDict, node):
        prevDict[node.val + 1] = node
    def __insertNextDict(self, nextDict, node):
        nextDict[node.val - 1] = node

def longest_consecutive(nums):
    # Fill this in.
    solu = Solution()
    return solu.longest_consecutive(nums)

if __name__ == "__main__":
    print (longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4

    print(longest_consecutive([5, 100, 4, 200, 7, 1, 3, 2, 6]))