#Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.

#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#- Open brackets are closed by the same type of brackets.
#- Open brackets are closed in the correct order.
#- Note that an empty string is also considered valid.

#Example:
#Input: "((()))"
#Output: True
#Input: "[()]{}"
#Output: True
#Input: "({[)]"
#Output: False

class Solution:

    def closePara (self, s):
        if( s == '('):
            return (')', False)
        elif (s == '{'):
            return ('}', False)
        elif (s == '['):
            return (']', False)
        else:
            return (s, True)


    def appendStack (self, c,  paraStack):
        paraStack.append(c)


    def isValid(self, s):
        # Fill this in.

        paraStack=[]
        lastPara=''
        for ch in s:
            if(lastPara == ''):
                lastPara = ch
                paraStack.append(ch)
                continue
            nextPara, isclosed = self.closePara(ch)
            if isclosed:
                #pop stack
                if(len(paraStack) <= 0):
                    return False
                expectPara,isclosed = self.closePara(paraStack[-1:][0])
                if(expectPara != ch):
                    return False
                else:
                    paraStack.pop()
            else:
                #put stack
                paraStack.append(ch)

        if(len(paraStack) != 0 ):
            return False
        else:
            return True


if __name__ == "__main__":
    # Test Programs
    s = "()(){(())"
    # should return False
    print(Solution().isValid(s))

    s = ""
    # should return True
    print(Solution().isValid(s))

    s = "([{}])()"
    # should return True
    print(Solution().isValid(s))


    s = "([{}])())"
    # should return True
    print(Solution().isValid(s))

    s = "([{}])("
    # should return True
    print(Solution().isValid(s))