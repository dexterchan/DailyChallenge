#Skill: bitwise operation
#Given a 32-bit integer, swap the 1st and 2nd bit, 3rd and 4th bit, up til the 31st and 32nd bit.

#Here's some starting code and an example:

class Solution():

    def __createFilter(self, base, numDigit):
        filter = 0
        for i in range(int(numDigit/2)):
            filter = filter << 2
            filter = filter | base
        return filter

    def swap_bits(self, num):
        numDigit = 32
        oddFilter = self.__createFilter(int("10",2), numDigit)
        evenFilter = self.__createFilter(int("01",2), numDigit)
        #print (f"{oddFilter:032b}")
        #print(f"{evenFilter:032b}")
        oddValues = num & oddFilter
        evenValues = num & evenFilter
        oddValues = oddValues >> 1
        evenValues = evenValues << 1
        return oddValues | evenValues



def swap_bits(num):
    solu = Solution()
    return solu.swap_bits(num)

if __name__ == "__main__":
    print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
    # 0b01010101010101010101010101010101

    print(f"0b{swap_bits(0b110101):032b}")
