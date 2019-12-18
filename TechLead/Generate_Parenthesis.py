
#Given n paris of paretheses, write a function to generate all combinations of well-formed parentheses

#For example, given n = 3, a solution set is

sample=[
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]
from typing import List


class JomaSolution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(S, left, right):
            if len(S) == 2*n:
                res.append(S)
                return
            if left < n:
                backtrack(S+'(', left + 1, right)
            if left > right:
                backtrack(S+')', left, right + 1)
        backtrack("", 0, 0)
        return res

class Solution:
    def generateParetheses(self, pairs):
        input = [ ("(", 1) ]
        maxLoop = pairs * 2
        output = self.__generateRescursive(1, maxLoop, input)

        result = []
        for grp in output:
            result.append(grp[0])

        return result

    def __generateRescursive(self, n, maxLoop, input ):
        output = []
        n += 1
        for grp in input:
            str = grp[0]
            cnt = grp[1]
            if n < maxLoop:
                newStr=""
                newStr = str + "("
                output.append((newStr, cnt+1))
                if cnt - 1 >= 0:
                    newStr = str + ")"
                    output.append((newStr, cnt-1))
            else:
                if cnt-1 == 0:
                    newStr = str + ")"
                    output.append((newStr, cnt - 1))
        if n < maxLoop:
            return self.__generateRescursive(n, maxLoop, output)
        else:
            return output

def generateParetheses(pairs):
    solu = Solution()
    return solu.generateParetheses(pairs)


if __name__ == "__main__":
    print (generateParetheses(4))
