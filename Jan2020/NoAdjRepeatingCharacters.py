
#Given a string, rearrange the string so that no character next to each other are the same.
# If no such arrangement is possible, then return None.

#Example:
#Input: abbccc
#Output: cbcbca

#Analysis
#First understand the statistics
# Scan the whole string to find frequency for each character.. O(N)
# Store result in a map O(1)
# put the frequency into priority queue O(NlogN)
# pop the priority queue one by one
# each item , if next character = current character , put this element into a temp stack
# then pop another element
# if next element <> current character, append to new string,
# then pop all temp stack back to priority queue
# repeat for next character
# if all next element = current character, return None

from heapq import heappush, heappop
from collections import defaultdict
MAX = 1<<31 - 1
class Solution:
    def rearrangeString(self,str):
        h = []
        m = self.__analysisString2Map(str)

        for k in m.keys():
            heappush(h, (MAX - m[k], k))

        preValue=None
        curValue=None
        result = []
        s = []
        while len(h) > 0:
            _freq, curValue = heappop(h)
            f = MAX - _freq

            if preValue is None:
                result.append(curValue)
                s.append((f-1, curValue))
                self.__pushBackHeap(h, s)
                preValue = curValue
            elif preValue != curValue:
                result.append(curValue)
                s.append((f - 1, curValue))
                self.__pushBackHeap(h, s)
                preValue = curValue
            else:
                s.append((f, curValue))


        if len(result) != len(str):
            return None
        return "".join(result)

    def __pushBackHeap(self, h, stack):
        while len(stack)>0:
            freq, curValue = stack.pop()
            if freq > 0:
                heappush(h, (MAX-freq, curValue))
    def __analysisString2Map(self, s):
        m = defaultdict(int)
        for ch in s:
            m[ch] = m[ch] + 1
        return m


def rearrangeString(s):
    # Fill this in.
    solu = Solution()
    return solu.rearrangeString(s)



if __name__ == "__main__":
    print(rearrangeString('abbcccc'))
    # cbcacbc

    print (rearrangeString('abbccc'))
    # cbcabc

    print(rearrangeString('abbccccc'))
    # None