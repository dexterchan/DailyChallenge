
#Given a list of numbers of size n, where n is greater than 3,
# find the maximum and minimum of the list using less than 2 * (n - 1) comparisons.

#Here's a start:

#Analysis
#Exploit the property of N>3
#for first 3 element, we can do 3-4 comparison to find the max and min numbers:
# A compare to B.... if A is larger,
# then we have two cases:
# Case 1:
# if B compare to C , if B is larger, stop comparison. we end up with 3 comparison max A, min C
# if B is smaller, C compare with A to find larger number. we end up with 4 comparison min B, max A or C
# We extend this comparison by N-1 times, starting from first element
# beginning, we compare 1st and 2nd element to find max value and min value
# then, we compare 3rd element
# 1) if 3rd element > max, we update max value and iterate to 4th element
# 2) if 3rd element < max, we compare 3rd element with min value to update min value before iterate to 4th element
# For N element
# IN general,
# In best case, if all element in ascending order, it takes, n-1 comparisons
# in worst case, if all element in decending order, it takes 1 + 2(N-2) = 2N-3 comparison.... still 1 less than 2*(n-1)

def find_min_max(nums):
    # Fill this in.
    min=0
    max=0
    l = len(nums)
    if nums[0] > nums[1]:
        max, min = nums[0], nums[1]
    else:
        max, min = nums[1], nums[0]
    for inx in range(2, l):
        if nums[inx] > max:
            max = nums[inx]
        elif nums[inx] < min:
            min = nums[inx]

    return (min, max)

if __name__ == "__main__":
    print (find_min_max([3, 5, 1, 2, 4, 8]))
    # (1, 8)