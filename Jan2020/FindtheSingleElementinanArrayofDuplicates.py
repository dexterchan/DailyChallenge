# Skill: Bitwise XOR
#Given an array of integers, arr, where all numbers occur twice except one number which occurs once, find the number. Your solution should ideally be O(n) time and use constant extra space.
#Example:
#Input: arr = [7, 3, 5, 5, 4, 3, 4, 8, 8]
#Output: 7

#Analysis
# Exploit the question of all numbers occurs twice except one number
# we use chain of bitwise operator XOR to "zero" the duplicate
# With XOR property, it allow single occur number remain
# Example:
# 1 ^ 3 ^ 5 ^ 1 ^ 5 = 3
# Time complexity O(N) space complexity O(1)
class Solution(object):
    def findSingle(self, nums):
        # Fill this in.
        tmp = 0
        for n in nums:
            tmp = tmp ^ n
        return tmp



if __name__ == "__main__":
    nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
    print(Solution().findSingle(nums))
    # 3