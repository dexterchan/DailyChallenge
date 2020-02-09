#Skill: iteration
# Difficulty : Medium
#Given two strings, determine the edit distance between them.
# The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution)
# needed to change one string to the other.

#For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).

#Analysis
# Strategy:
# Find the longest substring matching between s1, s2, say s1[a1,b1], s2[a2,b2]
# Rest of substring pair, put into process stack (s1[0:a1],s2[0:a2]), (s1[b1:len(s1)], s2[b2:len(s2)])
# pop a element from process stack
# if string pair, all matching, dist=0
# if string pair not found matching substring(sub), distance=longest(substring), add to variable
# if one side of string is None (insert/delete), distance=longest(substring), add to variable
# until process stack empty
# Time cost O(N) space cost O(N)
# How to find longest matching substring? O(N^3)
# scanning between s1, s2
# suppose s1 is shorter
# variable : h1, t1, h2,t2, maxlen
#  s1, h1=t1=0, iterate h2=0
# if s1[h1]=s2[h2] , t1=h1+1,t2=h2+1, iterate t1,t2, until s1[t1]!=s2[t2]... if s1[t1]!=s2[t2] , l=t1-h1, h1=t1,h2=t2, check if l is max, if yes, register h1,t1,h2,t2
# else h2+=1
# the most cost is on find longest matching substring:
# Time cost O(N^3) , space cost O(N)

class Solution():
    def distance(self, s1, s2):
        s = []
        element = (s1, s2)
        s.append(element)
        distance = 0
        while len(s) > 0:
            e0, e1 = s.pop()
            minL = min(len(e0), len(e1))
            if e0 == e1:
                continue
            if minL == 0:
                distance += max(len(e0), len(e1))
                continue
            substr, (mh1,mt1,mh2,mt2) = self.__longestSubStr(e0, e1)
            lSubstr = len(substr)
            if lSubstr == 0:
                distance += max(len(e0), len(e1))
                continue

            s.append((e0[0:max(0, mh1)], e1[0:max(0,mh2)]))
            s.append((e0[min(len(e0),mt1):len(e0)], e1[min(len(e1),mt2):len(e1)]))
        return distance

    def __longestSubStr(self, s1, s2):
        if len(s1) < len(s2):
            (mh1,mt1,mh2,mt2) = self.__longestSubStrHelper(s1, s2)
        else:
            (mh2,mt2, mh1,mt1) = self.__longestSubStrHelper(s2, s1)
        return s1[mh1:mt1], (mh1,mt1,mh2,mt2)

    def __longestSubStrHelper(self, s1, s2):
        (h1, t1, h2, t2) = (0,0,0,0)
        maxLen = 0
        (mh1,mt1,mh2,mt2) = (0,0,0,0)
        msub1=None
        msub2=None


        while h1 < len(s1):
            h2=0
            while h1 < len(s1) and h2 < len(s2):
                t1 = h1 + 1
                t2 = h2 + 1
                while s1[h1:t1] == s2[h2:t2] and t1<=len(s1) and t2<=len(s2):
                    msub1 = s1[h1:t1]
                    msub2 = s2[h2:t2]
                    t1, t2 = t1+1, t2+1
                t1, t2 = t1-1, t2-1
                if t1-h1 > maxLen:
                    maxLen = t1-h1
                    (mh1, mt1, mh2, mt2) = (h1,t1,h2,t2)
                    msub1 = s1[h1:t1]
                    msub2 = s2[h2:t2]
                    h2 = max(t2, h2+1)
                else:
                    h2 = max(t2, h2+1)
            h1 += 1
        return (mh1,mt1,mh2,mt2)

def distance(s1, s2):
    solu = Solution()
    return solu.distance(s1, s2)


if __name__ == "__main__":
    print(distance('alert', 'let'))
    # 3

    print (distance('biting', 'sitting'))
    # 2

