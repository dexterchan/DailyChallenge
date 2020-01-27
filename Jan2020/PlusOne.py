
#Given a non-empty array where each element represents a digit of a non-negative integer, add one to the integer. The most significant digit is at the front of the array and each element in the array contains only one digit. Furthermore, the integer does not have leading zeros, except in the case of the number '0'.

#Example:
#Input: [2,3,4]
#Output: [2,3,5]

#Analysis
#iterate the array from right to left
#for most right digit, add one to digit
#each iteration , we have digit + carry
#check if (digit+carry) > 9,
# if yes, carry = 1, d-=10
# left append digit to result... result should be double linked queue
# in the end, transform double linked queue to list for output
from collections import deque
class Solution():
    def plusOne(self, digits):
        # Fill this in.
        l = len(digits)
        carry = 0
        result = deque()
        for inx in range(l-1, -1, -1):
            d = digits[inx]
            if inx == l-1:
                d += 1
            d += carry
            if d > 9:
                carry = 1
                d -= 10
            else:
                carry = 0
            result.appendleft(d)
        if carry != 0:
            result.appendleft(1)
        return list(result)


if __name__ == "__main__":
    num = [2, 9, 9]
    print(Solution().plusOne(num))
    # [3, 0, 0]
    num = [9, 9, 9]
    print(Solution().plusOne(num))
