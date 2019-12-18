
#Find the minimum rm for meeting schedules
from typing import List

class Solution:

    def findMinRoom(self, meetingList):
        start = []
        end = []
        for m in meetingList:
            start.append(m[0])
            end.append(m[1])
        start.sort()
        end.sort()

        s = 0
        e = 0
        numOfRm = 0
        available = 0

        while s < len(start):
            if start[s] < end[e]:
                if available == 0:
                    numOfRm += 1
                    s += 1
                else:
                    available -= 1
                    s += 1
            else:
                available += 1
                e += 1

        return numOfRm

    def findMinRoom2(self, meetingList):
        start = []
        end = []
        for m in meetingList:
            start.append(m[0])
            end.append(m[1])
        start.sort()
        end.sort()

        s = 0
        e = 0
        numOfRm = 0
        occupied = 0

        while s < len(start):
            if start[s] < end[e]:
                if numOfRm-occupied == 0:
                    numOfRm += 1
                    occupied += 1
                    s += 1
                else:
                    occupied += 1
                    s += 1
            else:
                occupied -= 1
                e += 1

        return numOfRm

def minRoom(meetingList: List[List[int]] )->int:
    solu = Solution()
    return solu.findMinRoom2(meetingList)


if __name__ == "__main__":
    meetingList = [(15,20), (0,30), (5, 10), (17,20)]
    print (minRoom(meetingList))
