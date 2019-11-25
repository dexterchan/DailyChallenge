#Given a non-empty array of integers, return k most freq elements

#input nums = [1,1,1,2,2,3], k=2
#Output: [1,2]
import heapq

class Solution :
    def topKFrequest(self, nums, k):
        st = {}
        for n in nums:
            if n in st:
                st[n] = st[n] + 1
            else:
                st[n] = 1
        return heapq.nlargest(k, st, key=st.get)


if __name__ == "__main__":
    solu = Solution()
    l = solu.topKFrequest(nums=[1,1,1,2,2,3], k=2)
    print (l)