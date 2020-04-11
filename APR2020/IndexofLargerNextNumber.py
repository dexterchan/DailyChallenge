
#Given a list of numbers, for each element find the next element that is larger than the current element.
# Return the answer as a list of indices. If there are no elements larger than the current element, then use -1 instead.
#Here's an example and some starter code:

#Analysis
#initialize the blank array result as [-1]*(array length)
#scan the array,
#find the k smallest element smaller than current value
#if match, replace result with -1 of the current value
#put current element (v, index) back into the heap
#iterate next element
#Time cost: O(N) space cost O(N)

from heapq import heappush, heappop

def larger_number(nums):
    # Fill this in.
    length = len(nums)
    result = [-1] * length
    h = []
    for inx in range(length):
        while True:
            sValue, sInx = __checkHeap(h, nums[inx])
            if sValue is None:
                break
            if result[sInx] == -1:
                result[sInx] = inx
        heappush(h, (nums[inx], inx))
    return result


def __checkHeap(h:list, value) -> (int, int):
    if len(h) == 0:
        return (None, None)
    v, inx = h[0]
    if v < value:
        heappop(h)
        return (v, inx)
    else:
        return (None, None)


if __name__ == "__main__":
    # print [2, 2, 3, 4, -1, -1]
    print(larger_number([3, 2, 5, 6, 9, 8]))