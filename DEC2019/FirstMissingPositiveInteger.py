#Skill: array iteration
#You are given an array of integers. Return the smallest positive integer that is not present in the array. The array may contain duplicate entries.

#For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist in the array.

#Your solution should run in linear time and use constant space.

#Here's your starting point:

class Solution:

    #Cost: O(N), Space(1)
    def first_missing_positive(self, nums):
        #First pass to find +ve boundaries
        low = (1<<31) - 1
        high = 0
        for i in nums:
            if low > i and i>0:
                low = i
            if high < i:
                high = i

        # K pass to find first missing positive
        firstMiss = low + 1
        searchmiss = firstMiss
        found = False
        kill = False
        l = len(nums)
        inx = 0
        while (not kill) and (not found) :
            if nums[inx] < low or nums[inx] > high:
                inx += 1
                continue
            if nums[inx] == searchmiss:
                searchmiss = searchmiss + 1

            inx += 1
            if inx < l:
                continue
            else:
                inx = 0
                if searchmiss == firstMiss:
                    found = True
                else:
                    firstMiss = searchmiss
        if firstMiss > high or firstMiss < low:
            return None
        else:
            return firstMiss


def first_missing_positive(nums):
    solu = Solution()
    return solu.first_missing_positive(nums)

if __name__ == "__main__":
    print(first_missing_positive([8, 7, 2, 3, 4, 5, -1, 10, 6, 1]))

    print(first_missing_positive([7, 2, 3, 4, 5, -1, 10, 6, 1]))

    print(first_missing_positive([7, 2, 3, 4, 5, -1, 1]))

    print (first_missing_positive([3, 4, -1, 1]))
    # 2