# Dynamic programming
#Given a sorted list of positive numbers, find the smallest positive number that cannot be a sum of any subset in the list.

#Example:
#Input: [1, 2, 3, 8, 9, 10]
#Output: 7
#Numbers 1 to 6 can all be summed by a subset of the list of numbers, but 7 cannot.

#Analysis
#Trick to keep time cost within O(N^2) space cost O(N^2) without using O(exp) as brutal force
#Iterate the array with variable
#inx = 0
#expect = nums[inx]
#a) fresh the dynamic memory 2d map.... map requires photo scan in written form
#b) for each new element in the map ... cache in another hashset

#1) expect = nums[inx]
#2) if expect < nums[inx+1] check if expect in the hashset, if yes, expect++, and loop back to 2
#3) if not found in hashset, expect is the missing number
#4) if expect == nums[inx+1], increment inx, then run (a),(b) to update dynmaic memory and hashset, loop back to 2

# Populate D at level lv
# D[lv][j] = D[lv-1][j] + newvalue for j = 0
# D[lv-i][j] = D[lv-i-1][j-1] + newvalue

class Solution:
    def findSmallest(self, nums):
        l = len(nums)
        M = set()
        D = []
        inx = 0

        expect = nums[inx]
        self.__updateMD(nums, inx, M, D)
        while inx < l-1:
            if expect < nums[inx + 1]:
                if expect in M:
                    expect += 1
                    continue
                else:
                    return expect
            elif expect == nums[inx+1]:
                inx += 1
                self.__updateMD(nums, inx, M, D)
            else :
                return None
        return None

    def __updateMD(self, nums, inx, M, D):
        value = nums[inx]
        newRow = []
        D.append(newRow)
        for i in range(inx, -1, -1):
            if i-1 >= 0:
                preRow = D[i-1]
                for oldValue in preRow:
                    newValue = oldValue + value
                    D[i].append(newValue)
                    M.add(newValue)
            if i==0:
                D[i].append(value)
                M.add(value)




def findSmallest(nums):
    # Fill this in.
    solu = Solution()
    return solu.findSmallest(nums)


if __name__ == "__main__":
    print (findSmallest([1, 2, 3, 8, 9, 10]))
    # 7

    print(findSmallest([1, 2, 3,4, 8, 9, 10]))
    # None

    print(findSmallest([1, 2, 3, 7, 9, 100]))
    # 23