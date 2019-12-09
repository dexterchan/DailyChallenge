
#You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most k distinct characters.

#For instance, given the string:
#aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.

#Here's a starting point:

class NotYetImplemented (Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self, *args, **kwargs)


class Solution:

    def longest_substring_with_k_distinct_characters(self, s, k):
        return self.__longest_substring_with_k_distinct_charactersHelper(s, k)

    def __longest_substring_with_k_distinct_charactersHelper(self, s, k):
        brutalForce = True
        if brutalForce:
            substr = self.__brutalForce(s, k)
            print ("SubString is %s" % (substr))
            return len(substr)
        else:
            raise NotYetImplemented("Not yet implemented")
        return substr

    #Cost: O(N^2) Space: O(N)
    def __brutalForce(self, s, k):
        lsubstr=""
        l = len(s)
        sbset=set()
        i = 0

        while i < l-1:
            sbset.clear()
            sbset.add(s[i])
            for j in range(i+1, l):
                sbset.add(s[j])
                if len(sbset) > k:
                    j = j - 1
                    break
            if (j - i + 1) > len(lsubstr):
                lsubstr = s[i:j+1]
            i = i + 1
        return lsubstr




def longest_substring_with_k_distinct_characters(s, k):
    solu = Solution()
    return solu.longest_substring_with_k_distinct_characters(s, k)


if __name__ == "__main__":
    print (longest_substring_with_k_distinct_characters('aabcdefff', 3))
    # 5 (because 'defff' has length 5 with 3 characters)