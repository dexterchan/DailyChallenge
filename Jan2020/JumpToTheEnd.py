#Skill: Path searching, backtracking
#Difficulty: Medium
#Starting at index 0, for an element n at index i, you are allowed to jump at most n indexes ahead. Given a list of numbers, find the minimum number of jumps to reach the end of the list.

#Example:
#Input: [3, 2, 5, 1, 1, 9, 3, 4]
#Output: 2
#Explanation:

#The minimum number of jumps to get to the end of the list is 2:
#3 -> 5 -> 4

#Here's a starting point:

#Analysis
#Brutal force
#Simple recursive function:
#   findPath(at, nums) -> List(dequeue(Int))
# dequeue is to model path
#Give the start point,

#pick current number at index (n),
# iterate from 1 to n , 2 choices:
# if 0+1, 0+2 , 0+n == final index, return list(final Node: type=dequeue, cost=1)
# to call findPath(0+1), findPath(0+1), findPath(0+n)
#Gather all result of List from all path and append itself to the left of the result
# each return , appendleft to the dequeue and add 1 to the cost....
# append the list into the new output list
# In the end, iterate List(dequeue(Int)) to find the lowest cost dequeue
# Time cost: O(N^3) Space cost: O(N^2)


from typing import Deque
from typing import List
from collections import deque

class Solution:
    def jumpToEnd(self, nums):
        (pathLists) = self.__recursive(0, nums)
        mincost = (2^31)-1
        minpath = None
        for path in pathLists:
            cost = len(path)
            if cost < mincost:
                mincost = cost
                minpath = path
        #self.__debug (minpath, nums)
        return mincost-1

    def __debug(self, minpath, nums):
        for pt in minpath:
            print (nums[pt], end="->")
        print("")

    def __recursive(self, at, nums: List[int]) -> (List[Deque] ):
        N = nums[at]
        dest = len(nums) - 1
        returnPath = []
        for i in range(N, 0, -1):
            next = at + i
            if next > dest:
                continue
            elif next == dest:
                path = deque()
                path.append(at)
                path.append(dest)
                returnPath.append(path)
            else:
                subpathlist = self.__recursive(next, nums)
                if subpathlist is None:
                    continue
                for subpath in subpathlist:
                    subpath.appendleft(at)
                    returnPath.append(subpath)
        return returnPath


def jumpToEnd(nums):
    # Fill this in.
    solu = Solution()
    return solu.jumpToEnd(nums)


if __name__ == "__main__":
    print(jumpToEnd([3, 2, 4, 1, 1, 9, 3, 4]))
    # 2

    print (jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
    # 2

