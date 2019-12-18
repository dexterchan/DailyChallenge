#Skill : bitwise
#Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same letters).

#Example:

#Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
#Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

#Here's a starting point:

#import collections

#Note: if we sort each word, cost will raise to O(NlogN)

# Time: O(N) Space: O(N)
class Solution:
    def groupAnagramWords(self, strList):
        m = {}
        result = []
        for ele in strList:
            ele = ele.lower()
            key = self.__createKey(ele)
            if key not in m:
                m[key] = []
            m[key].append(ele)

        for k in m.keys():
            result.append(m[k])
        return result

    def __createKey(self, str):
        numKey = 0
        for ch in str:
            num = self.__convertCh2Int(ch)
            tmp = 1 << num
            numKey = numKey | tmp
        return numKey
    def __convertCh2Int(self, ch):
        return ord(ch) - ord('a')
def groupAnagramWords(strs):
    solu = Solution()
    return solu.groupAnagramWords(strs)


if __name__ == "__main__":
    print (groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]