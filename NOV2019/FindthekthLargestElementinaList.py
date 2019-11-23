#Skill: heap
#Given a list, find the k-th largest element in the list.
#Input: list = [3, 5, 2, 4, 6, 8], k = 3
#Output: 5
#Here is a starting point:
from heapq import heappush
from heapq import heappop
import sys

#O(n) create a heap
#O(k log n) to retrieve kth element
class Solution:
    def findKthLargest(self, nums, k):
        h = []
        kth = 0
        maxint = (1 << 63)-1
        for n in nums:
            heappush(h, (maxint-n, n))
        for i in range(k):
            kth = heappop(h)[1]
        return kth


def findKthLargest(nums, k):
    solu = Solution()
    return solu.findKthLargest(nums,k)



if __name__ == "__main__":
    print ( findKthLargest([3, 5, 2, 4, 6, 8], 3) )
    # 5