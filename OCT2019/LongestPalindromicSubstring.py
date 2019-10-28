
# Example
#Input: "banana"
#Output: "anana"

#Input: "million"
#Output: "illi"
import math

class Solution:
    def longestPalindrome(self, s):
        result = self.brutalForce(s)
        result = self.dynamicProgram(s)
        return result

    def checkPalindrom(selfs,s):
        wordL = len(s)
        left = s[: math.ceil(wordL/2) ]
        right = s[math.floor(wordL/2):]
        right = right[::-1]
        if left == right:
            return True
        else:
            return False

    #O(N^3)
    def brutalForce(self,s):
        wordL = len(s)
        longStr = ""

        for i in range(0, wordL-1):
            for j in range ( wordL-1,i,-1):
                testStr = s[i:j+1]
                if( self.checkPalindrom (testStr) ):
                    if(len(testStr) > len(longStr)):
                        longStr = testStr

        return longStr

    def dynamicProgram ( self, s):
        wordL = len(s)
        memory = [[False for i in range(wordL)] for j in range(wordL)]

        maxLength = 0
        start = -1
        for i in range(0,wordL):
            memory[i][i] = True

        k = 1
        for i in range (0,wordL-k):
            if (s[i]==s[i+1]):
                memory[i][i+1]=True
                if(k>maxLength):
                    start = i
                    maxLength = k

        #self.debug (memory,wordL)

        for k in range(2, wordL-2):
            for i in range (wordL-k):
                if( memory[i+1] and memory[i+k-1]):
                    if(s[i] == s[i+k]):
                        memory[i][i+k] = True
                        if(k > maxLength):
                            maxLength = k
                            start = i
        #self.debug(memory, wordL)

        return s[start:start+maxLength+1]

    def debug (self, memory, l):
        for i in range(l):
            for j in range(l):
                print ("%d "%(memory[i][j]), end='')
            print ("")

# Fill this in.
if __name__ == "__main__":
    # Test program
    s = "tracecars"
    s = "abcded"
    print(str(Solution().longestPalindrome(s)))
    # racecar