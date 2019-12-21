#Skill: array traversal

#Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

#Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

#Note: You are not suppose to use the library’s sort function for this problem.

#Can you do this in a single pass?

#Example:
#Input: [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]
#Here's a starting point:
class ConstantSolution:

  #Cost: O(N) space O(1)
  def sortColors(self, nums):

      inx = 0
      redinx = -1
      whiteinx = len(nums)

      while inx < len(nums) and redinx <= whiteinx:
          color = nums[inx]
          if color == 0:
              if redinx < inx:
                  redinx += 1
                  if nums[redinx] != 0:
                      self.__swap(nums, inx, redinx)
                  continue
              else:
                  inx += 1
          elif color == 1:
              inx += 1
          else:
              if inx < whiteinx:
                  whiteinx -= 1
                  if nums[whiteinx] != 2:
                      self.__swap(nums, inx, whiteinx)
                  continue
              else:
                  inx += 1
      return nums


  def __swap(self, nums, pos1, pos2):
      org = nums[pos1]
      nums[pos1] = nums[pos2]
      nums[pos2] = org

class Solution:
  # Cost: O(N) space O(N)
  def sortColors(self, nums):
      redlst = []
      whitelst = []
      bluelst = []


      for inx in range(len(nums)):
          color = nums[inx]
          if color == 0:
            redlst.append(inx)
          elif color == 1:
            whitelst.append(inx)
          elif color == 2:
            bluelst.append(inx)
      nums.clear()
      for r in redlst:
        nums.append(0)
      for w in whitelst:
        nums.append(1)
      for b in bluelst:
        nums.append(2)
      return nums


if __name__ == "__main__":
  nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
  print("Before Sort: ")
  print(nums)
  # [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

  ConstantSolution().sortColors(nums)
  print("After Sort: ")
  print(nums)
  # [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]