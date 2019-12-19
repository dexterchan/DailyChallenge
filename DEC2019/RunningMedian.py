# Skill: Heap
#You are given a stream of numbers. Compute the median for each new element .

#Eg. Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2, 2]

#Here's a starting point:
from heapq import heappush, heappop

#How's brutal force?
# Each time, we insert a new number into array
# find the number into correct order cost: N
# insert the number cost: N
# get the median by pointing at middle of array
# Time Cost for inserting N numbers : O(N^2)
# Space Cost : O(1)

# How's Heap?
# Setup two Heap:
# Left Heap storing numbers of the left of median
# Right Heap storing numbers of the right of median
# Each time, we insert a new number into Heap
# insert the number into one of heap cost: log(N)
# After each insert, rebalance left and right heap
# Cost : 2 * log(N)
# In each iteration, peek the highest number from left heap and lowest number from right heap
# Work out median from result from two heap
# Time Cost for inserting N numbers: O(Nlog(N)
# Space Cost: O(N)



class Heap:
    def __init__(self, ishigh = False):
        self.heap = []
        self.MAX = 1 << 31
        self.isHigh = ishigh

    def pushHeap(self, number):
        KEY = (self.MAX - number) if self.isHigh else number
        heappush(self.heap, (KEY, number))

    def popHeap(self):
        n = heappop(self.heap)
        return n[1]
    def peek(self):
        if len(self.heap) > 0:
            return self.heap[0][1]
        else:
            return None
    def __len__(self):
        return len(self.heap)


class HeapSolution:

    def running_median(self, stream):
        result = []
        leftHeap = Heap(True)
        rightHeap = Heap(False)

        for n in stream:
            if len(leftHeap)==0:
                leftHeap.pushHeap(n)
                result.append(n)
                continue
            peekleftHeap = leftHeap.peek()
            if peekleftHeap > n:
                leftHeap.pushHeap(n)
            else:
                rightHeap.pushHeap(n)

            if len(leftHeap)>len(rightHeap) + 1:
                self.__rebalance (leftHeap, rightHeap)
            elif len(rightHeap) > len(leftHeap) + 1:
                self.__rebalance (rightHeap, leftHeap)

            if len(leftHeap) == len(rightHeap):
                v1 = leftHeap.peek()
                v2 = rightHeap.peek()
                result.append((v1+v2)/2)
            elif len(leftHeap) > len(rightHeap):
                v = leftHeap.peek()
                result.append(v)
            else:
                v = rightHeap.peek()
                result.append(v)
        return result

    def __rebalance (self, h1, h2):
        value = h1.popHeap()
        if value is None:
            raise Exception("h1 is None")
        h2.pushHeap(value)

def running_median(stream):
    # Fill this in.
    solu = HeapSolution()
    return solu.running_median(stream)


if __name__ == "__main__":
    m = running_median([2, 1, 4, 7, 2, 0, 5])
    print(m)
# 2 1.5 2 3.0 2 2.0 2
