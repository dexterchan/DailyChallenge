class Solution:
    def getRange(self, arr, target):
        found = False
        start = -1
        end = -1
        for inx, e in enumerate ( arr):
            if(  not found and e == target):
                found = True
                start = inx
                end = start
                while (end < len(arr) ):
                    if (arr[end] == target):
                        end = end + 1
                    else:
                        return [start, end-1]

        return [start, max(end-1,-1) ]


if __name__ == '__main__':
    # Fill this in.

    # Test program
    arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
    x = 2
    print(Solution().getRange(arr, x))
    # [1, 4]

    arr = [1, 2, 2, 2, 2]
    x = 2
    print(Solution().getRange(arr, x))
    # [1, 4]

    arr = [1, 5]
    x = 2
    print(Solution().getRange(arr, x))
    # [1, 4]