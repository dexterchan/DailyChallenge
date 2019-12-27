#Skill: array
#Difficulty: Medium
#You are given an array of integers. Return the length of the longest increasing subsequence (not necessarily contiguous) in the array.

#Example:
#[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

#The following input should return 6 since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.


#Analysis
#By Brutal force
#It scan each number for longest subsequence,
#Cost O(N!) Space O(1)

#By back tracking
#First iteration, for each number, find number of integer (L) on the right larger than current number
# Cost O(N^2)
#Find largest L in the window
#Recusively, find largest L in the window on the right until window size = 1
# Cost O(N^2) --- N+(N-1)+....+2+1 steps




def lis(arr):
    # to allow the access of global variable
    global maximum

    # lenght of arr
    n = len(arr)

    # maximum variable holds the result
    maximum = 1

    def _lis(arr, n):
        # to allow the access of global variable
        global maximum

        # Base Case
        if n == 1:
            return 1

        # maxEndingHere is the length of LIS ending with arr[n-1]
        maxEndingHere = 1

        """Recursively get all LIS ending with arr[0], arr[1]..arr[n-2] 
           IF arr[n-1] is maller than arr[n-1], and max ending with 
           arr[n-1] needs to be updated, then update it"""
        for i in range(1, n):
            res = _lis(arr, i)
            if arr[i - 1] < arr[n - 1] and res + 1 > maxEndingHere:
                maxEndingHere = res + 1

        # Compare maxEndingHere with overall maximum. And
        # update the overall maximum if needed
        maximum = max(maximum, maxEndingHere)

        return maxEndingHere
    # The function _lis() stores its result in maximum
    _lis(arr, n)

    return maximum

class Solution():
    def longestIncreasingSubSequence(self, input):
        result = []

        nlr = self.__findNumberOfIntegerLargerOnRight(input)

        self.__rescursiveFindSubSequence(input, nlr, result)

        return result

    def __rescursiveFindSubSequence(self, number, nlr, result):
        l = len(nlr)
        if l == 0:
            return
        maxFreq = 0
        inx = 0


        for i in range(l):
            if nlr[i] > maxFreq:
                maxFreq = nlr[i]
                inx = i
        if maxFreq == 0:
            return
        result.append(number[inx])

        return self.__rescursiveFindSubSequence(number[inx+1:], nlr[inx+1:], result)


    def __findNumberOfIntegerLargerOnRight(self, input):
        l = len(input)
        freq = [0] * l
        for i in range(l):
            f = 0
            for j in range (i+1, l):
                if input[j] >= input[i]:
                    f += 1
            freq[i] = f
        return freq



def longestIncreasingSubSequence(input):

    return lis(input)

if __name__ == "__main__":
    input = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    result = longestIncreasingSubSequence(input)
    print(result)