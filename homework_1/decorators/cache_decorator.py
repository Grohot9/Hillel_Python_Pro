import functools


def lfu_cache(max_limit=64):
    """A decorator for caching with deleting elements by LFU algorithm after going beyond the limit"""

    def internal(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            new_cache_key = (args, tuple(kwargs.values()))
            for cache_key, cache_value in wrapper._cache.items():
                if new_cache_key == cache_key:
                    cache_data = cache_value[0]
                    count_of_calls = cache_value[1]
                    # changing the number of calls
                    cache_value = [cache_data, count_of_calls + 1]
                    wrapper._cache.update({cache_key: cache_value})
                    return cache_data
            cache_data = func(*args, **kwargs)
            if len(wrapper._cache) >= max_limit:
                for cache_key, cache_value in wrapper._cache.items():
                    # deleting data with the least number of calls
                    if cache_value[1] == wrapper.minimal_count_of_calls:
                        wrapper._cache.pop(cache_key)
                        break
            # adding new data in the cache
            wrapper._cache.update({new_cache_key: [cache_data, 1]})
            wrapper.minimal_count_of_calls = 1

        wrapper.minimal_count_of_calls = 1
        wrapper._cache = dict()
        return wrapper

    return internal
