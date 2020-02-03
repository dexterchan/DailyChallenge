
#MS Excel column titles have the following pattern: A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc. In other words, column 1 is named "A", column 2 is "B", column 26 is "Z", column 27 is "AA" and so forth. Given a positive integer, find its corresponding column name.
#Examples:
#Input: 26
#Output: Z

#Input: 51
#Output: AY

#Input: 52
#Output: AZ

#Input: 676
#Output: YZ

#Input: 702
#Output: ZZ

#Input: 704
#Output: AAB
#Here is a starting point:

#ANalysis
#It is a number base26 conversion problem
#Iterately divide the number by 26
# the remainder translate to Character chr(rem + 65)
# the divide carry into next loop until number = 0
from collections import deque
import math
class Solution:
    def convertToTitle(self, n):
        # Fill this in.
        num = n
        result = deque()
        while num > 0:
            rem = num % 26
            rem = 64 + ( 26 if rem == 0 else rem  )
            ch = chr (rem)
            result.appendleft( ch )
            num = max(math.ceil(num/26)-1,0)
        return "".join(result)



if __name__ == "__main__":

    print(Solution().convertToTitle(51))

    input1 = 1
    input2 = 456976
    input3 = 28
    print(Solution().convertToTitle(input1))
    # A
    print(Solution().convertToTitle(input2))
    # YYYZ
    print(Solution().convertToTitle(input3))
    # AB