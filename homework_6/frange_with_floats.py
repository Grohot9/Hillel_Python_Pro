class frange:
    def __init__(self, start, stop=None, step=None):
        self._start = start if stop is not None else 0
        self._stop = stop if stop is not None else start
        self._step = step if step is not None else 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._start > self._stop and self._step < 0 or self._start < self._stop and self._step > 0:
            result = self._start
            self._start += self._step
            return result
        else:
            raise StopIteration("Limit is exceeded")


# Tests:
# assert(list(frange(5)) == [0, 1, 2, 3, 4])
# assert(list(frange(2, 5)) == [2, 3, 4])
# assert(list(frange(2, 10, 2)) == [2, 4, 6, 8])
# assert(list(frange(10, 2, -2)) == [10, 8, 6, 4])
# assert(list(frange(2, 5.5, 1.5)) == [2, 3.5, 5])
# assert(list(frange(1, 5)) == [1, 2, 3, 4])
# assert(list(frange(0, 5)) == [0, 1, 2, 3, 4])
# assert(list(frange(0, 0)) == [])
# assert(list(frange(100, 0)) == [])
#
# print('SUCCESS!')
