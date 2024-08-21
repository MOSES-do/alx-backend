#!/usr/bin/python3
""" FIFO Caching System"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """initialize derived class"""
        super().__init__()

    def delete_by_index(self, cache_dict, index):
        """Delete a key-value pair from the dictionary by index"""
        keys = list(cache_dict.keys())   # keys converted to a list
        if 0 <= index < len(keys):   # checks if index is valid:
            key_to_del = keys[index]   # Grab the key at index of list
            del cache_dict[key_to_del]
            return key_to_del

    def put(self, key, item):
        """Add items to cache"""
        if key is not None and item is not None:
            """if dict is larger than MAX value of cache system
               delete first key-value pair
            """
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                deleted_key = self.delete_by_index(self.cache_data, 0)
                print("DISCARD:", deleted_key)

    def get(self, key):
        """Retrieves an item based on the key"""
        return self.cache_data.get(key, None)
