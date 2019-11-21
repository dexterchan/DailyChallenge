# Skill: heap
#You are given a hash table where the key is a course code,
# and the value is a list of all the course codes that are prerequisites for the key.
# Return a valid ordering in which we can complete the courses. If no such ordering exists, return NULL.

#Example:
#{
#  'CSC300': ['CSC100', 'CSC200'],
#  'CSC200': ['CSC100'],
#  'CSC100': []
#}

#This input should return the order that we need to take these courses:
# ['CSC100', 'CSC200', 'CSCS300']
import heapq


class Solution_BrutalForce:
    def course_to_take (self, input):
        courseh = self.__constructHeap(input)
        courseSet = set()
        outputcourse = []

        while len(courseh):
            c = heapq.heappop(courseh)
            #Check the course dependency
            course = c[1][0]
            d = c[1][1]
            ok = self.__checkCourseDepedency(d, courseSet)
            if not ok:
                return None
            outputcourse.append(course)
            courseSet.add(course)
        return outputcourse

    def __checkCourseDepedency(self, d, courseSet):
        if len(d) == 0:
            return True
        for c in d:
            if c not in courseSet:
                return False
        return True

    def __constructHeap (self, input):
        h = []
        for key in input.keys():
            dlen = len(input[key])
            heapq.heappush(h, (dlen, (key, input[key])))
        return h


def courses_to_take(course_to_prereqs):
    solu = Solution_BrutalForce()
    return solu.course_to_take(course_to_prereqs)

if __name__ == "__main__":
    courses = {
      'CSC300': ['CSC100', 'CSC200'],
      'CSC200': ['CSC100'],
      'CSC100': []
    }
    print ( courses_to_take(courses) )

    courses = {
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100']
    }
    print(courses_to_take(courses))
    # ['CSC100', 'CSC200', 'CSC300']