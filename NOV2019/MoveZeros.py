#Skills: array iteration
#Given an array nums, write a function to move all 0's to the end of it
# while maintaining the relative order of the non-zero elements.

#Example:
#Input: [0,1,0,3,12]
#Output: [1,3,12,0,0]
#You must do this in-place without making a copy of the array.
#Minimize the total number of operations.


class Solution:
    def moveZeros(self, nums):
        l = len(nums)
        scanpos = 0
        fixpos = 0

        while scanpos < l:
            if nums[scanpos] != 0:
                nums[fixpos] = nums[scanpos]
                fixpos = fixpos + 1
            scanpos = scanpos + 1

        #Pending zeros at the end
        while fixpos < l:
            nums[fixpos] = 0
            fixpos = fixpos + 1

        return nums


if __name__ == "__main__":
    nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
    Solution().moveZeros(nums)
    print(nums)
    # [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]