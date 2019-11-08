
#Given a list of numbers, find if there exists a pythagorean triplet in that list.
# A pythagorean triplet is 3 variables a, b, c where a^2 + b^2 = c^2

#Example:
#Input: [3, 5, 12, 5, 13]
#Output: True


def findPythagoreanTriplets_nSquare(nums):
    mynums = nums
    mynums.sort(key=lambda v: v * v)

    for k in range(len(nums)-1, 1, -1):
        j = k - 1
        i = 0
        ref = mynums[k] * mynums[k]
        while i<j:

            v = (mynums[j])*(mynums[j]) + (mynums[i])*(mynums[i])
            if(v == ref):
                return True
            elif (v < ref):
                i = i + 1
            else:
                j = j - 1


    return False





#O[N^3]
def findPythagoreanTriplets_brutal(nums):
    mynums = nums
    mynums.sort(key = lambda v : v*v)

    for i in range(len(nums)-1, 1,-1 ):
        for j in range (0, i-1):
            for k in range(j+1, i ):
                v = (mynums[j])*(mynums[j]) + (mynums[k])*(mynums[k])
                if(v == mynums[i] * mynums[i] ):
                    return True

    return False



print (findPythagoreanTriplets_brutal(  [3,12,-5,13] ))

print (findPythagoreanTriplets_nSquare(  [3, 5, 12, 5, 13]))
# True