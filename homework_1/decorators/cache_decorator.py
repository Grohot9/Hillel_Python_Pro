import functools


def lfu_cache(max_limit=64):
    """A decorator for caching with deleting elements by LFU algorithm after going beyond the limit"""

    def internal(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = (args, tuple(kwargs.values()))
            if cache_key in wrapper._cache_keys:
                # changing the count of calls
                wrapper._counts_of_calls[wrapper._cache_keys.index(cache_key)] += 1
                return wrapper._cache[cache_key]
            cache_data = func(*args, **kwargs)
            if len(wrapper._cache) >= max_limit:
                index_for_del = wrapper._counts_of_calls.index(min(wrapper._counts_of_calls))
                # deleting data with the least count of calls
                wrapper._cache.pop(wrapper._cache_keys[index_for_del])
                wrapper._cache_keys.pop(index_for_del)
                wrapper._counts_of_calls.pop(index_for_del)
            # adding new data in the cache
            wrapper._cache.update({cache_key: cache_data})
            wrapper._cache_keys.append(cache_key)
            wrapper._counts_of_calls.append(1)

        wrapper._cache = dict()
        wrapper._cache_keys = list()
        wrapper._counts_of_calls = list()
        return wrapper

    return internal
