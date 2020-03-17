
#Given an array and an integer k, rotate the array by k spaces. Do this without generating a new array and without using extra space.

#Here's an example and some starter code

def rotate_list(nums, k):
    # Fill this in.
    l = len(nums)
    m = k%l
    for i in range(m):
        firstNum = nums[0]
        for j in range(0, l-1):
            nums[j] = nums[j+1]
        nums[l-1] = firstNum
    return nums


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    rotate_list(a, 2)
    print(a)
    # [3, 4, 5, 1, 2]

    a = [1, 2, 3, 4, 5]
    rotate_list(a, 6)
    print(a)