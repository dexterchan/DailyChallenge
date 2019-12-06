#skills: array iteration
#A look-and-say sequence is defined as the integer sequence
# beginning with a single digit in which the next term is obtained
# by describing the previous term. An example is easier to understand:

#Each consecutive value describes the prior value.

#1      #
#11     # one 1's
#21     # two 1's
#1211   # one 2, and one 1.
#111221 # #one 1, one 2, and two 1's.

#Your task is, return the nth term of this sequence.

def findnTermOfSeq(seq, k):
    if len(seq)<2*k:
        return ""
    substr = seq[2*(k-1):2*k]
    num = int(substr[0])
    digit = substr[1]
    nums = ""
    if num==0:
        nums = "zero"
    elif num==1:
        nums = "one"
    elif num==2:
        nums = "two"
    elif num==3:
        nums = "three"
    elif num==4:
        nums = "four"
    elif num==5:
        nums = "five"
    elif num==6:
        nums = "six"
    elif num==7:
        nums = "seven"
    elif num==8:
        nums = "eight"
    elif num==9:
        nums = "nine"

    return "%s %s"%(nums, digit)

if __name__ == "__main__":
    print( findnTermOfSeq('1',1))      #
    print( findnTermOfSeq('11',1))     # one 1's
    print( findnTermOfSeq('21',1))     # two 1's
    print( findnTermOfSeq('1211',2))   # one 2, and one 1.
    print( findnTermOfSeq('111221',3)) # #one 1, one 2, and two 1's.