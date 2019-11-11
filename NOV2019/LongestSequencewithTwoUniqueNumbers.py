#Skill : array, dynamic programming

#Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.

#Example:
#Input: [1, 3, 5, 3, 1, 3, 1, 5]
#Output: 4

#The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]

class Solution:

    def findSequenceHelper (self, seq):
        #res = self.__findSequenceBrutalForce(seq)
        res = self.__findSequenceDynamic(seq)
        #print ("substring start at %d" % res[1])
        return res[0]

    #O(N^2)
    def __findSequenceBrutalForce(self, seq):
        inx = 0
        maxLen = 0
        pos = None
        while inx < len(seq)-1:
            unqiueset = set()
            myLength = 1
            unqiueset.add(seq[inx])
            for j in range(inx+1, len(seq)):
                unqiueset.add(seq[j])
                if len(unqiueset) <= 2:
                    myLength = myLength + 1
                elif len(unqiueset) > 2:
                    break
            if (maxLen < myLength and len(unqiueset) >= 2):
                pos = inx
                maxLen = myLength
            inx = inx + 1
        return maxLen, pos

    #O(N)
    def __findSequenceDynamic(self, seq):
        inx = 1
        maxLen = 0
        pos = 0
        uniqueset = set()
        myLength = 1
        lastNum = seq[0]
        uniqueset.add(lastNum)

        posMap = {}

        while inx < len(seq):
            cur = seq[inx]
            uniqueset.add(cur)
            if len(uniqueset) > 2:
                uniqueset.clear()
                uniqueset.add(seq[pos+2])
                uniqueset.add(seq[pos+1])
                if maxLen < myLength:
                    maxLen = myLength
                    posMap[maxLen] = pos
                myLength = 2
                pos = pos + 1
                inx = pos + 1
            else:
                myLength = myLength + 1

            inx = inx + 1
        if maxLen < myLength:
            maxLen = myLength
            posMap[maxLen] = pos

        return maxLen, posMap[maxLen]

def findSequence(seq):
    solu = Solution()
    return solu.findSequenceHelper(seq)

#print (findSequence([1, 3, 5, 3, 1, 3, 1, 5]) )
# 4
print (findSequence([1, 3, 0, 1, 1, 3, 1, 5]) )