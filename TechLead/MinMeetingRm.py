# Find the minimum rm for meeting schedules
from __future__ import annotations
from typing import List
import heapq


class Session:
    def __init__(self, start: int, end: int):
        self.start: int = start
        self.end: int = end

    def __repr__(self) -> str:
        return f"({self.start}, {self.end})"


class MeetingRoom:
    def __init__(self):
        self.end: int = -1
        self.sessions: list[Session] = []

    def add(self, session: Session):
        self.sessions.append(session)
        self.end = max(self.end, session.end)

    def earliest_available(self) -> int:
        return self.end

    def __lt__(self, other: MeetingRoom):
        return self.end < other.earliest_available()

    def __repr__(self) -> str:
        res = ""
        for s in self.sessions:
            res = res + repr(s) + ","
        res += "\n"
        return res


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
                if numOfRm - occupied == 0:
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

    def findMinRoom3(self, meetingList):
        # ref: https://www.javatpoint.com/minimum-number-of-meeting-room-required-problem-in-java
        start = []
        end = []
        for m in meetingList:
            start.append(m[0])
            end.append(m[1])

        start.sort()
        end.sort()

        i: int = 1
        j: int = 0
        curr: int = 1
        answer: int = 1
        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                curr += 1
                i += 1
            else:
                curr -= 1
                j += 1

            answer = max(answer, curr)
            pass
        return answer

    def findMinRoom4(self, meetingList: list[tuple]):
        start = []
        end = []
        if len(meetingList) == 0:
            return 0

        for m in meetingList:
            start.append(m[0])
            end.append(m[1])

        start.sort()
        end.sort()

        priority_queue = []

        heapq.heappush(priority_queue, end[0])

        i: int = 1

        max_room: int = 1

        while i < len(start):
            earliest_available: int = priority_queue[0]
            if start[i] < earliest_available:
                # need new room
                max_room += 1
            else:
                # offload the old room
                heapq.heappop(priority_queue)
                pass
            pass
            heapq.heappush(priority_queue, end[i])
            i += 1

        assert (
            len(priority_queue) == max_room
        ), f"len of priority queue: {len(priority_queue)}"
        return max_room

    def findMinRoom5(self, meetingList: List[tuple]) -> list[MeetingRoom]:
        start = []
        end: list[Session] = []
        if len(meetingList) == 0:
            return 0, []
        for m in meetingList:
            start.append(m[0])
            end.append(Session(m[0], m[1]))
        start.sort()
        end.sort(key=lambda x: x.end)

        first_meeting_rm = MeetingRoom()
        first_meeting_rm.add(end[0])
        priority_queue: list[MeetingRoom] = [first_meeting_rm]
        for i in range(1, len(start)):
            earliest_available: MeetingRoom = priority_queue[0]
            if start[i] < earliest_available.end:
                # need new room
                new_room = MeetingRoom()
                new_room.add(end[i])
                heapq.heappush(priority_queue, new_room)
            else:
                # add session to the earliest available room
                rm_to_update = heapq.heappop(priority_queue)
                rm_to_update.add(end[i])
                heapq.heappush(priority_queue, rm_to_update)
            pass
        return priority_queue


def minRoom(meetingList: List[List[int]]) -> int:
    solu = Solution()
    return solu.findMinRoom5(meetingList)


if __name__ == "__main__":
    meetingList = [(15, 20), (0, 30), (5, 10), (17, 20)]
    # meetingList = [(6, 8), (1, 6)]
    meetingList = [(1, 18), (18, 23), (15, 29), (4, 15), (2, 11), (5, 13)]
    # meetingList = [(1, 18), (18, 23), (15, 29), (4, 15), (2, 11)]
    print(minRoom(meetingList))
