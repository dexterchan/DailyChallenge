#SKill : array iteration
#A UTF-8 character encoding is a variable width character encoding
# that can vary from 1 to 4 bytes depending on the character. The structure of the encoding is as follows:
#1 byte:  0xxxxxxx
#2 bytes: 110xxxxx 10xxxxxx
#3 bytes: 1110xxxx 10xxxxxx 10xxxxxx
#4 bytes: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
#For more information, you can read up on the Wikipedia Page.

#Given a list of integers where each integer represents 1 byte, return whether or not the list of integers is a valid UTF-8 encoding.

#Analysis
# State machine
# check pattern in sequence
# from 4 byte to 1 byte pattern
# For first byte, XOR(first byte, 4 byte mask) = value....
# if value <= 1<<3, match, otherwise, not match and try 3 byte to 1 byte mask
# if it is N byte, check consecutive N-1 byte , if match XOR (byte, b10000000), if value < 1<<6, match... otherwise not match

BYTE_MASKS = [
    None,
    0b10000000,
    0b11100000,
    0b11110000,
    0b11111000,
]
BYTE_EQUAL = [
    None,
    0b00000000,
    0b11000000,
    0b11100000,
    0b11110000,
]

def utf8_validator(bytes):
    numOfBytes = 4
    cnt=0
    while cnt < len(bytes):
        while numOfBytes>0:
            value = bytes[cnt] & BYTE_MASKS[numOfBytes]
            if value == BYTE_EQUAL[numOfBytes]:
                break
            else:
                numOfBytes -= 1
        i = 0
        if numOfBytes < 1:
            return False
        if numOfBytes + cnt > len(bytes):
            return False
        cnt += 1

        while i < numOfBytes-1:
            value = bytes[cnt + i] ^ 0b10000000
            if value < 1<<6:
                i +=1
            else:
                return False
        cnt += (numOfBytes-1)
        numOfBytes = 4
    return True


if __name__ == "__main__":
    print(utf8_validator([0b11000000, 0b10000000, 0b00000000]))
    # True

    print(utf8_validator([0b11000000, 0b00000000]))
    # False

    print (utf8_validator([0b11000000, 0b10000000]))
    # True
    print (utf8_validator([0b00000000]))
    # True
    print (utf8_validator([0b00000000, 0b10000000]))
    # False



