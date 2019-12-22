#Skill : state, array iteration
#Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

#Example:
#Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
#Output: ['0->2', '5->5', '7->11', '15->15']
#Assume that all numbers will be greater than or equal to 0, and each element can repeat.

#Here is a starting point:

SEARCH = 0
FOUND = 1

class Solution():
    def findRanges(self,nums):
        l = len(nums)
        pos = 0
        result = []
        value = nums[pos]
        curStart = value


        while pos < l - 1:
            if (nums[pos+1] - value) <= 1:
                pos += 1
                value = nums[pos]
                continue
            else:
                endvalue = nums[pos]
                result.append("{}-{}".format(curStart, endvalue))
                curStart = nums[pos+1]
                pos += 1
                value = nums[pos]
        result.append("{}-{}".format(curStart, nums[l-1]))
        return result

def findRanges(nums):
    solu = Solution()
    return solu.findRanges(nums)

if __name__ == "__main__":
    print (findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
    # ['0->2', '5->5', '7->11', '15->15']

    print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 12]))
    # ['0->2', '5->5', '7->11', '15->15']