
#You are given an array. Each element represents the price of a stock on that particular day. Calculate and return the maximum profit you can make from buying and selling that stock only once.

#For example: [9, 11, 8, 5, 7, 10]


#Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).

#Here's your starting point:

class BuylowSellHigh:

    def buy_and_sell(self, arr):
        low, high =   self.__findlowHighDynamic(arr)
        return high - low

    #Cost: O(n)
    def __findlowHighDynamic(self, arr):
        maxdiff = -2 ** 31
        low = 0
        l = len(arr)

        bl = 0
        bh = 0

        for i in range (1, l):
            pnl = arr[i]-arr[low]
            if pnl > maxdiff:
                maxdiff = pnl
                bl = low
                bh = i

            if arr[i] < arr[low]:
                low = i

        return arr[bl], arr[bh]


    #Cost O(n^2)
    def __findLowHighBrutalForce(self, arr):
        maxdiff = -2**31
        l = len(arr)
        high=0
        low = 0
        for i in range (l-1):
            for j in range (i+1, l):
                if arr[j] - arr[i] > maxdiff:
                    maxdiff = arr[j] - arr[i]
                    high = arr[j]
                    low = arr[i]
        return low, high



def buy_and_sell(arr):
    solu = BuylowSellHigh()
    return solu.buy_and_sell(arr)

if __name__ == "__main__":
    print ( buy_and_sell([9, 11, 8, 5, 7, 10]) )
# 5