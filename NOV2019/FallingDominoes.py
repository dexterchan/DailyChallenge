# Given a string with the initial condition of dominoes, where:

# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side

# Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends,
# the force cancels out and that domino remains upright.

# Example:
# Input:  ..R...L..R.
# Output: ..RR.LL..RR

class Solution(object):
    def pushDominoes(self, dominoes):
        cur = dominoes
        run = True

        while run:
            latest = cur
            plr = self.__placeHolderRight(latest)
            pll = self.__placeHolderLeft(latest)
            latest = self.__ziplr(plr, pll)
            if latest == cur:
                run = False
            else:
                cur = latest
        return cur

    def __ziplr(self, plr, pll):
        tmp = []
        for i in range (0, len(plr)):
            if(plr[i]=='R' and pll[i]=='L'):
                tmp.append(".")
            elif(plr[i] == 'R' and pll[i] == '.'):
                tmp.append("R")
            elif(plr[i] == '.' and pll[i] == 'L'):
                tmp.append("L")
            elif plr[i] == pll[i]:
                tmp.append(plr[i])
            else:
                raise Exception("Invalid state at %d R:%s L:%s"%(i,plr[i],pll[j]))
        return "".join(tmp)

    def __placeHolderRight(self, d):
        tmp = []
        prev = None
        for i in range (0,len(d)):
            if prev is None:
                prev = d[i]
                tmp.append(d[i])
                continue
            if prev == 'R' and d[i] == '.':
                prev = d[i]
                tmp.append('R')
            else:
                prev = d[i]
                tmp.append(d[i])
        return "".join(tmp)
    def __placeHolderLeft(self, d):
        tmp = []
        prev = None
        for i in range (len(d)-1, -1, -1):
            if prev is None:
                prev = d[i]
                tmp.append(d[i])
            if prev == 'L' and d[i] == '.':
                prev = d[i]
                tmp.append('L')
            else:
                prev = d[i]
                tmp.append(d[i])
        tmp.reverse()
        return "".join(tmp)

if __name__ == "__main__":
    print(Solution().pushDominoes('..R...L..R.'))
    # ..RR.LL..RR
