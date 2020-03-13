#Skill: Tries
#Difficulty : EASY
#Given a phone number, return all valid words that can be created using that phone number.

#For instance, given the phone number 364
#we can construct the words ['dog', 'fog'].

#Here's a starting point:

#Analysis
#If done by brutal force, time cost is exponent to find all possibilties
#To reduce to linear, we can use data structure Tries
#Create a Tries from valid words... using digit sequence.... time cost O[N] -> linear
#To search for word with number, it cost O[N]
#space complexity is Linear O(N)
from typing import List
lettersMaps = {
    1: [],
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z'],
    0: []
}

class Tries():
    def __init__(self, isWord=False):
        self.digits = [None]*10
        self.isWord = isWord
        self.bagOfWords = []

    def insertWord(self, word):
        self.isWord = True
        self.bagOfWords.append(word)
    def get(self, digit):
        return self.digits[digit]

    def assign(self, digit):
        self.digits[digit] = Tries()


validWords = ['dog', 'fish', 'cat', 'fog']

class PhoneNumbers():
    def __init__(self):
        self.tries = Tries()

    def constructTries(self, validWords:List[str]):
        for w in validWords:
            tries = self.tries
            cnt = 0
            maxLen = len(w)
            for ch in w:
                d = self.__mapChToNumber(ch)
                if d is None:
                    raise Exception("not found character to map digit:"+ch)
                if tries.get(d) is None:
                    tries.assign(d)
                tries = tries.get(d)
                cnt = cnt + 1
                if cnt == maxLen:
                    tries.insertWord(w)


    def __mapChToNumber(self, ch):
        for (d, l) in lettersMaps.items():
            if ch in l:
                return d
        return None

    def getWords(self, phoneNumbers:str):
        tries = self.tries
        result = []
        for d in phoneNumbers:
            tries = tries.get(int(d))
            if tries is None:
                return result
        result = tries.bagOfWords
        return result

phoneNumbers = PhoneNumbers()
phoneNumbers.constructTries(validWords)

def makeWords(phone):
    #Fill this in
    phoneNumbersRef = phoneNumbers
    return phoneNumbers.getWords(phone)


if __name__ == "__main__":
    print(makeWords('364'))
    # ['dog', 'fog']

    print(makeWords('3474'))