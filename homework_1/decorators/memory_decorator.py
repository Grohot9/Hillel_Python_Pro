import functools
import tracemalloc


def memory(func):
    """A decorator that measures how much a function occupies in the non-swapped physical memory"""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        func(*args, **kwargs)
        snapshot = tracemalloc.take_snapshot()
        tracemalloc.stop()
        stats = snapshot.statistics('traceback')[0]
        print("The function took up %.1f MB of the physical memory." % (stats.size / 1024 / 1024))

    return wrapper
