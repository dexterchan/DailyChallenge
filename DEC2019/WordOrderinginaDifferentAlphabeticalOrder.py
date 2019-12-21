#Skill: array traversal
#Given a list of words, and an arbitrary alphabetical order, verify that the words are in order of the alphabetical order.

#Example:
#Input:
#words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

#Output: False
#Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

#Example 2:
#Input:
#words = ["zyx", "zyxw", "zyxwy"],
#order="zyxwvutsrqponmlkjihgfedcba"

#Output: True
#Explanation: The words are in increasing alphabetical order

#Here's a starting point:

class Solution():
    def isSorted(self, words, order):
        ordering = self.__parseOrder(order)
        for i in range(len(words)-1):
            if self.__compare(ordering, words[i], words[i+1])>0:
                return False
        return True


    def __parseOrder(self, order):
        orderArray = [0] * 26
        cnt = 0
        for c in order:
            inx = self.__address(c)
            orderArray[inx] = cnt
            cnt += 1
        return orderArray

    def __address(self, ch):
        return ord(ch) - ord('a')

    def __compare(self, order, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        l = min(l1, l2)
        for i in range(l):
            o1 = order[self.__address(word1[i])]
            o2 = order[self.__address(word2[i])]
            if o1!=o2:
                return o1-o2
        return l1-l2


def isSorted(words, order):
    return Solution().isSorted(words, order)

if __name__ == "__main__":
    print ( isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba") )
    # False
    print ( isSorted(["zyx", "zyxw", "zyxwy"],
                   "zyxwvutsrqponmlkjihgfedcba") )
    # True
