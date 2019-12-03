#Skills: array iteration

#You have a landscape, in which puddles can form. You are given an array of non-negative integers representing the elevation at each location. Return the amount of water that would accumulate if it rains.

#For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
#       X
#   X███XX█X
# X█XX█XXXXXX
# [0,1,0,2,1,0,1,3,2,1,2,1]


class Solution:
    #time O(N^2)
    # space (O(N))
    def findCapacity(self, arr):
        lvl = 0
        accum = 0

        wlvl = self.__sliceLvl(arr, lvl)
        while wlvl !=0 :
            #print (wlvl)
            accum = accum + wlvl
            lvl = lvl + 1
            wlvl = self.__sliceLvl(arr, lvl)
        return accum


    def __sliceLvl (self, arr, lvl):
        arrlvl = []
        for l in arr:
            arrlvl.append(max(0, l-lvl))

        #find water trapped
        cnt = False
        chkW = 0
        confirmedW = 0
        if arrlvl[0] > 0:
            cnt=True
        for i in range(1, len(arrlvl)):
            if cnt:
                if arrlvl[i] == 0:
                    chkW = chkW + 1
                else:
                    confirmedW = confirmedW + chkW
                    chkW = 0
            else:
                if arrlvl[i] >0:
                    cnt = True
        return confirmedW

def capacity(arr):
    solu = Solution()
    return solu.findCapacity(arr)

if __name__ == "__main__":
    print ( capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) )