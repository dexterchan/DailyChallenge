#Skill: regex, array iteration
#Given a string with a certain rule: k[string] should be expanded to string k times.
# So for example, 3[abc] should be expanded to abcabcabc.
# Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.

#Your starting point:

#Analysis
#search the first regex: '(\d+)\[', it will return match object
# if match object is not None, get span: (start, end), match group group(1) to read the number N
# else return the same string
# find the last ] in pos l <- iterate the string, start from 0, if find [, increment 1, if find ] , decrement 1, until reaching 0
# Cut the substring s[end: l] and recursive the same function again..
# duplicate N times from the sub-call output
import re
class Solution:
    def __init__(self):
        self.pattern = '(\\d+)\\['

    def decodeString(self, s):
        return self.__recurseDecode (s)

    def __recurseDecode(self, str):
        cpos = 0
        result = ""
        m = re.search(self.pattern, str[cpos:])
        if m is None:
            return str
        s = str
        while (m != None):
            (start, end) = m.span(0)
            N = int( m.group(1))
            cpos = self.__findclosing(s)
            substr = s[end:cpos]
            tmpresult = self.__recurseDecode(substr)
            result = result + s[0:start]
            for i in range(N):
                result = result + tmpresult
            s = s[cpos+1:]
            m = re.search(self.pattern, s)
            if m is None:
                result = result + s

        return result

    def __findclosing (self, s):
        cnt = 0
        l = len(s)
        for i in range(l):
            if s[i] == '[':
                cnt += 1
            elif s[i] == ']':
                cnt -= 1
                if cnt == 0:
                    return i

        raise Exception ("Not found proper closing")

def decodeString(s):
    # Fill this in.
    solu = Solution()
    return solu.decodeString(s)

if __name__ == "__main__":
    print (decodeString('2[a2[b]c]'))
    # abbcabbc

    print(decodeString('a2[a]2[b]'))

    print(decodeString('2[a2[b]c2[d]]'))