
#Given a number n, find the least number of squares needed to sum up to the number.

#Here's an example and some starting code:
#Analysis:
#Brutal force: exhaust all combination
#Easier way,
#square root the number, get the remainder of number - int(root) * int(root)
# if remainder <>0, run same function again
# time cost: O(logN), space complexity O(logN)
import math
from typing import List

class Solution():
    def square_sum(self, n):
        l = self.__sqhelper(n)
        #print(l)
        return len(l)

    def __sqhelper(self, n)->List[int]:
        root = math.sqrt(n)
        root = int (root)
        remainder = n - root*root
        if remainder == 0:
            return [root]
        l = self.__sqhelper(remainder)
        l.append(root)
        return l

def square_sum(n):
    # Fill this in.
    solu = Solution()
    return solu.square_sum(n)

if __name__ == "__main__":
    print(square_sum(13))
    # Min sum is 3^2 + 2^2
    # 2

    print(square_sum(19))
