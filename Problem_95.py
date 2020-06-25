# This problem was asked by Palantir.

# Given a number represented by a list of digits, find the next greater permutation of a number, in terms of lexicographic ordering. If there is not greater permutation possible, return the permutation with the lowest value/ordering.

# For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2] should return [2,1,3]. The list [3,2,1] should return [1,2,3].

# Can you perform the operation without allocating extra memory (disregarding the input memory)?

def nextPermutation(self, nums):
    def swap(nums, a, b):
        # Perform an in-place swap
        nums[a], nums[b] = nums[b], nums[a]

    def reverse(nums, a, b):
        # Reverses elements at index a to b (inclusive) in-place
        nums[a:b+1] = reversed(nums[a:b+1])

    # Find first index where nums[idx] < nums[idx + 1]
    pivot = len(nums) - 2
    while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
        pivot -= 1

    if pivot >= 0:
        # Find the next-largest number to swap with
        successor = len(nums) - 1
        while (successor > 0 and nums[successor] <= nums[pivot]):
            successor -= 1
        swap(nums, pivot, successor)

    reverse(nums, pivot + 1, len(nums) - 1)