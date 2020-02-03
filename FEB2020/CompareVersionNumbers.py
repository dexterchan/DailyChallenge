#Skill: regex
#Version numbers are strings that are used to identify unique states of software products. A version number is in the format a.b.c.d. and so on where a, b, etc. are numeric strings separated by dots. These generally represent a hierarchy from major to minor changes. Given two version numbers version1 and version2, conclude which is the latest version number. Your code should do the following:
#If version1 > version2 return 1.
#If version1 < version2 return -1.
#Otherwise return 0.

#Note that the numeric strings such as a, b, c, d, etc. may have leading zeroes,
#and that the version strings do not start or end with dots. Unspecified level revision numbers default to 0.

#Example:
#Input:
#version1 = "1.0.33"
#version2 = "1.0.27"
#Output: 1
#version1 > version2

#Input:
#version1 = "0.1"
#version2 = "1.1"
#Output: -1
#version1 < version2

#Input:
#version1 = "1.01"
#version2 = "1.001"
#Output: 0
#ignore leading zeroes, 01 and 001 represent the same number.

#Input:
#version1 = "1.0"
#version2 = "1.0.0"
#Output: 0
#version1 does not have a 3rd level revision number, which
#defaults to "0"
#Here's a starting point

#Analysis
# Suppose there is a way to parse the version number into list
# we compare the 2 list (version number) element by element iteration
# if left reach the end first, assign left = 0
# if right reach the end first, assign right = 0
# for each element,
# if left > right , return 1
# if right > left, return -1
# if left = right, keep going until both reach the end

# How to parse version number to list?
# using regex (\d+) to catch the first number in version string, append to list
# (start, end) = m.span(0)
# For the rest, run into loop for substring version[end:]:
# look for regex(\.(\d+)) to catch N number and append into list
# (start, end) = m.span(0)
# update next search number version[end:]
import re

class Solution:
    def compareVersion(self, version1, version2):
        # Fill this in.
        version1Lst = self.__convertVersion2List(version1)
        version2Lst = self.__convertVersion2List(version2)

        digit1 = 0
        digit2 = 0
        inx1 = 0
        inx2 = 0

        while (inx1 < len(version1Lst)) or (inx2 < len(version2Lst)):
            if inx1 < len(version1Lst):
                digit1 = version1Lst[inx1]
            else:
                digit1 = 0
            if inx2 < len(version2Lst):
                digit2 = version2Lst[inx2]
            else:
                digit2 = 0

            if digit1 == digit2:
                inx1 += 1
                inx2 += 1
            elif digit1 < digit2:
                return -1
            else:
                return 1
        return 0
    def __convertVersion2List(self, version):
        firstD = r"(\d+)"
        nD = r"\.(\d+)"
        result = []
        m = re.search(firstD, version)
        if m is None:
            return result
        (start, end) = m.span(0)
        result.append(int(m.group(1)))
        subVersion = version[end:]
        while True:
            m = re.search(nD, subVersion)
            if m is None:
                break
            (start, end) = m.span(0)
            result.append(int(m.group(1)))
            subVersion = subVersion[end:]

        return result


if __name__ == "__main__":
    version1 = "01.00000.001"
    version2 = "1"
    print(Solution().compareVersion(version1, version2))
    # 1

    version1 = "1.0.0"
    version2 = "1"
    print(Solution().compareVersion(version1, version2))

    version1 = "01.00000.001"
    version2 = "1.000001"
    print(Solution().compareVersion(version1, version2))
    # -1