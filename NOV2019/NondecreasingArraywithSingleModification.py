#You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

#We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

#Example:

#[13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.

#[13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.

class Solution:
    def check(self, lst):
      # Fill this in.
        offenseNum = 0
        lastNum = lst[0]
        for n in lst[1:]:
            if ( lastNum <=n ):
                offenseNum = offenseNum + 1
            else:
                lastNum = n
            if(offenseNum > 1):
                return False
        return True


if __name__ == "__main__":
    print (Solution().check([13, 4, 7]))
    # True
    print (Solution().check([5,1,3,2,5]))
    # False