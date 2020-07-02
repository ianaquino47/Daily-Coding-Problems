# This problem was asked by Stripe.

# Write a map implementation with a get function that lets you retrieve the value of a key at a particular time.

# It should contain the following methods:

# set(key, value, time): sets key to value for t = time.
# get(key, time): gets the key at t = time.
# The map should work like this. If we set a key at a particular time, it will maintain that value forever or until it gets set at a later time. In other words, when we get a key at a time, it should return the value that was set for that key set at the most recent time.

# Consider the following examples:

# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 2) # set key 1 to value 2 at time 2
# d.get(1, 1) # get key 1 at time 1 should be 1
# d.get(1, 3) # get key 1 at time 3 should be 2
# d.set(1, 1, 5) # set key 1 to value 1 at time 5
# d.get(1, 0) # get key 1 at time 0 should be null
# d.get(1, 10) # get key 1 at time 10 should be 1
# d.set(1, 1, 0) # set key 1 to value 1 at time 0
# d.set(1, 2, 0) # set key 1 to value 2 at time 0
# d.get(1, 0) # get key 1 at time 0 should be 2

class TimeMap:
    def __init__(self):
        self.map = dict()
        self.sorted_keys_cache = None

    def get(self, key):
        value = self.map.get(key)
        if value is not None:
            return value
        if self.sorted_keys_cache is None:
            self.sorted_keys_cache = sorted(self.map.keys())
        i = bisect.bisect_left(self.sorted_keys_cache, key)
        if i == 0:
            return None
        else:
            return self.map.get(self.sorted_keys_cache[i - 1])

    def set(self, key, value):
        self.sorted_keys_cache = None
        self.map[key] = value