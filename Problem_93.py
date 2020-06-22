# This problem was asked by Apple.

# Given a tree, find the largest tree/subtree that is a BST.

# Given a tree, return the size of the largest tree/subtree that is a BST.

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_bst(root):
    def is_bst_helper(root, min_key, max_key):
        if root is None:
            return True
        if root.key <= min_key or root.key >= max_key:
            return False
        return is_bst_helper(root.left, min_key, root.key) and \
               is_bst_helper(root.right, root.key, max_key)

    return is_bst_helper(root, float('-inf'), float('inf'))

def size(root):
    if root is None:
        return 0
    return size(root.left) + size(root.right) + 1

def largest_bst_subtree(root):
    max_size = 0
    max_root = None
    def helper(root):
        # Returns a tuple of (size, min_key, max_key) of the subtree.
        nonlocal max_size
        nonlocal max_root
        if root is None:
            return (0, float('inf'), float('-inf'))
        left = helper(root.left)
        right = helper(root.right)
        if root.key > left[2] and root.key < right[1]:
            size = left[0] + right[0] + 1
            if size > max_size:
                max_size = size
                max_root = root
            return (size, min(root.key, left[1]), max(root.key, right[2]))
        else:
            return (0, float('-inf'), float('inf'))

    helper(root)
    return max_root