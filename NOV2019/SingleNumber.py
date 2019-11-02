#Given a list of numbers, where every number shows up twice except for one number, find that one number.

#Example:
#Input: [4, 3, 2, 4, 1, 3, 2]
#Output: 1

def singleNumber(nums):
  # Fill this in.
    #numOccur = {}
    candidates = set()
    blacklist = set()
    for n in nums:
        if ( n in candidates or n in blacklist):
            candidates.remove(n)
            blacklist.add(n)
            continue;
        else:
            candidates.add(n)

    return candidates


if __name__ == "__main__":
    print (singleNumber([4, 3, 2, 4, 1, 3, 2]) )
# 1
    print(singleNumber([10,4, 3, 2, 4, 1, 3, 2]))
# 1, 10
