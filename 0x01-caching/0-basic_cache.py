#!/usr/bin/env python3
"""Cache Class"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
  """Representation of a Cache System"""
  def put(self, key, item):
    """Add items to cache dictionary"""
    if key is not None or item is not None:
      self.cache_data[key] = item


  def get(self, key):
    """Retrieve items from cache dict"""
    if key is None or key not in self.cache_data:
      return None
    return self.cache_data.get(key)

