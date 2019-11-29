#Skills: dynamic programming
#You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

#Example:

#[34, -50, 42, 14, -5, 86]

#Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].

#Your solution should run in linear time.

#Here's a starting point:

class Solution:
    def max_subarray_sum(self,arr):

        negsum = 0
        maxvalue = 0
        localvalue = 0


        for pos in  range(len(arr)):
            if arr[pos] < 0:
                negsum = negsum + arr[pos]
                continue

            if negsum < 0:
                if localvalue + negsum < 0:
                    #reset seq
                    negsum = 0
                    localvalue = arr[pos]
                else:
                    localvalue = localvalue + negsum
                    negsum = 0
                    localvalue = localvalue + arr[pos]
            else:
                localvalue = localvalue + arr[pos]
            maxvalue = max ( maxvalue, localvalue)
        return maxvalue



def max_subarray_sum(arr):
    solu = Solution()
    return solu.max_subarray_sum(arr)

if __name__ == "__main__":
    print (max_subarray_sum([34, -50, 42, 14, -5, 86]) )
    # 137

    print(max_subarray_sum([34, -50, 42, 14, -5, 2, 2, 2, 2, 2]))

    print(max_subarray_sum([100, -34, -50, 42,100]))