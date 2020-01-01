
#Write a function that reverses the digits a 32-bit signed integer, x.
# Assume that the environment can only store integers within the 32-bit signed integer range, [-2^31, 2^31 - 1].
# The function returns 0 when the reversed integer overflows.

#Example:
#Input: 123
#Output: 321
class Solution:
    def reverse(self, x):
        rNum = 0
        input = x
        neg = False

        if x < 0:
            neg = True
            input *= -1

        while input>0:
            d = input % 10
            rNum = rNum * 10 + d
            input = input // 10

        if neg:
            rNum *= -1
        if rNum >= (1<<31) - 1 or rNum < -(1<<31):
            return 0
        return rNum

if __name__ == "__main__":
    print(Solution().reverse(123))
    # 321
    print(Solution().reverse(2**31))
    # 0
    print(Solution().reverse(-(2 ** 31)))
    # 0
    print(Solution().reverse(-(31423)))
    # 0