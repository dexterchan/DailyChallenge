
#Given a list of integers, return the bounds of the minimum range that must be sorted so that the whole list would be sorted.

#Example:
#Input: [1, 7, 9, 5, 7, 8, 10]
#Output: (1, 5)
#Explanation:
#The numbers between index 1 and 5 are out of order and need to be sorted.

#Here's your starting point:

#Analysis
#Brutal force
#Set bound to be (0, len(list)-1)
#lower bound 0 , upper bound len(list-1)
#Run N*N iteration for all possible bounds combination
#For each iteration, sort the bound Cost (N*logN)
#Then, check the number if in ascending order
#Finally, record the shortest bound
# Time cost: N^3 (logN) space cost: O(1)

#Better solution
# Begin with lbound = 0, ubound = len(list)-1
# Run N iteration
# Each iteration, find max number and smallest number in the range Cost: N
# if index smallest number <> lbound, set tmplbound to (lbound, index smallest number), update lbound to index smallest number
# else update lbound to lbound + 1
# if index largest number <> ubound, set tmpubound to (index latest number, ubound), update ubound to index latest number
# else update ubound to ubound -1
# loop break if not lbound < ubound
# finally, check if tmplbound overlap with tmpubound.... if yes, merge them


class Solution:
    def findMinRangeForSort(self, nums):
        lbound = 0
        ubound = len(nums)-1
        tmplbound = None
        tmpubound = None

        while lbound < ubound:
            sIndex, lIndex = self._findSmallestBiggestInx(nums, lbound, ubound)
            if sIndex != lbound:
                if tmplbound is None:
                    tmplbound = [lbound, sIndex]
                else:
                    tmplbound[1] = sIndex
                lbound = sIndex
            else:
                lbound += 1

            if lIndex != ubound:
                if tmpubound is None:
                    tmpubound = [lIndex, ubound]
                else:
                    tmpubound[0] = lIndex
                ubound = lIndex
            else:
                ubound -= 1

        if tmplbound is None and tmpubound is None:
            finalBound = None
        elif tmplbound is None:
            finalBound = tmpubound
        elif tmpubound is None:
            finalBound = tmplbound
        elif tmpubound[0] <= tmplbound[1]+1:
            finalBound = [tmplbound[0], tmpubound[1]]
        else:
            finalBound = [tmplbound, tmpubound]

        return finalBound

    def _findSmallestBiggestInx(self, nums, lbound, ubound):
        sindex = lbound
        lindex = ubound
        smallest = nums[sindex]
        largest = nums[lindex]
        for i in range(lbound, ubound+1):
            if smallest > nums[i]:
                sindex = i
            if largest < nums[i]:
                lindex = i
        return sindex, lindex


def findRange(nums):
    # Fill this in.
    solu = Solution()
    return solu.findMinRangeForSort(nums)

if __name__ == "__main__":
    print(findRange([1, 2, 4, 8, 7, 10, 80, 100]))
    # (3, 4)

    print(findRange([1, 2, 9, 5, 7, 10, 4, 100]))
    # (2, 6)

    print(findRange([1, 2, 9, 5, 7, 10, 4]))
    # (2, 6)

    print (findRange([1, 7, 9, 5, 7, 8, 10]))
    # (1, 5)

    print(findRange([1, 7, 4, 5, 6, 8, 10]))
    # (1, 5)

