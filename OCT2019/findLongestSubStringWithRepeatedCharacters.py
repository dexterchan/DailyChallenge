
from functools import reduce

class Solution2:
    CHAR_MAP_SIZE = 256
    def addr(self, chr):
        return ord(chr)#-97

    def lengthOfLongestSubstring(self, s):
        # Fill this in.
        r = self.LinearShortestLength(s)
        return r

    #O[n^2]
    def dummyFindShortestLength(self, s):
        longestLength = 0
        for i in range(0, len(s)):
            check = [0] * self.CHAR_MAP_SIZE
            for chr in s[i:]:
                inx = self.addr(chr)
                if(check[inx] == 0):
                    check[inx] = 1
                else:
                    break
            segmentLength = reduce (lambda x, y: x+y, check)
            longestLength = max ( segmentLength, longestLength)
        return longestLength

    #O[n]
    def LinearShortestLength(self,s):
        longestLength = 0
        visit = [-1] * self.CHAR_MAP_SIZE
        start=0
        currentLength = 0
        for i in range (0,len(s)):
            chr = s[i]
            inx = self.addr(chr)
            if(visit[inx] < start ):
                visit[inx] = i
                currentLength = currentLength + 1
                longestLength = max( longestLength, currentLength)
            else:
                start = min(visit[inx]+1,len(s)-1)
                currentLength=i-start+1
                visit[inx] = i

        return longestLength,start


if __name__ == "__main__":
    longestLen, start = Solution2().lengthOfLongestSubstring('abrkaabcdefghijjxxx')

    longestLen, start = Solution2().lengthOfLongestSubstring('abcdddddfghjklmnbmhj')

    longestLen, start = Solution2().lengthOfLongestSubstring('ABDEFGABEF'.lower())



    print ("%d %d"%(longestLen,start))

    #print (Solution().lengthOfLongestSubstring('abcde'))
    # 10