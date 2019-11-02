
class ReverseString :

    def recursive(self, s):
        l = len(s)
        if( l<=1):
            return s
        else:
            return s[l-1]+self.recursive(s[:l-1])

    def iterative (self,s):
        newS = ""
        for inx in range(len(s)-1, -1, -1):
            newS=newS+(s[inx])
        return newS

if __name__ == "__main__":
    Solution = ReverseString()
    result = Solution.recursive("abcd")
    print (result)
    result = Solution.iterative("abcd")
    print(result)