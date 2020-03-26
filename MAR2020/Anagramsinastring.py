
#Given 2 strings s and t, find and return all indexes in string s where t is an anagram.

#Here's an example and some starter code:

#Analysis
# brutal force : need exponential steps to find out all possibilities of anagram of t
# better way...
# Use map of numbers
# record the number of occurance of each character into the map
# each iteration duplicate the map
# then iterate the substring of s beginning from index 0
# check if character hit the map..
# if hit map, reduce the number by 1.... if the final value >=0, assign back to map
# if find -ve number, not find the anagram
# move into next character and start again
#Time complexity : O(N*k)

from collections import defaultdict
from copy import deepcopy

class Solution():

    def find_anagrams(self, s, t):
        seedMap = self.__constructMap(t)

        for i in range(len(s) - len(t)+1):
            ss = s[i:i+len(t)]
            m = deepcopy(seedMap)
            for c in ss:
                v = m[c]
                m[c] = v - 1
                if m[c] < 0:
                    break
            clean = True
            for k,v in m.items():
                if v != 0:
                    clean = False
                    break
            if clean:
                return [i, i+len(t)+1]

        return None


    def __constructMap(self, t):
        m = defaultdict(int)
        for c in t:
            m[c] = m[c] + 1
        return m

def find_anagrams(s, t):
    # Fill this in.
    solu  = Solution()
    return solu.find_anagrams(s, t)

if __name__ == "__main__":
    print(find_anagrams('acdbacdacb', 'abc'))
    # [3, 7]
