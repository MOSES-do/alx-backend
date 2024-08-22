#!/usr/bin/python3
""" LIFO Caching System"""

from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Object that stores and retrieves items from
       a dictionary utilizing the FIFO removal mechanism
       when the cache storage limit is reached.
    """
    def __init__(self):
        """initialize derived class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item to cache"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item based on its key."""
        return self.cache_data.get(key, None)
