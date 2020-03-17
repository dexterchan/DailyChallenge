#Skill: regex
#Given a string that may represent a number, determine if it is a number. Here's some of examples of how the number may be presented:
#"123" # Integer
#"12.3" # Floating point
#"-123" # Negative numbers
#"-.3" # Negative floating point
#"1.5e5" # Scientific notation
#Here's some examples of what isn't a proper number:
#"12a" # No letters
#"1 2" # No space between numbers
#"1e1.2" # Exponent can only be an integer (positive or negative or 0)
#Scientific notation requires the first number to be less than 10,
# however to simplify the solution assume the first number can be greater than 10.
# Do not parse the string with int() or any other python functions.

#Here's some starting code:
#Analysis
import re


def __parseReg(s, p):

    matcher = re.compile(p)
    m = matcher.match(s)
    if m is None:
        return False
    else:
        #for g in range(len(m.groups())):
        #    print (m.group(g))
        return True



def parse_number(s):
    # Fill this in.
    p = r"^(-)?(\d)*(\.)?(\d)*$"
    chk = __parseReg(s, p)
    if not chk:
        p = r"^(-)?(\d)*(\.)?(\d)*e(\d)*$"
        chk = __parseReg(s,p)

    return chk

if __name__ == "__main__":
    print(parse_number("-12e2"))
    # True

    print(parse_number("-1.5.1e2"))
    # False

    print(parse_number("-1.5e1.55"))
    # False

    print(parse_number("-1.5e5"))
    # True

    print(parse_number("1e1.2"))
    # False

    print(parse_number("1 2"))
    # False

    print(parse_number("1.5e5"))
    # True

    print(parse_number("-.3"))
    # True

    print(parse_number("-123"))
    # True

    print(parse_number("12a"))
    # False

    print(parse_number("12.3"))
    # True

