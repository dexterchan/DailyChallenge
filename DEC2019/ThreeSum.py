
#Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0. Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.

#Example:
#Input: nums = [0, -1, 2, -3, 1]
#Output: [0, -1, 1], [2, -3, 1]
#Here's a starting point:
from typing import List

class Solution_Sort:
    def threeSum(self, nums: List[int]) -> List[ List[int] ] :
        nums.sort()

        res = []
        l = len(nums)
        for i in range (l-2):
            k = i + 1
            j = l - 1
            while k < j:
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.append([nums[i], nums[k], nums[j]])
                    break
                elif s > 0:
                    j = j - 1
                else:
                    k = k + 1

        return res






class Solution(object):
    def threeSum(self, nums):

        numberAddressMap = self.__getNumberAddressMap(nums)
        TwoSumMap = self.__calculateTwoSumMap(nums, numberAddressMap)

        #Combine result
        address = set()
        for key in TwoSumMap.keys():
            twosumtuples = TwoSumMap[key]
            finalNumbers = numberAddressMap[key]
            for tuple in twosumtuples:
                for f in finalNumbers:
                    x = f
                    y = tuple[0]
                    z = tuple[1]
                    r = [x, y ,z]
                    r.sort()
                    address.add( (r[0], r[1], r[2]) )
        result = []
        for tuple in address:
            result.append([ nums[tuple[0]],nums[tuple[1]],nums[tuple[2]] ] )

        return result


    #Cost : O(N) space O(N^2)
    def __getNumberAddressMap(self, nums):
        l = len (nums)
        numberAddressMap = {}
        for i in range(l):
            n = nums[i]
            if n not in numberAddressMap:
                numberAddressMap[n] = set()
            numberAddressMap[n].add(i)
        return numberAddressMap


    #Cost : O(N^2) space O(N^2)
    def __calculateTwoSumMap(self, nums, numberAddressMap):
        l = len(nums)
        TwoSumMap = {}
        for i in range(l-1):
            for j in range(i+1, l):
                s = nums[i] + nums[j]
                s = -s
                #filter result
                if s in numberAddressMap:
                    if i in numberAddressMap[s]:
                        continue
                    if j in numberAddressMap[s]:
                        continue
                    if s not in TwoSumMap:
                        TwoSumMap[s] = []
                    TwoSumMap[s].append((i, j))
        return TwoSumMap


# Test Program
if __name__ == "__main__":
    nums = [1, -2, 1, 0, 5]
    print(Solution().threeSum(nums))
    # [[-2, 1, 1]]

    nums = [0, -1, 2, -3, 1]
    print(Solution_Sort().threeSum(nums))

    nums = [-1,0, 1, 2, -1, -4]
    print(Solution_Sort().threeSum(nums))