#Skill: hash set
#Given [4, 7, 1 , -3, 2] and k = 5,
#return true since 4 + 1 = 5.


def two_sum_HashSet(list, k):

    memory = set()

    for i in  (list):
        if(i in memory ):
            return True
        wantedNum = k - i
        memory.add(wantedNum)
    return False

#O(N)
def two_sum (list, k):
    m_size = 1<<16
    offset = m_size>>1
    memory = [False] * (m_size)

    for i in  (list):
        if(memory[i + offset] ):
            return True
        wantedNum = k - i
        memory[wantedNum + offset] = True
    return False

#Brutal force O(N^2)
def two_sum_brutalForce(list, k):
    size = len(list)
    for i in range(size):
        for j in range(i+1):
            if(i != j):
                sum = list[i] + list[j]
                if(sum == k):
                    return True;
    return False



if __name__ == "__main__":
    print (two_sum([4,7,1,-3,2], 5) )
    print(two_sum([4, 7, 1, -3, 2], 10))
    print(two_sum([4, 7, 2, -3, 2], 4))

    print(two_sum_HashSet([4, 7, 1, -3, 2], 5))
# True

#Try to do it in a single pass of the list.