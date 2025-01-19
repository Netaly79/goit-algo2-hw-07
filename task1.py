import random
from functools import lru_cache
import time


def range_sum_no_cache(array, L, R):
    return sum(array[L:R + 1])


def update_no_cache(array, index, value):
    array[index] = value


class SmartCachedRange:

    def __init__(self, array, cache_size=1000):
        self.array = array
        self.lru_cache_size = cache_size

    @lru_cache(maxsize=1000)
    def range_sum_with_cache(self, L, R):
        return sum(self.array[L:R + 1])

    def update_with_cache(self, index, value):
        self.array[index] = value
        self.range_sum_with_cache.cache_clear()


N = 100000
Q = 50000
random.seed(0)

array = [random.randint(1, 100) for _ in range(N)]
queries = []
for _ in range(Q):
    if random.choice(['Range', 'Update']) == 'Range':
        L = random.randint(0, N - 1)
        R = random.randint(L, N - 1)
        queries.append(('Range', L, R))
    else:
        index = random.randint(0, N - 1)
        value = random.randint(1, 100)
        queries.append(('Update', index, value))

start_time = time.time()
for query in queries:
    if query[0] == 'Range':
        _, L, R = query
        range_sum_no_cache(array, L, R)
    elif query[0] == 'Update':
        _, index, value = query
        update_no_cache(array, index, value)
end_time = time.time()
no_cache_time = end_time - start_time

cached_operations = SmartCachedRange(array)
start_time = time.time()
for query in queries:
    if query[0] == 'Range':
        _, L, R = query
        cached_operations.range_sum_with_cache(L, R)
    elif query[0] == 'Update':
        _, index, value = query
        cached_operations.update_with_cache(index, value)
end_time = time.time()
cache_time = end_time - start_time

# Results
print("Час виконання без кешування", no_cache_time, "секунд")
print("Час виконання з LRU-кешем:", cache_time, "секунд")
