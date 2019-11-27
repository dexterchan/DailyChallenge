#Skill: bit manipulation, hashmap
#You are given an array of intervals - that is, an array of tuples (start, end). The array may not be sorted, and could contain overlapping intervals. Return another array where the overlapping intervals are merged.

#For example:
#[(1, 3), (5, 8), (4, 10), (20, 25)]

#This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10) can be merged into (4, 10).

#Here's a starting point:

from collections import deque

#Cost : O(n)
class BrutalForce:
    def MergeInterval(self, intervals):
        newinterval = []
        intervalmap = {}
        processStack = deque()
        for i in intervals:
            blk = self.__createblock(i)
            intervalmap[blk] = i
            processStack.append(blk)

        while len(processStack) != 0:
            p = processStack.popleft()
            if p not in intervalmap:
                continue
            blk = intervalmap[p]
            del intervalmap[p]
            isMerged, newKey = self.__checkAnyOverlapAndMerge(intervalmap, p, blk)
            if isMerged:
                processStack.appendleft(newKey)
            else:
                intervalmap[p] = blk

        for k in intervalmap.keys():
            newinterval.append(intervalmap[k])
        return newinterval

    def __checkAnyOverlapAndMerge(self, m, key, blk):
        for chkKey in m.keys():
            if chkKey & key:
                mergeToBlk = m[chkKey]
                del m[chkKey]
                newmin = min (mergeToBlk[0], blk[0])
                newmax = max (mergeToBlk[1], blk[1])
                newkey = chkKey | key
                m[newkey] = (newmin, newmax)
                return True, newkey

        return False, None

    #Create block of range
    #e.g. (5, 8) gives 0b11100000
    def __createblock(self, i):
        right = (1 << (i[0] + 1)) - 1
        left = (1 << (i[1])) - 1
        lr = right ^ left
        lr = lr | (1 << i[0])
        return lr

# Very bad implementation..... extremely slow when reading bitmap result
class BitManipulation:
    def MergeByBits(self, intervals):
        bitmap = 0
        for i in intervals:
            bitmap = self.__fill(bitmap, i)

        return self.__readbitmap(bitmap)

    def __fill(self, bitmap, i):
        right = (1 << (i[0]+1)) - 1
        left = (1 << (i[1])) - 1
        lr = right ^ left
        lr = lr | (1<<i[0])
        bitmap = bitmap | lr
        return bitmap

    def __readbitmap(self, bitmap):
        high = 0
        low = 0
        result = []
        foundRange = False
        for i in range(2<<10-1):
            if not foundRange:
                if bitmap & 1 :
                    low = i
                    high = i
                    foundRange = True
            else:
                if bitmap & 1 == 0:
                    foundRange = False
                    high = i
                    result.append((low, high))
                else:
                    high = i
            bitmap = bitmap>>1
        return result


def merge(intervals):
    solu = BrutalForce()
    return solu.MergeInterval(intervals)

if __name__ == "__main__":
    print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))


    # [(1, 3), (4, 10), (20, 25)]

    print(merge([(1, 3), (5, 8), (2, 10), (20, 25)]))