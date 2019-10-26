
from functools import reduce
class Solution:

    def addr(self, chr):
        return ord(chr)-97

    def lengthOfLongestSubstring(self, s):
        # Fill this in.
        print ("Hello")
        r = self.dummyFindShortestLength(s)
        return r

    def calculateLength ( self, checkArray):
        return reduce (lambda x, y: x+y, checkArray)

    def dummyFindShortestLength(self, s):
        longestLength = 0
        for i in range(0, len(s)-1):
            check = [0] * 26
            for chr in s[i:]:
                inx = self.addr(chr)
                if(check[inx] == 0):
                    check[inx] = 1
                else:
                    segmentLength = self.calculateLength(check)
                    if(segmentLength > longestLength):
                        longestLength = segmentLength
                    break
        return longestLength

print (Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10