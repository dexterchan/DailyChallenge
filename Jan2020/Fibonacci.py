
#The Fibonacci sequence is the integer sequence defined by the recurrence relation:
# F(n) = F(n-1) + F(n-2), where F(0) = 0 and F(1) = 1. In other words,
# the nth Fibonacci number is the sum of the prior two Fibonacci numbers. Below are the first few values of the sequence:

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

#Given a number n, print the n-th Fibonacci Number.
#Examples:
#Input: n = 3
#Output: 2

#Input: n = 7
#Output: 13
#Here's a starting point:

#Analysis
# recursive
# Time cost: O(exp) Space cost: O(N)

# recursive with memory
# Time cost: O(N) Space cost: O(N)

class Solution():
    def fibonacci(self, n):
        # fill this in.
        return self.__itwithMemory(n)

    def __recursive(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.__recursive(n-1) + self.__recursive(n-2)

    def __itwithMemory(self, n):
        m = {}
        return self.__itwithMemoryHelper(n, m)

    def __itwithMemoryHelper(self, n, m):
        if n == 0:
            return 0
        if n == 1:
            return 1
        f1 = self.__getCache(n-1, m)
        f2 = self.__getCache(n-2, m)
        return f1 + f2

    def __getCache(self, n, m):
        if n in m:
            return m[n]
        else:
            v =  self.__itwithMemoryHelper(n, m)
            m[n] = v
            return v


if __name__ == "__main__":
    n = 9
    print(Solution().fibonacci(n))
    # 34