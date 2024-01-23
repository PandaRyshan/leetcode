import os
import pickle

from functools import cache
from time import time


def cached(func):
    def wrapper(*args, **kwargs):
        cache_file = f"{func.__name__}.cache"
        if os.path.exists(cache_file):
            with open(cache_file, "rb") as f:
                return pickle.load(f)
        result = func(*args, **kwargs)
        with open(cache_file, "wb") as f:
            pickle.dump(result, f)
        return result
    return wrapper


def fib_recursive(n):
    if n < 2:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


@cache
def fib_recursive_cache(n):
    if n < 2:
        return n
    return fib_recursive_cache(n - 1) + fib_recursive_cache(n - 2)


@cached
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


n = 40


# start_time = time()
# fib_recursive(n)
# 
# print(f"Time taken by fib_recursive({n}): {time() - start_time:.4f} seconds")

start_time = time()
fib_recursive_cache(n)
print(f"Time taken by fib_recursive_cache({n}): {time() - start_time:.4f} seconds")

start_time = time()
fib_cached(n)
print(f"Time taken by fib_cached({n}): {time() - start_time:.4f} seconds")
