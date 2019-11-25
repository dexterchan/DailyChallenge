#You are given an array of integers.
# Return the largest product that can be made by multiplying any 3 integers in the array.

#Example:

#[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.
import heapq

class Solution:

    #Cost = O(n) + 2*3*log(n)
    def max_product_3(self, lst):
        heapq.heapify(lst)
        rightmax3 = heapq.nlargest(3, lst)
        leftmin3 = heapq.nsmallest(3, lst)


        p1 = leftmin3[0] * leftmin3[1] * rightmax3[0]
        p2 = leftmin3[0] * rightmax3[0] * rightmax3[1]
        p3 = rightmax3[0] * rightmax3[1] * rightmax3[2]
        return max(p1, max(p2, p3))


def maximum_product_of_three(lst):
    solu = Solution()
    return solu.max_product_3(lst)

if __name__ == "__main__":
    print (maximum_product_of_three([-4, -4, 2, 8]))
# 128
    print(maximum_product_of_three([-4, -4,-6, 2, 8]))

    print(maximum_product_of_three([-4, -4, -6, 2, -20,-20]))