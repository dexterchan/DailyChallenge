
#The h-index is a metric that attempts to measure the productivity and citation impact of the publication of a scholar.
# The definition of the h-index is if a scholar has at least h of their papers cited h times.

#Given a list of publications of the number of citations a scholar has, find their h-index.

#Example:
#Input: [3, 5, 0, 1, 3]
#Output: 3
#Explanation:
#There are 3 publications with 3 or more citations, hence the h-index is 3.

#Here's a starting point:

#Analysis
# scan the list
# find the map of citation frequency vs number of publication: map[citation] = number of publication cost(N)
# also , push the citation to priority queue h (Max - citation, citation) cost(logN)


# pop priority queue item -> hIndex, find the number of publication cost(logN)
# if hIndex = new pop item from priority queue , skip
# get numberOfPublication = numberOfPublication + m [new hindex]
# if hIndex > number of publication, pop another item from priority queue
# until we have hIndex <= number of publication

# Time Cost: O(Nlog(N)) Space cost O(N)

from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def hIndex(self, publications):
        m = defaultdict(int)
        h = []
        MAX = (2^31) - 1
        for c in publications:
            m[c] = m[c] + 1
            heappush(h, (MAX - c, c))

        hIndex = -1
        numberOfPublication = 0
        while len(h) > 0:
            key, newC = heappop(h)
            if newC == hIndex:
                continue
            else:
                hIndex = newC
            numberOfPublication = numberOfPublication + m[hIndex]
            if hIndex <= numberOfPublication:
                break
        return hIndex


def hIndex(publications):
    # Fill this in.
    solu = Solution()
    return solu.hIndex(publications)
if __name__ == "__main__":
    print (hIndex([5, 3, 3, 1, 0]))
    # 3

    print(hIndex([5, 3, 3, 1, 4, 4, 4, 0]))