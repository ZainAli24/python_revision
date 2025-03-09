# Problem 3: Cache Return Values
# Problem: Implement a decorator that caches the return values of a function, so that when it's called
# with the same arguments, the cached value is returned instead of re-executing the function.
import time

def decorator(func):
    cached_value = {}
    print("empty", cached_value)
    def wrapper(*args, **kwargs):
        kv = tuple(sorted(kwargs.items()))
        key = (args, kv)
        if key in cached_value:
            # print(cached_value)
            return f"args value is {cached_value[key]}"
        else:
            result = func(*args, **kwargs)
            cached_value[key] = result
            # print(cached_value)
            return f"result is {result}"
    return wrapper


@decorator
def data_fetching(n, *args, **kwargs):
    time.sleep(n)
    return f"{sum(args)} and key value is {kwargs}"


print(data_fetching(5, 10, 20, name="ZAIN", age="20"))
print(data_fetching(5, 10, 20, name="ZAIN", age="20"))
print(data_fetching(5, 10, 20, name="ZAIN", age="20"))

