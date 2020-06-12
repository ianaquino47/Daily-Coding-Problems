# This question was asked by Google.

# Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

from random import randrange

def process_list(n, l):
    all_nums_set = set()
    for i in range(n):
        all_nums_set.add(i)

    l_set = set(l)
    nums_set = all_nums_set - l_set
    return list(nums_set)

def random_number_excluing_list(n, l):
    nums_list = process_list(n, l)
    idx = randrange(0, len(nums_list))
    return nums_list[idx]

print(random_number_excluing_list(4, [1, 2, 5]))