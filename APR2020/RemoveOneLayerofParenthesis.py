
#Given a valid parenthesis string (with only '(' and ')', an open parenthesis will always end with a close parenthesis, and a close parenthesis will never start first), remove the outermost layers of the parenthesis string and return the new parenthesis string.

#If the string has multiple outer layer parenthesis (ie (())()), remove all outer layers and construct the new string. So in the example, the string can be broken down into (()) + (). By removing both components outer layer we are left with () + '' which is simply (), thus the answer for that input would be ().

#Here are some examples and some starter code.

#Analysis
#Data structure P {"open":inx, "close":inx}
#label number of parenthesis similar to missing parenthesis with stack
#each number represents level
#segment index by level above with open closing
#put segment into a MAP {level: list of P}
#iterate each level from 1 to N
#if one of the P element having close-open=1, stop.... get the answer
from typing import List
from collections import defaultdict

class Level():
    def __init__(self, level: int, open:int, close:int=-1):
        self.level = level
        self.open = open
        self.close = close
    def __str__(self):
        return f"{self.level},{self.open},{self.close}"

class Solution():
    def remove_outermost_parenthesis(self, s:str):
        res = None
        labels = self.__labelLevel(s)

        segments = defaultdict(list)
        for label in labels:
            segments[label.level].append(label)

        maxLevels = len(segments)
        for l in range(1,maxLevels+1):
            segmentLst = segments[l]
            dump = False
            for label in segmentLst:
                if label.close-label.open == 1:
                    dump=True
                    break
            if dump:
                newres = self.__dumpResult(s, segmentLst)
                if res is None:
                    res = newres
                break
            else:
                res = self.__dumpResult(s, segmentLst)

        return res

    def __dumpResult(self, s:str, segmentLst:List[Level])->str:
        res = []
        for label in segmentLst:
            if label.close - label.open == 1:
                res.append("")
            else:
                res.append(s[label.open+1:label.close])
        return "".join(res)


    def __labelLevel(self, s:str)->List[Level]:
        res = []
        stack = []
        lvl = 0
        inx = 0
        for ch in s:
            if ch == '(':
                lvl += 1
                p = Level(lvl, inx)
                stack.append(p)
            elif ch == ')':
                p = stack.pop()
                assert (p.level == lvl)
                p.close = inx
                res.append(p)
                lvl -= 1
            inx += 1
        return res





def remove_outermost_parenthesis(s):
    # Fill this in.
    solu = Solution()
    return solu.remove_outermost_parenthesis(s)


if __name__ == "__main__":
    print(remove_outermost_parenthesis('(()())'))
    # ()()

    print(remove_outermost_parenthesis('(())()'))
    # ()



    print(remove_outermost_parenthesis('()()()'))
    # ' '
