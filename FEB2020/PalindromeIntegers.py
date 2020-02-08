

#Given an integer, check if that integer is a palindrome. For this problem do not convert the integer to a string to check if it is a palindrome.

#Analysis
#find the max number of digit
#numOfDigits=floor(log10(number))
#Go into loop
#head , tail
#init: head=numOfDigits , tail = 0
#loop until head<=tail
# check if hd=trunc(n/10**head)%10 = td=trunc(n/10**tail)%10
# if yes, continue with head=head-1, tail=tail+1 else return false
# return true
#Time complexity O(N), space complexity O(1)


import math

def is_palindrome(n):
    # Fill this in.
    numOfDigits = math.floor(math.log(n)/math.log(10))
    head = numOfDigits
    tail = 0
    while head > tail:
        hd = math.trunc(n/(10**head))%10
        td = math.trunc(n/(10**tail))%10
        if hd == td:
            head -= 1
            tail += 1
            continue
        else:
            return False
    return True



if __name__ == "__main__":
    print(is_palindrome(1234322))
    # False

    print (is_palindrome(1234321))
    # True

    print (is_palindrome(12))
    # False

    print(is_palindrome(121))
    # True