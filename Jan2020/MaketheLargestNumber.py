
#Given a number of integers, combine them so it would create the largest number.

#Example:
#Input:  [17, 7, 2, 45, 72]
#Output:  77245217

#Analysis
#Sort the array by custom comparer:
# (A,B) -> return AB/(10 ** num of digit of AB) - BA / (10 ** num of digit of BA)
# we want to normalize the combination to avoid bias to long number
# After getting the sorted list
# merge all numbers
# Time cost : O(NlogN) for sorting Space cost: O(1)

from functools import cmp_to_key, reduce
from math import log


class Solution:
    def largestNum(self, nums):
        nums = sorted(nums, key=cmp_to_key(self.__compare))
        result = reduce(lambda A,B : self.__merge(A,B), nums)
        return int(result)

    def __compare(self, B, A):
        left = self.__merge(A, B)
        right = self.__merge(B, A)
        lDigit = self.__digits(left)
        rDigit = self.__digits(right)

        return left/(10**lDigit) - right/(10**rDigit)

    def __digits(self, n):
        return (log(n) // log (10))

    def __merge(self, n1, n2):
        if n2 > 0:
            numDigits = 1 + self.__digits(n2)
        else:
            numDigits = 0
        return n1 * (10 ** numDigits) + n2

def largestNum(nums):
    # Fill this in.
    solu = Solution()
    return solu.largestNum(nums)


if __name__ == "__main__":
    print(largestNum([7, 45, 72]))

    print(largestNum([ 9,  45, 822]))

    print (largestNum([17, 7, 2, 45, 72]) )
    # 77245217