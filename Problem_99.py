# This problem was asked by Microsoft.

# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# For example, given [100, 4, 200, 1, 3, 2], the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.

def longest_consecutive(self, nums):
    max_len = 0
    bounds = dict()
    for num in nums:
        if num in bounds:
            continue
        left_bound, right_bound = num, num
        if num - 1 in bounds:
            left_bound = bounds[num - 1][0]
        if num + 1 in bounds:
            right_bound = bounds[num + 1][1]
        bounds[num] = left_bound, right_bound
        bounds[left_bound] = left_bound, right_bound
        bounds[right_bound] = left_bound, right_bound
        max_len = max(right_bound - left_bound + 1, max_len)

    return max_len