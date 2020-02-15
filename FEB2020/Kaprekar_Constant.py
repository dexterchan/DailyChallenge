
#Kaprekar's Constant is the number 6174. This number is special because it has the property where for any 4-digit number that has 2 or more unique digits, if you repeatedly apply a certain function it always reaches the number 6174.

#This certain function is as follows:
#- Order the number in ascending form and descending form to create 2 numbers.
#- Pad the descending number with zeros until it is 4 digits in length.
#- Subtract the ascending number from the descending number.
#- Repeat.

#Given a number n, find the number of times the function needs to be applied to reach Kaprekar's constant. Here's some starter code:



KAPREKAR_CONSTANT = 6174

class Solution():
    def num_kaprekar_iterations(self, n):
        cnt = 0
        r = n
        while r != KAPREKAR_CONSTANT:
            r = self.__kaprekar(r)
            cnt += 1
        return cnt

    def __kaprekar(self, n):
        numLst = []
        num = n
        while num > 0 and len(numLst) < 4:
            numLst.append(num % 10)
            num = num // 10
        numLst.sort()
        bigNum=0
        smallNum = 0
        for i in range(len(numLst)):
            bigNum = bigNum*10 + numLst[len(numLst) - i - 1]
            smallNum = smallNum * 10 + numLst[i]
        for i in range(4 - len(numLst)):
            bigNum = bigNum * 10
        return bigNum - smallNum


def num_kaprekar_iterations(n):
    # Fill this in.
    solu = Solution()
    return solu.num_kaprekar_iterations(n)


if __name__ == "__main__":
    print (num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)
    print(num_kaprekar_iterations(4560))