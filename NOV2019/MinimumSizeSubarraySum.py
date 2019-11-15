# Skill: dynamic programming
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.


class Solution:
    def minSubArrayLen(self, nums, s):
        minlen, pos = self.__minSubArrayLenBrutal(nums, s)
        #print(pos)
        return minlen

    def __minSubArrayLenBrutal(self, nums, s):
        lenNum = len(nums)
        minLength = lenNum + 1
        pos = -1
        for i in range(0, lenNum ):
            sumvalue = nums[i]
            for j in range(i, lenNum):
                if i != j:
                    sumvalue = sumvalue + nums[j]
                if (sumvalue >= s):
                    if(minLength > j-i+1):
                        minLength = j - i+1
                        pos = i
                    break

        if(minLength == lenNum+1):
            return 0, pos
        else:
            return minLength, pos


if __name__ == "__main__":
    print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))

    print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 4))

    print(Solution().minSubArrayLen([8, 3, 5, 2, 1, 10], 10))
