
#An IP Address is in the format of A.B.C.D, where A, B, C, D are all integers between 0 to 255.

#Given a string of numbers, return the possible IP addresses you can make with that string by splitting into 4 parts of A, B, C, D.

#Keep in mind that integers can't start with a 0! (Except for 0)

#Example:
#Input: 1592551013
#Output: ['159.255.101.3', '159.255.10.13']

#Analysis
#use backtracking
#construct a queue: explore, result
#explore contains a Node
# Node{
# parts=[]
# ptr (contains last pos)
#
#}
# a function take a Node from explore queue
# it produce the next possible parts, by trying the increment the next_ptr (ptr + 1, ptr + 2, ptr +3)
# the number num[ptr:next_ptr+1] will be validated with (0,255), num[ptr]!=0
# also, the parts length <4
# if all ok, deepcopy a new Node and append this new number
# if node.parts==4 and next_ptr==len(s)-1, put node into result queue
# if node.parts<4 and next_ptr < len(s)-1, put node into explore queue
# loop until all explore queue empty

# result the final result queue
import copy
from collections import deque
class Node():
    def __init__(self, ptr):
        self.parts = []
        self.ptr = ptr
    def copy(self):
        return copy.deepcopy(self)

class Solution():
    def ip_addr(self, s):
        n = Node(0)
        explore = deque()
        result = []
        explore.append(n)

        while len(explore) > 0:
            n = explore.popleft()
            if len(n.parts)>=4 and n.ptr > len(s):
                continue
            if len(n.parts)==4 and n.ptr == len(s):
                result.append(n)
                continue
            for i in range(3):
                newPtr = n.ptr + i + 1
                if newPtr > len(s):
                    break
                if not self.__validate(s[n.ptr:newPtr]):
                    break
                num = int (s[n.ptr:newPtr])
                newNode = n.copy()
                newNode.parts.append(str(num))
                newNode.ptr = newPtr
                explore.append(newNode)

        return result

    def __validate (self, substr):
        if substr[0] == "0" and len(substr) > 1:
            return False
        num = int(substr)
        if num<0 or num>255:
            return False

        return True


def ip_addresses(s, ip_parts=[]):
    # Fill this in.
    solu = Solution()
    nodeList = solu.ip_addr(s)
    return list(map(lambda n: ".".join(n.parts), nodeList))


if __name__ == "__main__":
    print (ip_addresses('1592551013'))
    # ['159.255.101.3', '159.255.10.13']