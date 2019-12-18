
#You are given a string of parenthesis. Return the minimum number of parenthesis that would need to be removed in order to make the string valid. "Valid" means that each open parenthesis has a matching closed parenthesis.

#Example:

#"()())()"

#The following input should return 1.

#")("

#Here's a start:

#Inspired by Joma strategy on "Generate_Parethsis"


class Solution:
    def count_invalid_parenthesis(self, str):
        l = len(str)
        nInvalid = 0
        i = 0

        invalidPos = []
        chkSum = 0
        while i < l:
            if str[i] == '(':
                chkSum += 1
            elif str[i] == ')':
                chkSum -= 1
            if chkSum < 0:
                nInvalid += 1
                invalidPos.append(i)
                chkSum = 0
            i += 1

        nInvalid += chkSum
        return nInvalid, invalidPos

def count_invalid_parenthesis(string):
    solu = Solution()

    num, invalidPos = solu.count_invalid_parenthesis(string)
    return num


if __name__ == "__main__":
    print (count_invalid_parenthesis("()())()"))
    # 1

    print(count_invalid_parenthesis("()"))
    # 0

    print(count_invalid_parenthesis("((()())()"))
    # 1