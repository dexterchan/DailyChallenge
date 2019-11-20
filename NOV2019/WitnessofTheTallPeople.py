# Skiils : array traversal
#There are n people lined up, and each have a height represented as an integer.
# A murder has happened right in front of them,
# and only people who are taller than everyone in front of them
# are able to see what has happened. How many witnesses are there?

#Input: [3, 6, 3, 4, 1]
#Output: 3

#
 #
 # #
####
####
#####
#36341                                 x (murder scene)

class Solution:
    def countWitness(self, heights):
        witness = self.__findWitnessBrutalForce(heights)
        return len(witness)

    def __findWitnessBrutalForce(self, heights):
        l = len(heights)

        witnessSet = set()
        lastHeight = heights[l - 1]
        witnessSet.add(l-1)

        for i in range (l-3, -1, -1):
            if heights[i] > lastHeight:
                witnessSet.add(i)
                lastHeight = heights[i]
        return witnessSet





def witnesses(heights):
    solu = Solution()
    return solu.countWitness(heights)

if __name__ == "__main__":
    print (witnesses([3, 6, 3, 4, 1]))
    # 3