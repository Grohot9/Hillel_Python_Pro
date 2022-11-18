import functools
import psutil


def memory(func):
    """A decorator that measures how much a function occupies in the non-swapped physical memory"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        process = psutil.Process()
        memory_usage_before = process.memory_info().rss
        result = func(*args, **kwargs)
        memory_usage_after = process.memory_info().rss
        print(f"The function took up {memory_usage_after - memory_usage_before} Byte of the physical memory.")
        return result

    return wrapper
