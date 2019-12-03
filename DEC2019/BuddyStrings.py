
#Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

#Example 1:
#Input: A = "ab", B = "ba"
#Output: true
#Example 2:

#Input: A = "ab", B = "ab"
#Output: false
#Example 3:
#Input: A = "aa", B = "aa"
#Output: true
#Example 4:
#Input: A = "aaaaaaabc", B = "aaaaaaacb"
#Output: true
#Example 5:
#Input: A = "", B = "aa"
#Output: false
#Here's a starting point:

class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False
        if len(A) <= 1:
            return False
        buddyFound = False
        sameAdj = False
        for i in range(len(A)-1):
            if A[i] != B[i]:
                if self.__isBuddy(A[i], A[i+1], B[i], B[i+1]):
                    if not buddyFound:
                        buddyFound = True
                    else:
                        return False
                else:
                    return False
            else:
                if not sameAdj and self.__sameAdj(A[i], A[i+1], B[i], B[i+1]):
                    sameAdj = True

        return buddyFound or sameAdj
    def __sameAdj (self, a0,a1, b0, b1):
        if a0==a1 and b0 == b1:
            return True
        else:
            return False
    def __isBuddy(self,a0,a1,b0,b1):
        if a0==b1 and a1 == b0:
            return True
        else:
            return False

if __name__ == "__main__":
    buddyStringSolu = Solution()
    print (buddyStringSolu.buddyStrings('aaaaaaabc', 'aaaaaaacb') )
    # True
    print (buddyStringSolu.buddyStrings('aaaaaabbc', 'aaaaaaacb'))
    # False

    print(buddyStringSolu.buddyStrings('ab', 'ba'))
    # True

    print(buddyStringSolu.buddyStrings('aaa', 'aaa'))
    # True