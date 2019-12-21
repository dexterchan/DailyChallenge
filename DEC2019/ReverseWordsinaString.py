#Skill: array traversal, stack, state
#Level : too easy
#Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

#Example 1:
#Input: "The cat in the hat"
#Output: "ehT tac ni eht tah"
#Note: In the string, each word is separated by single space and there will not be any extra space in the string.

#Here's a starting point:
from enum import Enum
from typing import List

class STATE(Enum):
    NONE = 0
    WORD = 1
    NONWORD = 2

class Solution:
    def reverseWords(self, str):
        wordStack=[]
        state = STATE.NONE
        result=[]

        for c in str:
            state=self.__checkSTATE(c)
            if state == STATE.WORD:
                wordStack.append(c)
            elif state == STATE.NONWORD:
                newWord = self.__getPrevWord(wordStack)
                if len(newWord) > 0:
                    result.append(newWord)
                result.append(c)
        newWord = self.__getPrevWord(wordStack)
        if len(newWord) > 0:
            result.append(newWord)
        return "".join(result)
    def __checkSTATE(self, ch):
        n = ord(ch)
        if n>=ord('a') and n<=ord('z'):
            return STATE.WORD
        if n>=ord('A') and n<=ord('Z'):
            return STATE.WORD
        return STATE.NONWORD
    def __getPrevWord(self, wordStack):
        w = []
        for i in range(len(wordStack)):
            w.append( wordStack.pop())
        return "".join(w)


if __name__ == "__main__":
    print (Solution().reverseWords("The cat in the hat"))
    # ehT tac ni eht tah