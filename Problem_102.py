# This problem was asked by Lyft.

# Given a list of integers and a number K, return which contiguous elements of the list sum to K.

# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

def find_continuous_k(list, k):
    previous = dict()
    sum = 0
    # sublist starting at the zeroth position work.
    previous[0] = -1
    for last_idx, item in enumerate(list):
        sum += item
        previous[sum] = last_idx
        first_idx = previous.get(sum - k)
        if first_idx is not None:
            return list[first_idx + 1:last_idx + 1]
    return None