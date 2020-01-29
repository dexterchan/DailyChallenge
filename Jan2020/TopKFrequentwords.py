
#Given a non-empty list of words, return the k most frequent words.
# The output should be sorted from highest to lowest frequency,
# and if two words have the same frequency, the word with lower alphabetical order comes first.
# Input will contain only lower-case letters.

#Example:
#Input: ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"], k = 2
#Output: ["pro", "daily"]

#get the frequency of each word
#Save frequency of each word into heap Cost O(N)
#custom the comparison lambda with highest frequency and lower alphabetical order
#Finally return first k element from heap Cost (klogN)
from collections import defaultdict
from heapq import heappush, heappop
from typing import ByteString

class Node(object):
    def __init__(self, val: int, sval ):
        self.val = val
        self.sval = sval

    def __repr__(self):
        return f'Node value: {self.val} {self.sval}'

    def __lt__(self, other):
        if self.val == other.val:
            return self.sval < other.sval
        else:
            return other.val < self.val

class Solution(object):
    def topKFrequent(self, words, k):
        # Fill this in.
        Freq = defaultdict(int)
        H = []
        result = []
        for w in words:
            f = Freq[w]
            Freq[w] = f + 1
        for w in Freq.keys():
            n = Node(Freq[w], w)
            heappush(H, n)
        for i in range(k):
            n = heappop(H)
            result.append(n.sval)
        return result

if __name__ == "__main__":
    words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
    k = 2
    print(Solution().topKFrequent(words, k))
    # ['pro', 'daily']

    words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems","daily"]
    k = 2
    print(Solution().topKFrequent(words, k))