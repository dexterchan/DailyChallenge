#Given a list of possible coins in cents, and an amount (in cents) n,
# return the minimum number of coins needed to create the amount n.
# If it is not possible to create the amount using the given coin denomination, return None.

#Here's an example and some starter code:
#ANalysis, sort the list of possible coins O(nlogn) from largest to smallest
#for each cent,
#divide amount by cent value = d, if d >= 1
# amt = amt - d*cent value
# store cent value to list
# iterate for next cent
# at end of list
# if amt > 0 , return None

def make_change(coins, n):
    # Fill this in.
    lst = []
    coinsLst = sorted(coins, reverse=True)
    amt = n
    for c in coinsLst:
        d = amt // c
        amt = amt - d * c
        for i in range(d):
            lst.append(str(c))

    if amt > 0:
        return None
    else:
        result = "%d coins (%s)"%(len(lst), "+".join((lst)))
    return result

if __name__ == "__main__":
    print(make_change([1, 5, 10, 25], 36))
    # 3 coins (25 + 10 + 1)

    print(make_change([1, 5, 10, 25], 30))
    # 2 coins (25 + 5)

    print(make_change([1, 5, 10, 25], 27))
    # 2 coins (25 + 1 + 1)