#You are given a positive integer N which represents the number of steps in a staircase.
#You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.
import queue

class Node:
    def __init__(self, val, prevStep):
        self.value = val
        if prevStep is not None:
            self.accum = self.value + prevStep.accum
        else:
            self.accum = 0
        self.prev = prevStep

def walk (nextStep, limit, walkQueue, successQueue):
    if nextStep.accum == limit:
        successQueue.append(nextStep)
    elif (nextStep.accum < limit):
        walkQueue.put(nextStep)

def nCk(n, k):
    numerator = 1
    denominator = 1

    if k==0 :
        return 1
    for num in range (n,n-k,-1):
        numerator = num * numerator
    for num in range (1, k+1):
        denominator = denominator * num
    return int(numerator/denominator)

def staircase(num):
    n = num
    k = 0
    accum = 0
    #analytic equation:
    # nC0 + n-1C1 + n-2C2 +...
    while n>=k:
        accum = accum + nCk (n-k, k)
        k = k +1

    return accum


def staircase_brutal_force(n):
    walkQueue = queue.Queue()
    successQueue = []
    walkQueue.put(Node(0, None))

    while not walkQueue.empty():
        step = walkQueue.get()

        walk(Node(1, step), n, walkQueue, successQueue)
        walk(Node(2, step), n, walkQueue, successQueue)

    #printSteps(successQueue)
    return len(successQueue)


def printSteps(successQueue):
    for steps in successQueue:
        while (steps.prev is not None):
            print (steps.value, end=',')
            steps = steps.prev
        print()

# Fill this in.
if __name__ == "__main__":
    print (staircase_brutal_force(4) )
    # 5
    print (staircase_brutal_force(5) )
    # 8

    print(staircase_brutal_force(10))
    # 8

    print(staircase(10))
    # 8