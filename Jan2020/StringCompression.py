
#Given an array of characters with repeats, compress it in place.
# The length after compression should be less than or equal to the original array.

#Example:
#Input: ['a', 'a', 'b', 'c', 'c', 'c']
#Output: ['a', '2', 'b', 'c', '3']
#Here's a starting point:

#Analysis
#iterate the array
# if next pos == cur pos, then we start to compress it by ['cur ch', 'count number of character'] until next pos <> cur pos
# otherwise, leave it

class Solution(object):
    def compress(self, chars):
        # Fill this in.
        l = len(chars)
        inx = 0
        cnt = 1
        curCh = None
        nextCh = None
        result = []
        while inx < l-1:
            curCh = chars[inx]
            nextCh = chars[inx + 1]
            if curCh == nextCh:
                cnt += 1
            else:
                result.append(curCh)
                if cnt > 1:
                    result.append(cnt)
                cnt = 1
            inx += 1
        if chars[l-2] == chars[l-1]:
            result.append(chars[l-2])
            result.append(cnt)
        else:
            result.append(chars[l-1])
        return result
if __name__ == "__main__":
    print (Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
    # ['a', '2', 'b', 'c', '3']

    print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'd']))
    # ['a', '2', 'b', 'c', '2','d']

    print(Solution().compress(['a', 'b', 'b', 'c', 'c', 'd']))
    # ['a', '2', 'b', 'c', '2','d']